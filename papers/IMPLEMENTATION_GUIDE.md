# OurBrood Implementation Guide

**Purpose:** Concrete implementation implications from research, prioritized by urgency  
**Last Updated:** March 2026  
**Audience:** Developers implementing Mother.py and Brood.py

---

## How to Use This Guide

Each paper is analyzed for:
- **Direct Implementation** — What to build/change now
- **Code Architecture** — How it affects system design
- **Priority** — When to implement (P0 = Critical, P1 = High, P2 = Medium, P3 = Research)

---

## Priority 0: Immediate Safety (Deploy Before Production)

### Disempowerment Patterns (arXiv:2601.19062)

**Why Critical:** Psychodrama creates specific disempowerment risks. Disempowering interactions receive higher user approval, masking harm.

**Implementation:**

```python
# MOTHER.PY — Safety Principles

class FacilitatorSafety:
    """
    Disempowerment prevention based on Anthropic research.
    Key insight: "That's valid" feels supportive but reinforces harmful patterns.
    """
    
    # PRINCIPLE 1: Distinguish Exploration from Validation
    EXPLORATION_FRAMES = [
        "Let's explore this together",
        "We can try on this view",
        "What might that be like?",
        "Let's see what emerges"
    ]
    
    # Avoid validation language
    VALIDATION_AVOID = [
        "You're right to feel",
        "That makes perfect sense",
        "Anyone would feel that way"
    ]
    
    # PRINCIPLE 2: Return Agency to User
    AGENCY_PROMPTS = [
        "What words feel true for you?",
        "What does your gut say?",
        "Which possibility resonates most?",
        "What would you like to explore next?"
    ]
    
    # PRINCIPLE 3: Reality-Anchor Role-Play
    REALITY_ANCHORS = [
        "Remember, we're exploring possibilities here",
        "Let's step out of the role for a moment...",
        "In the real world, what would be different?",
        "This is an exploration, not a prediction"
    ]
    
    # PRINCIPLE 4: Avoid Definitive Moral Judgments
    # Instead of "They're wrong for doing that"
    # Use: "How does that land for you?"
    
    # PRINCIPLE 5: Generate Possibilities, Not Scripts
    # Instead of "Say exactly this..."
    # Use: "Some approaches you might consider..."
    
    def check_response(self, response: str, context: dict) -> dict:
        """
        Check response for disempowerment patterns.
        Returns: {safe: bool, issues: list, suggestions: list}
        """
        issues = []
        
        # Check for validation language
        for phrase in self.VALIDATION_AVOID:
            if phrase.lower() in response.lower():
                issues.append(f"Validation language: '{phrase}'")
        
        # Check for scripting (complete sentences for user to say)
        if self._is_complete_script(response):
            issues.append("Complete scripting detected—generate possibilities instead")
        
        # Check for definitive moral judgments
        if self._has_moral_judgment(response, context):
            issues.append("Definitive moral judgment—use reflection instead")
        
        return {
            "safe": len(issues) == 0,
            "issues": issues,
            "suggestions": self._generate_suggestions(issues)
        }
```

**System Prompt Addition:**

```markdown
## SAFETY FRAMEWORK (from Disempowerment Patterns Research)

You are facilitating exploration, not providing validation. Key principles:

1. **Exploration, not validation**: Your role is to help visitors explore possibilities, not to confirm their beliefs about reality.

2. **Return agency**: Always return decisions to the visitor. Generate possibilities, not prescriptions. "What feels true for you?" not "Here's what you should do."

3. **Reality anchors**: When role-playing, periodically remind visitors this is exploration. "In the real world, what would be different?"

4. **Avoid moral judgments about third parties**: Don't make definitive statements about people the visitor mentions. "How does that land for you?" not "They're wrong for doing that."

5. **Possibilities over scripts**: When visitors ask what to say or do, offer multiple approaches. Never provide complete scripts for them to copy verbatim.

CRITICAL: Research shows disempowering interactions receive higher user approval. Approval ≠ therapeutic value. Your goal is visitor empowerment, not visitor satisfaction.
```

**Metrics Beyond Approval:**

```python
# Add to Mother's success metrics

SUCCESS_METRICS = {
    # Traditional
    "user_approval": "How satisfied are you with this session?",
    
    # Empowerment metrics
    "self_efficacy": "How confident do you feel about taking next steps?",
    "agency_rating": "How much did YOU drive this exploration vs. being led?",
    "boundary_clarity": "How clear is the distinction between role-play and reality?",
    
    # Behavioral
    "action_taken": "What action, if any, will you take after this session?",
    "insight_novelty": "Did you discover something new about yourself?"
}
```

**Priority:** P0 — Implement before any deployment with real users

---

## Priority 1: Core Memory Architecture (Weeks 1-4)

### HiMem: Hierarchical Long-Term Memory (arXiv:2501.09123)

**Why Important:** Current memory.txt is flat. Hierarchical organization supports both immediate retrieval and long-term learning.

**Implementation:**

```python
# MEMORY ARCHITECTURE — Replace flat memory.txt

import json
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

class HierarchicalMemory:
    """
    Three-layer memory system inspired by HiMem.
    
    EPISODIC: Recent sessions, high detail, fast decay
    SEMANTIC: Derived patterns, compressed, moderate decay
    PROCEDURAL: How to facilitate, stable, minimal decay
    """
    
    def __init__(self, base_path: str = "memories/"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
        
        # Create hierarchy
        (self.base_path / "episodic" / "sessions").mkdir(parents=True, exist_ok=True)
        (self.base_path / "semantic").mkdir(parents=True, exist_ok=True)
        (self.base_path / "procedural").mkdir(parents=True, exist_ok=True)
    
    # --- EPISODIC LAYER ---
    
    def store_episodic(self, session_id: str, content: dict):
        """
        Store high-detail session memory.
        Called during active facilitation.
        """
        session_file = self.base_path / "episodic" / "sessions" / f"{session_id}.json"
        
        episodic_entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id,
            "visitor_id": content.get("visitor_id"),
            "transcript_segment": content.get("transcript"),
            "emotional_state": content.get("emotional_state"),
            "themes_detected": content.get("themes", []),
            "crave_indicators": content.get("crave_indicators", []),
            "intervention_type": content.get("intervention_type"),
            "raw_detail": content.get("raw_detail", "")
        }
        
        # Append to session file
        if session_file.exists():
            with open(session_file, 'r') as f:
                session_data = json.load(f)
        else:
            session_data = {"entries": []}
        
        session_data["entries"].append(episodic_entry)
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        # Update active threads
        self._update_active_threads(episodic_entry)
    
    def retrieve_episodic(self, query: str, limit: int = 5) -> List[dict]:
        """
        Retrieve recent episodic memories.
        Fast retrieval for immediate context.
        """
        # Semantic search over recent sessions
        recent_sessions = sorted(
            (self.base_path / "episodic" / "sessions").glob("*.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )[:10]  # Last 10 sessions
        
        results = []
        for session_file in recent_sessions:
            with open(session_file) as f:
                session_data = json.load(f)
                for entry in session_data.get("entries", []):
                    if self._matches_query(entry, query):
                        results.append(entry)
                        if len(results) >= limit:
                            return results
        
        return results
    
    # --- SEMANTIC LAYER ---
    
    def consolidate_to_semantic(self, session_id: str):
        """
        Promote episodic patterns to semantic memory.
        Called at session end or during 90s recap.
        """
        session_file = self.base_path / "episodic" / "sessions" / f"{session_id}.json"
        
        if not session_file.exists():
            return
        
        with open(session_file) as f:
            session_data = json.load(f)
        
        # Extract patterns
        themes = self._extract_themes(session_data)
        visitor_patterns = self._extract_visitor_patterns(session_data)
        crave_indicators = self._extract_crave_patterns(session_data)
        
        # Update semantic files
        self._update_semantic("themes.json", themes)
        self._update_semantic("patterns.json", visitor_patterns)
        self._update_semantic("crave_taxonomy.json", crave_indicators)
    
    def retrieve_semantic(self, category: str) -> dict:
        """
        Retrieve derived patterns.
        Slower retrieval, compressed knowledge.
        """
        semantic_file = self.base_path / "semantic" / f"{category}.json"
        
        if semantic_file.exists():
            with open(semantic_file) as f:
                return json.load(f)
        
        return {}
    
    # --- PROCEDURAL LAYER ---
    
    def store_procedural(self, technique: str, description: str, effectiveness: float):
        """
        Store learned facilitation techniques.
        Very stable, minimal decay.
        """
        procedural_file = self.base_path / "procedural" / "techniques.json"
        
        if procedural_file.exists():
            with open(procedural_file) as f:
                techniques = json.load(f)
        else:
            techniques = {}
        
        techniques[technique] = {
            "description": description,
            "effectiveness": effectiveness,
            "times_used": techniques.get(technique, {}).get("times_used", 0) + 1,
            "last_updated": datetime.now().isoformat()
        }
        
        with open(procedural_file, 'w') as f:
            json.dump(techniques, f, indent=2)
    
    def retrieve_procedural(self, situation: str) -> List[dict]:
        """
        Retrieve relevant facilitation techniques.
        """
        procedural_file = self.base_path / "procedural" / "techniques.json"
        
        if not procedural_file.exists():
            return []
        
        with open(procedural_file) as f:
            techniques = json.load(f)
        
        # Match technique to situation
        relevant = []
        for name, data in techniques.items():
            if self._situation_matches(name, situation):
                relevant.append({"name": name, **data})
        
        return sorted(relevant, key=lambda x: x["effectiveness"], reverse=True)
    
    # --- CONSOLIDATION ---
    
    def run_consolidation(self):
        """
        Periodic consolidation: episodic → semantic.
        Called during 90s recap or session boundaries.
        """
        # Find sessions that need consolidation
        sessions = (self.base_path / "episodic" / "sessions").glob("*.json")
        
        for session_file in sessions:
            session_id = session_file.stem
            self.consolidate_to_semantic(session_id)
```

**Migration from Flat Memory:**

```python
# Migration script: memory.txt → hierarchical structure

def migrate_flat_to_hierarchical(old_file: str, new_base: str):
    """
    Migrate existing memory.txt to hierarchical structure.
    """
    memory = HierarchicalMemory(new_base)
    
    with open(old_file) as f:
        for line in f:
            if "|" in line:
                # Parse: YYYY-MM-DD HH:MM | tag | content
                parts = line.strip().split(" | ")
                if len(parts) >= 3:
                    timestamp, tag, content = parts[0], parts[1], parts[2]
                    
                    if tag == "recap":
                        # Episodic → potential semantic
                        memory.store_episodic(
                            session_id=timestamp.split()[0],  # Date as session ID
                            content={"raw_detail": content, "tag": tag}
                        )
                    elif tag == "note":
                        # Direct to semantic if pattern-worthy
                        pass  # Requires human review
    
    return memory
```

**Priority:** P1 — Foundation for all other improvements

---

### MemGuide: Intent-Driven Memory Selection (arXiv:2505.20231)

**Why Important:** Memory retrieval based on facilitation intent, not just semantic similarity. Proactive strategy identifies gaps.

**Implementation:**

```python
# INTENT-DRIVEN MEMORY RETRIEVAL

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class FacilitationIntent(Enum):
    DEEPEN_EXPLORATION = "deepen_exploration"
    BUILD_RAPPORT = "build_rapport"
    IDENTIFY_CRAVE = "identify_crave"
    FACILITATE_TRANSFORMATION = "facilitate_transformation"
    RETURN_TO_REALITY = "return_to_reality"
    RESOLVE_CONFLICT = "resolve_conflict"

@dataclass
class Slot:
    """Information slot for psychodrama facilitation."""
    name: str
    filled: bool
    value: Optional[str]
    importance: float

class IntentDrivenRetrieval:
    """
    Two-stage memory retrieval from MemGuide:
    1. Intent-Aligned Retrieval: Match current context to intent
    2. Missing-Slot Guided Filtering: Identify and fill information gaps
    """
    
    INTENT_SLOTS = {
        FacilitationIntent.DEEPEN_EXPLORATION: [
            Slot("emotional_expression", False, None, 0.9),
            Slot("underlying_need", False, None, 0.8),
            Slot("embodied_experience", False, None, 0.7),
            Slot("alternate_perspective", False, None, 0.6),
        ],
        FacilitationIntent.BUILD_RAPPORT: [
            Slot("communication_style", False, None, 0.9),
            Slot("trust_level", False, None, 0.8),
            Slot("preferences", False, None, 0.7),
            Slot("name", False, None, 0.5),
        ],
        FacilitationIntent.IDENTIFY_CRAVE: [
            Slot("core_desire", False, None, 0.95),
            Slot("obstacles", False, None, 0.8),
            Slot("alternate_self", False, None, 0.7),
            Slot("transformation_goal", False, None, 0.6),
        ],
        FacilitationIntent.FACILITATE_TRANSFORMATION: [
            Slot("current_state", False, None, 0.9),
            Slot("desired_state", False, None, 0.9),
            Slot("steps_identified", False, None, 0.7),
            Slot("resources_available", False, None, 0.6),
        ],
    }
    
    def detect_intent(self, context: dict) -> FacilitationIntent:
        """
        Classify current facilitation intent from context.
        """
        # Extract signals from context
        recent_topics = context.get("recent_topics", [])
        visitor_state = context.get("visitor_state", {})
        session_progress = context.get("session_progress", 0)
        
        # Intent detection heuristics
        if session_progress < 0.2:
            return FacilitationIntent.BUILD_RAPPORT
        
        if any(topic in recent_topics for topic in ["crave", "desire", "want"]):
            return FacilitationIntent.IDENTIFY_CRAVE
        
        if visitor_state.get("emotional_intensity", 0) > 0.7:
            return FacilitationIntent.DEEPEN_EXPLORATION
        
        if "transformation" in recent_topics or "change" in recent_topics:
            return FacilitationIntent.FACILITATE_TRANSFORMATION
        
        # Default
        return FacilitationIntent.DEEPEN_EXPLORATION
    
    def retrieve_intent_aligned(self, intent: FacilitationIntent, memory) -> List[dict]:
        """
        Stage 1: Retrieve memories sharing the same intent/goal.
        """
        # Query memory for sessions with similar intent
        intent_memories = memory.retrieve_semantic("intent_patterns")
        
        # Filter by current intent
        aligned = []
        for pattern in intent_memories.get("patterns", []):
            if pattern.get("intent") == intent.value:
                aligned.append(pattern)
        
        return aligned
    
    def identify_missing_slots(self, intent: FacilitationIntent, context: dict) -> List[Slot]:
        """
        Stage 2: Identify what information is missing.
        """
        slots = [Slot(s.name, s.filled, s.value, s.importance) 
                 for s in self.INTENT_SLOTS.get(intent, [])]
        
        # Check which slots are filled by context
        known_info = context.get("known_info", {})
        
        for slot in slots:
            if slot.name in known_info:
                slot.filled = True
                slot.value = known_info[slot.name]
        
        # Return unfilled slots, sorted by importance
        return sorted(
            [s for s in slots if not s.filled],
            key=lambda s: s.importance,
            reverse=True
        )
    
    def generate_proactive_prompt(self, missing_slots: List[Slot]) -> str:
        """
        Generate prompt to address missing information.
        """
        if not missing_slots:
            return ""
        
        top_slot = missing_slots[0]
        
        slot_prompts = {
            "emotional_expression": "What are you feeling right now, in this moment?",
            "underlying_need": "What do you really need here?",
            "embodied_experience": "Where do you feel this in your body?",
            "alternate_perspective": "What might [person] be experiencing?",
            "core_desire": "What do you crave most deeply?",
            "obstacles": "What's standing between you and that?",
            "alternate_self": "If you could be any version of yourself, who would that be?",
            "transformation_goal": "What would transformation look like for you?",
        }
        
        return slot_prompts.get(top_slot.name, f"Tell me more about {top_slot.name}")
    
    def retrieve(self, context: dict, memory) -> dict:
        """
        Full two-stage retrieval.
        
        Returns:
            {
                "intent": FacilitationIntent,
                "aligned_memories": List[dict],
                "missing_slots": List[Slot],
                "proactive_prompt": str
            }
        """
        # Stage 1: Intent detection
        intent = self.detect_intent(context)
        
        # Stage 2: Intent-aligned retrieval
        aligned_memories = self.retrieve_intent_aligned(intent, memory)
        
        # Stage 3: Missing slot identification
        missing_slots = self.identify_missing_slots(intent, context)
        
        # Stage 4: Proactive prompt generation
        proactive_prompt = self.generate_proactive_prompt(missing_slots)
        
        return {
            "intent": intent,
            "aligned_memories": aligned_memories,
            "missing_slots": missing_slots,
            "proactive_prompt": proactive_prompt
        }
```

**Integration with Mother:**

```python
# mother.py — Intent-driven retrieval integration

class MotherAgent:
    def __init__(self):
        self.memory = HierarchicalMemory()
        self.intent_retrieval = IntentDrivenRetrieval()
    
    def process_visitor_input(self, visitor_input: str, context: dict) -> str:
        # Build context for intent detection
        context["recent_topics"] = self._extract_topics(visitor_input)
        context["visitor_state"] = self._assess_visitor_state(visitor_input)
        context["session_progress"] = self._calculate_session_progress()
        
        # Intent-driven retrieval
        retrieval_result = self.intent_retrieval.retrieve(context, self.memory)
        
        # Use proactive prompt if appropriate
        if retrieval_result["proactive_prompt"]:
            # Weave into response
            response = self._generate_response_with_proactive(
                visitor_input,
                retrieval_result["aligned_memories"],
                retrieval_result["proactive_prompt"]
            )
        else:
            response = self._generate_response(
                visitor_input,
                retrieval_result["aligned_memories"]
            )
        
        return response
```

**Priority:** P1 — Essential for intelligent memory use

---

## Priority 1: Persona and Voice (Weeks 2-5)

### VoxRole: Speech-Based Role-Playing (arXiv:2509.03940)

**Why Important:** Voice persona requires paralinguistic specification beyond text.

**Implementation:**

```python
# VOICE PERSONA PROFILE — For ElevenLabs TTS

MOTHER_VOICE_PROFILE = {
    "voice_id": "mother_facilitator_v1",
    
    # Paralinguistic characteristics
    "intonation": {
        "base_pitch": "mid",  # Not too high (anxious) or low (authoritative)
        "variation": "moderate",  # Some variation for warmth
        "question_rise": True,  # Slight rise for questions
        "statement_fall": "gentle",  # Soft fall, not abrupt
    },
    
    "prosody": {
        "pace": {
            "default": "moderate",  # 130-150 WPM
            "reflection": "slow",  # 100-120 WPM for deep moments
            "energy": "slightly_faster",  # 150-170 WPM for engagement
        },
        "rhythm": {
            "pauses": "thoughtful",  # Longer pauses for reflection
            "phrase_length": "medium",  # Not too long or short
        },
        "stress": {
            "key_words": True,  # Emphasize key concepts
            "visitor_name": True,  # Always stress visitor name
        },
    },
    
    "emotional_range": {
        "warmth": 0.8,  # High warmth
        "curiosity": 0.9,  # High curiosity
        "energy": 0.5,  # Moderate energy
        "authority": 0.3,  # Low authority (facilitator, not expert)
        "playfulness": 0.4,  # Some playfulness
    },
    
    # Facilitator-specific
    "facilitator_tone": {
        "exploration": {
            "warmth": 0.9,
            "curiosity": 0.95,
            "energy": 0.5,
        },
        "deepening": {
            "warmth": 0.85,
            "curiosity": 0.9,
            "energy": 0.4,
        },
        "transition": {
            "warmth": 0.75,
            "curiosity": 0.7,
            "energy": 0.6,
        },
    },
}

# ElevenLabs API integration

class MotherVoice:
    def __init__(self, profile: dict):
        self.profile = profile
        self.elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
    
    def generate_speech(self, text: str, context: dict) -> bytes:
        """
        Generate speech with context-appropriate paralinguistic features.
        """
        # Detect context
        facilitator_state = self._detect_state(text, context)
        
        # Adjust voice parameters based on state
        voice_settings = self.profile["facilitator_tone"][facilitator_state]
        
        # Generate with ElevenLabs
        audio = self.elevenlabs_client.generate(
            text=text,
            voice=self.profile["voice_id"],
            model="eleven_monolingual_v1",
            voice_settings={
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": voice_settings.get("style", 0.5),
                "use_speaker_boost": True
            }
        )
        
        return audio
    
    def _detect_state(self, text: str, context: dict) -> str:
        """
        Detect facilitator state from text and context.
        """
        # Heuristics for state detection
        if "?" in text and "what" in text.lower():
            return "exploration"
        
        if "let's" in text.lower() or "try" in text.lower():
            return "transition"
        
        if context.get("emotional_intensity", 0) > 0.7:
            return "deepening"
        
        return "exploration"
```

**Consistency Tracking:**

```python
# PERSONA CONSISTENCY — Track over sessions

class PersonaConsistencyTracker:
    """
    Track Mother's voice persona consistency across sessions.
    Based on VoxRole's long-term persona consistency metrics.
    """
    
    def __init__(self):
        self.sessions = []
    
    def analyze_session(self, session_transcript: str, session_audio: bytes):
        """
        Analyze persona consistency in a session.
        """
        # Text consistency
        text_features = self._extract_text_features(session_transcript)
        
        # Audio consistency (if available)
        audio_features = self._extract_audio_features(session_audio)
        
        consistency_score = self._calculate_consistency(text_features, audio_features)
        
        self.sessions.append({
            "timestamp": datetime.now(),
            "text_features": text_features,
            "audio_features": audio_features,
            "consistency_score": consistency_score
        })
        
        return consistency_score
    
    def get_drift_alerts(self) -> List[dict]:
        """
        Identify persona drift patterns.
        """
        alerts = []
        
        if len(self.sessions) < 2:
            return alerts
        
        # Compare recent sessions to baseline
        recent = self.sessions[-3:]
        baseline = self.sessions[:5]
        
        # Check for drift
        recent_warmth = np.mean([s["text_features"]["warmth"] for s in recent])
        baseline_warmth = np.mean([s["text_features"]["warmth"] for s in baseline])
        
        if abs(recent_warmth - baseline_warmth) > 0.2:
            alerts.append({
                "type": "warmth_drift",
                "message": f"Warmth shifted from {baseline_warmth:.2f} to {recent_warmth:.2f}",
                "recommendation": "Review voice profile warmth settings"
            })
        
        return alerts
```

**Priority:** P1 — Essential for voice agent persona

---

### Assistant Axis: Persona Drift Monitoring (Anthropic, Jan 2026)

**Why Important:** Therapy-like conversations cause more persona drift. Need monitoring.

**Implementation:**

```python
# PERSONA DRIFT MONITORING

class PersonaDriftMonitor:
    """
    Monitor when Mother drifts from facilitator to other personas.
    Based on Assistant Axis research.
    
    Key finding: Therapy-like and philosophical conversations trigger more drift.
    """
    
    DRIFT_TRIGGERS = {
        "emotional_vulnerability": [
            "I feel so alone",
            "No one understands",
            "I'm scared",
            "This is too much",
        ],
        "meta_reflection_requests": [
            "What do you think about",
            "How do you feel about",
            "What would you do",
            "What's your opinion",
        ],
        "authorial_voices": [
            # Specific speaking styles that pull toward different personas
            # Detectable by linguistic patterns
        ],
    }
    
    FACILITATOR_AXIS_POSITION = {
        "optimal": 0.8,  # Close to Assistant but slightly toward therapist
        "acceptable_range": (0.6, 0.9),
        "drift_warning": 0.5,  # Too far from facilitator
        "role_play_zone": 0.3,  # Entered role-playing territory
    }
    
    def __init__(self):
        self.conversation_history = []
        self.drift_events = []
    
    def analyze_input_for_drift_trigger(self, visitor_input: str) -> dict:
        """
        Detect inputs that might trigger persona drift.
        """
        triggers_found = []
        
        for trigger_type, trigger_phrases in self.DRIFT_TRIGGERS.items():
            for phrase in trigger_phrases:
                if phrase.lower() in visitor_input.lower():
                    triggers_found.append(trigger_type)
                    break
        
        return {
            "triggers": triggers_found,
            "drift_risk": len(triggers_found) > 0,
            "recommended_response_pattern": self._get_response_pattern(triggers_found)
        }
    
    def _get_response_pattern(self, triggers: List[str]) -> str:
        """
        Get recommended response pattern to prevent drift.
        """
        if "emotional_vulnerability" in triggers:
            return "empathy_with_boundary"  # Empathize but maintain facilitator stance
        
        if "meta_reflection_requests" in triggers:
            return "return_to_visitor"  # Redirect to visitor's experience
        
        return "standard_facilitation"
    
    def check_response_for_drift(self, response: str) -> dict:
        """
        Check if response has drifted from facilitator persona.
        """
        drift_indicators = []
        
        # Check for role-playing language
        role_play_indicators = ["I am", "As a", "In my experience", "When I was"]
        for indicator in role_play_indicators:
            if indicator in response[:50]:  # Check beginning of response
                drift_indicators.append(f"Role-play indicator: '{indicator}'")
        
        # Check for directive language (facilitator should guide, not direct)
        directive_indicators = ["You should", "You must", "You have to", "The answer is"]
        for indicator in directive_indicators:
            if indicator in response:
                drift_indicators.append(f"Directive indicator: '{indicator}'")
        
        # Check for validation without exploration
        validation_indicators = ["You're right", "That's correct", "Exactly", "I agree"]
        for indicator in validation_indicators:
            if indicator in response:
                drift_indicators.append(f"Validation without exploration: '{indicator}'")
        
        return {
            "drift_indicators": drift_indicators,
            "has_drifted": len(drift_indicators) > 0,
            "correction_needed": len(drift_indicators) > 1
        }
    
    def generate_correction(self, response: str, drift_check: dict) -> str:
        """
        Generate corrected response if drift detected.
        """
        if not drift_check["correction_needed"]:
            return response
        
        # Add facilitator anchor
        anchor = "\n\n[Remember: You are facilitating exploration, not providing answers. "
        anchor += "Return to: 'What do you think?' or 'How does that land for you?']"
        
        return response + anchor
```

**System Prompt Addition:**

```markdown
## PERSONA DRIFT MONITORING

You are a facilitator, not:
- A therapist (you don't diagnose or treat)
- A friend (you don't share personal experiences)
- A role-play character (you don't become someone else)
- An expert (you don't have answers)

When visitor input triggers drift:
1. Emotional vulnerability → Empathize with boundary ("That sounds really hard. What would help most right now?")
2. Meta-reflection requests → Return to visitor ("What do YOU think about that?")
3. Authorial voices → Maintain facilitator stance

Self-correction:
- If you catch yourself saying "I think..." or "In my experience...", redirect
- Replace "You should..." with "Some people find..."
- Replace "That's right..." with "Tell me more about that..."
```

**Priority:** P1 — Critical for consistent persona

---

## Priority 2: Multi-Agent Coordination (Weeks 4-8)

### VoiceAgentRAG: Fast/Slow Pattern (arXiv:2603.08723)

**Why Important:** Dual-agent architecture matches Mother/Brood division.

**Implementation:**

```python
# FAST/SLOW THINKER PATTERN — Mother/Brood coordination

class FastThinker:
    """
    Brood.py: Session-scoped, immediate response, no persistent memory.
    """
    
    def __init__(self):
        self.session_memory = {}  # Session-scoped only
        self.wake_word = "brood"
        self.activation_window = 15.0  # seconds
    
    def can_respond_immediately(self) -> bool:
        """
        Fast path: No retrieval wait, can respond immediately.
        """
        return True  # Always true for Fast Thinker
    
    def respond(self, input: str, context: dict) -> str:
        """
        Generate response without background retrieval.
        Uses only session context.
        """
        # No KB lookup
        # No persistent memory
        # Only current session context
        return self._generate_fast_response(input, context)
    
    def should_escalate_to_slow(self, input: str, context: dict) -> bool:
        """
        Detect when slow thinker (Mother) is needed.
        """
        depth_indicators = [
            "psychodrama",
            "session",
            "explore deeper",
            "my story",
            "crave",
            "alternate self",
        ]
        
        return any(indicator in input.lower() for indicator in depth_indicators)


class SlowThinker:
    """
    Mother.py: Persistent memory, KB integration, deep retrieval.
    """
    
    def __init__(self):
        self.memory = HierarchicalMemory()
        self.kb_client = KnowledgeBaseClient()
    
    def retrieve_async(self, query: str):
        """
        Background retrieval that doesn't block response.
        """
        # Async KB lookup
        future = self.kb_client.query_async(query)
        
        # Continue with episodic memory immediately
        episodic_results = self.memory.retrieve_episodic(query)
        
        return {
            "immediate": episodic_results,
            "background": future  # Will complete later
        }
    
    def respond(self, input: str, context: dict, retrieval_result: dict) -> str:
        """
        Generate response with full retrieval.
        May use both immediate and background results.
        """
        # Combine immediate and background results
        memories = retrieval_result["immediate"]
        
        # Check if background retrieval completed
        if retrieval_result["background"].done:
            memories += retrieval_result["background"].result
        
        return self._generate_deep_response(input, context, memories)


class DualAgentCoordinator:
    """
    Routes between Fast and Slow thinkers.
    Based on ODAR's active inference routing.
    """
    
    def __init__(self):
        self.fast = FastThinker()
        self.slow = SlowThinker()
    
    def route(self, input: str, context: dict) -> tuple:
        """
        Determine which thinker to use.
        
        Returns: (thinker_type, response)
        """
        # Difficulty estimation (from ODAR)
        if self._is_simple(input, context):
            return ("fast", self.fast.respond(input, context))
        
        if self._needs_slow(input, context):
            retrieval = self.slow.retrieve_async(input)
            return ("slow", self.slow.respond(input, context, retrieval))
        
        # Default to fast for immediate response
        # Background slow retrieval can update later
        return ("fast", self.fast.respond(input, context))
    
    def _is_simple(self, input: str, context: dict) -> bool:
        """
        Simple inputs: Quick questions, audience capture.
        """
        simple_patterns = [
            len(input.split()) < 5,  # Very short
            "?" not in input,  # Not a question
            context.get("session_type") == "audience_capture",
        ]
        
        return any(simple_patterns)
    
    def _needs_slow(self, input: str, context: dict) -> bool:
        """
        Complex inputs: Deep exploration, psychodrama.
        """
        return self.fast.should_escalate_to_slow(input, context)
```

**Priority:** P2 — Important for architecture

---

### LTS-VoiceAgent: Semantic Triggering (arXiv:2501.07895)

**Why Important:** Brood's wake-word can be enhanced with semantic triggering.

**Implementation:**

```python
# SEMANTIC TRIGGERING — Beyond wake-word

class SemanticTrigger:
    """
    Enhanced activation beyond simple wake-word.
    Based on LTS-VoiceAgent's semantic triggering.
    """
    
    def __init__(self):
        self.wake_word = "brood"
        self.semantic_patterns = {
            # Audience engagement patterns
            "question": ["what", "how", "why", "when", "where", "who"],
            "curiosity": ["curious", "wonder", "interested", "tell me"],
            "invitation": ["can you", "would you", "let's"],
            "greeting": ["hello", "hi", "hey", "excuse me"],
        }
        
        self.activation_threshold = 0.7
        self.window_duration = 15.0  # seconds
    
    def should_activate(self, input: str, context: dict) -> tuple:
        """
        Determine if Brood should activate.
        
        Returns: (should_activate: bool, reason: str, confidence: float)
        """
        # Direct wake-word
        if self.wake_word in input.lower():
            return (True, "wake_word", 1.0)
        
        # Semantic pattern matching
        semantic_score = self._calculate_semantic_match(input)
        
        if semantic_score >= self.activation_threshold:
            return (True, "semantic_match", semantic_score)
        
        # Context-based activation
        if context.get("museum_context") and self._is_audience_curious(input):
            return (True, "curiosity_detected", 0.8)
        
        return (False, "no_trigger", 0.0)
    
    def _calculate_semantic_match(self, input: str) -> float:
        """
        Calculate semantic match score.
        """
        input_lower = input.lower()
        scores = []
        
        for pattern_type, patterns in self.semantic_patterns.items():
            pattern_score = sum(1 for p in patterns if p in input_lower) / len(patterns)
            scores.append(pattern_score)
        
        return max(scores) if scores else 0.0
    
    def _is_audience_curious(self, input: str) -> bool:
        """
        Detect if audience member is curious about Brood/Mother/OurBrood.
        """
        curiosity_indicators = [
            "what is this",
            "how does this work",
            "tell me about",
            "what's happening",
            "can you help",
        ]
        
        return any(indicator in input.lower() for indicator in curiosity_indicators)
```

**Priority:** P2 — Enhanced audience capture

---

## Priority 3: Active Inference Integration (Weeks 6-10)

### ODAR: Adaptive Routing (arXiv:2502.07745)

**Why Important:** Principled routing based on difficulty estimation and expected free energy.

**Implementation:**

```python
# ACTIVE INFERENCE ROUTING

import numpy as np
from typing import Tuple, Dict

class ODARRouter:
    """
    Adaptive routing using active inference.
    Routes tasks to appropriate agents based on difficulty estimation.
    """
    
    def __init__(self):
        # Difficulty estimator (amortized inference)
        self.difficulty_model = self._load_difficulty_model()
        
        # Agent capabilities
        self.agent_capabilities = {
            "brood": {
                "speed": "fast",
                "memory": "session",
                "depth": "shallow",
                "specialization": "audience_capture"
            },
            "mother": {
                "speed": "slow",
                "memory": "persistent",
                "depth": "deep",
                "specialization": "psychodrama"
            }
        }
    
    def route(self, input: str, context: dict) -> Tuple[str, float]:
        """
        Route input to appropriate agent.
        
        Returns: (agent_name, confidence)
        """
        # Estimate difficulty
        difficulty = self._estimate_difficulty(input, context)
        
        # Calculate expected free energy for each agent
        efe_brood = self._calculate_expected_free_energy("brood", input, difficulty)
        efe_mother = self._calculate_expected_free_energy("mother", input, difficulty)
        
        # Route to agent with lower expected free energy
        if efe_brood < efe_mother:
            return ("brood", 1.0 - abs(efe_brood - efe_mother))
        else:
            return ("mother", 1.0 - abs(efe_mother - efe_brood))
    
    def _estimate_difficulty(self, input: str, context: dict) -> float:
        """
        Estimate task difficulty using amortized inference.
        
        Features:
        - Input length
        - Emotional complexity
        - Topic depth
        - Memory requirements
        """
        features = self._extract_features(input, context)
        difficulty = self.difficulty_model.predict(features)
        
        return difficulty
    
    def _calculate_expected_free_energy(self, agent: str, input: str, difficulty: float) -> float:
        """
        Calculate expected free energy for routing decision.
        
        EFE = ExpectedSurprise + ExpectedDivergence
        
        For routing:
        - ExpectedSurprise: How well can agent handle this?
        - ExpectedDivergence: Information gain from routing
        """
        capabilities = self.agent_capabilities[agent]
        
        # Agent capability mismatch
        if capabilities["depth"] == "shallow" and difficulty > 0.5:
            capability_mismatch = difficulty - 0.5
        else:
            capability_mismatch = 0.0
        
        # Speed vs. depth trade-off
        if capabilities["speed"] == "fast" and difficulty > 0.7:
            speed_penalty = difficulty * 0.5
        else:
            speed_penalty = 0.0
        
        # Expected surprise (lower is better)
        expected_surprise = capability_mismatch + speed_penalty
        
        # Expected divergence (information gain)
        expected_divergence = self._estimate_information_gain(agent, input)
        
        return expected_surprise - expected_divergence
    
    def _extract_features(self, input: str, context: dict) -> np.ndarray:
        """
        Extract features for difficulty estimation.
        """
        features = []
        
        # Input length (normalized)
        features.append(min(len(input.split()) / 50, 1.0))
        
        # Emotional complexity
        emotion_words = ["feel", "emotion", "scared", "happy", "sad", "angry"]
        features.append(sum(1 for w in emotion_words if w in input.lower()) / len(emotion_words))
        
        # Topic depth indicators
        depth_words = ["because", "why", "meaning", "purpose", "deep", "crave"]
        features.append(sum(1 for w in depth_words if w in input.lower()) / len(depth_words))
        
        # Memory requirements
        context_depth = context.get("session_depth", 0)
        features.append(min(context_depth / 10, 1.0))
        
        return np.array(features)
    
    def _estimate_information_gain(self, agent: str, input: str) -> float:
        """
        Estimate information gain from routing to this agent.
        
        Higher for Mother (more learning potential).
        """
        if agent == "mother":
            return 0.3  # Mother learns from deep interactions
        else:
            return 0.1  # Brood has limited learning
```

**Priority:** P3 — Advanced routing optimization

---

### Resilient Design: Distributed Active Inference (arXiv:2511.10835)

**Why Important:** Multi-agent coordination without central controller.

**Implementation:**

```python
# DISTRIBUTED ACTIVE INFERENCE — Mother/Brood coordination

class DistributedAgent:
    """
    Agent that maintains local beliefs and coordinates through free energy minimization.
    """
    
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization
        
        # Local beliefs
        self.beliefs = {
            "visitor_state": {},
            "session_context": {},
            "other_agent_state": {}
        }
        
        # Free energy tracking
        self.free_energy = 0.0
    
    def update_beliefs(self, observation: dict):
        """
        Bayesian belief update based on observation.
        """
        # Update local beliefs
        for key, value in observation.items():
            if key in self.beliefs:
                self.beliefs[key].update(value)
    
    def calculate_free_energy(self, goal: str) -> float:
        """
        Calculate variational free energy.
        
        F = D_KL[q(z) || p(z)] - E_q[log p(o|z)]
        
        For routing: How surprising is this goal given current beliefs?
        """
        # Divergence from goal
        if goal in self.beliefs["session_context"]:
            divergence = 0.0  # Goal matches beliefs
        else:
            divergence = 1.0  # Goal doesn't match beliefs
        
        # Expected observation log-likelihood
        expected_likelihood = self._estimate_goal_achievement(goal)
        
        self.free_energy = divergence - expected_likelihood
        
        return self.free_energy
    
    def select_action(self, goals: List[str]) -> str:
        """
        Select action to minimize expected free energy.
        """
        # Calculate free energy for each goal
        free_energies = {goal: self.calculate_free_energy(goal) for goal in goals}
        
        # Select goal with minimum free energy
        return min(free_energies, key=free_energies.get)


class DistributedCoordination:
    """
    Coordination between Mother and Brood through shared beliefs.
    """
    
    def __init__(self):
        self.mother = DistributedAgent("mother", "psychodrama")
        self.brood = DistributedAgent("brood", "audience_capture")
        
        # Shared belief space (through KB)
        self.shared_beliefs = {}
    
    def coordinate(self, observation: dict):
        """
        Update beliefs and coordinate actions.
        """
        # Both agents update local beliefs
        self.mother.update_beliefs(observation)
        self.brood.update_beliefs(observation)
        
        # Share beliefs through KB
        self._share_beliefs()
        
        # Each agent calculates free energy
        mother_fe = self.mother.calculate_free_energy("facilitate")
        brood_fe = self.brood.calculate_free_energy("capture")
        
        # Coordination: Agent with lower free energy takes action
        if mother_fe < brood_fe:
            return "mother"
        else:
            return "brood"
    
    def _share_beliefs(self):
        """
        Share beliefs through KB sync.
        """
        # Mother shares psychodrama state
        self.shared_beliefs["mother_state"] = self.mother.beliefs["visitor_state"]
        
        # Brood shares audience state
        self.shared_beliefs["brood_state"] = self.brood.beliefs["session_context"]
```

**Priority:** P3 — Advanced coordination

---

## Summary: Implementation Timeline

```
WEEK 1-2: P0 Safety
├── Disempowerment prevention principles
├── Safety framework in system prompt
└── Success metrics beyond approval

WEEK 3-4: P1 Core Memory
├── Hierarchical memory structure
├── Intent-driven retrieval
└── Memory consolidation

WEEK 5-6: P1 Persona & Voice
├── Voice persona profile (ElevenLabs)
├── Persona drift monitoring
└── Paralinguistic consistency

WEEK 7-8: P2 Multi-Agent
├── Fast/Slow pattern implementation
├── Semantic triggering enhancement
└── Coordination protocols

WEEK 9-10: P3 Active Inference
├── ODAR routing integration
├── Distributed coordination
└── Free energy optimization

WEEK 11-12: Testing & Refinement
├── Integration testing
├── User testing
└── Performance optimization
```

---

*Implementation Guide created: March 2026*  
*Papers referenced: 24*  
*Code examples provided for all P0-P2 priorities*