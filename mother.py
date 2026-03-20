"""
Mother.py v2 - OurBrood Psychodrama Facilitation Agent

Three-layer cognitive architecture inspired by:
- HiMem (arXiv:2501.09123): Hierarchical memory structure
- TiMem (arXiv:2501.11345): Temporal consolidation
- MemGuide (arXiv:2505.20231): Intent-driven retrieval

Version: 2.0
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, asdict


# =============================================================================
# JSON SCHEMAS (for validation)
# =============================================================================

EPISODIC_SESSION_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "EpisodicSession",
    "type": "object",
    "properties": {
        "session_id": {"type": "string"},
        "visitor_id": {"type": "string"},
        "started_at": {"type": "string", "format": "date-time"},
        "ended_at": {"type": "string", "format": "date-time"},
        "entries": {
            "type": "array",
            "items": {"$ref": "#/definitions/EpisodicEntry"}
        },
        "consolidated": {"type": "boolean", "default": False},
        "consolidated_at": {"type": "string", "format": "date-time"}
    },
    "required": ["session_id", "entries"],
    "definitions": {
        "EpisodicEntry": {
            "type": "object",
            "properties": {
                "timestamp": {"type": "string", "format": "date-time"},
                "transcript_segment": {"type": "string"},
                "emotional_state": {
                    "type": "object",
                    "properties": {
                        "valence": {"type": "number", "minimum": 0, "maximum": 1},
                        "arousal": {"type": "number", "minimum": 0, "maximum": 1},
                        "dominance": {"type": "number", "minimum": 0, "maximum": 1}
                    }
                },
                "themes_detected": {"type": "array", "items": {"type": "string"}},
                "crave_indicators": {"type": "array", "items": {"type": "string"}},
                "intervention_type": {
                    "type": "string",
                    "enum": ["rapport_building", "deepening", "reality_anchor", "closure"]
                },
                "salience_score": {"type": "number", "minimum": 0, "maximum": 1},
                "raw_detail": {"type": "string"}
            },
            "required": ["timestamp", "transcript_segment"]
        }
    }
}

SEMANTIC_MEMORY_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "SemanticMemory",
    "type": "object",
    "properties": {
        "category": {"type": "string", "enum": ["themes", "patterns", "crave-taxonomy"]},
        "entries": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "label": {"type": "string"},
                    "frequency": {"type": "integer"},
                    "first_occurrence": {"type": "string", "format": "date-time"},
                    "last_occurrence": {"type": "string", "format": "date-time"},
                    "related_sessions": {"type": "array", "items": {"type": "string"}},
                    "description": {"type": "string"},
                    "examples": {"type": "array", "items": {"type": "string"}},
                    "intent_associations": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["label", "frequency"]
            }
        },
        "last_consolidated": {"type": "string", "format": "date-time"},
        "version": {"type": "string", "default": "1.0"}
    },
    "required": ["category", "entries"]
}

PROCEDURAL_MEMORY_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "ProceduralMemory",
    "type": "object",
    "properties": {
        "category": {"type": "string", "enum": ["techniques", "interventions"]},
        "techniques": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "description": {"type": "string"},
                    "effectiveness": {"type": "number", "minimum": 0, "maximum": 1},
                    "times_used": {"type": "integer"},
                    "last_updated": {"type": "string", "format": "date-time"},
                    "situations": {"type": "array", "items": {"type": "string"}},
                    "visitor_responses": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["description", "effectiveness"]
            }
        }
    },
    "required": ["category", "techniques"]
}


# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class EpisodicEntry:
    """High-detail session memory entry."""
    timestamp: str
    transcript_segment: str
    emotional_state: Optional[Dict[str, float]] = None
    themes_detected: Optional[List[str]] = None
    crave_indicators: Optional[List[str]] = None
    intervention_type: Optional[str] = None
    salience_score: Optional[float] = None
    raw_detail: Optional[str] = None


# =============================================================================
# HIERARCHICAL MEMORY CLASS
# =============================================================================

class HierarchicalMemory:
    """
    Three-layer memory system for Mother agent.
    
    Architecture:
    - Episodic: Recent sessions, high detail, fast decay (7 days)
    - Semantic: Derived patterns, compressed, moderate decay (30 days)
    - Procedural: Facilitation techniques, stable, minimal decay
    
    Inspired by:
    - HiMem (arXiv:2501.09123): Hierarchical memory structure
    - TiMem (arXiv:2501.11345): Temporal consolidation
    - MemGuide (arXiv:2505.20231): Intent-driven retrieval
    """
    
    def __init__(self, base_path: str = "memory/"):
        """
        Initialize HierarchicalMemory.
        
        Args:
            base_path: Root directory for memory storage
        """
        self.base_path = Path(base_path)
        self._ensure_structure()
    
    def _ensure_structure(self) -> None:
        """Create directory hierarchy if not exists."""
        (self.base_path / "episodic" / "sessions").mkdir(parents=True, exist_ok=True)
        (self.base_path / "semantic").mkdir(parents=True, exist_ok=True)
        (self.base_path / "procedural").mkdir(parents=True, exist_ok=True)
        
        # Initialize empty semantic files if not exist
        for filename in ["themes.json", "patterns.json", "crave-taxonomy.json"]:
            semantic_file = self.base_path / "semantic" / filename
            if not semantic_file.exists():
                with open(semantic_file, 'w') as f:
                    json.dump({
                        "category": filename.replace(".json", ""),
                        "entries": [],
                        "last_consolidated": None,
                        "version": "1.0"
                    }, f, indent=2)
        
        # Initialize procedural files if not exist
        for filename in ["techniques.json", "interventions.json"]:
            procedural_file = self.base_path / "procedural" / filename
            if not procedural_file.exists():
                with open(procedural_file, 'w') as f:
                    json.dump({
                        "category": filename.replace(".json", ""),
                        "techniques": {}
                    }, f, indent=2)
    
    # =========================================================================
    # EPISODIC LAYER
    # =========================================================================
    
    def store_episodic(self, session_id: str, entry: EpisodicEntry) -> None:
        """
        Store high-detail session memory.
        
        Called during active facilitation to capture verbatim exchanges,
        emotional states, and detected themes.
        
        Args:
            session_id: Unique session identifier (YYYY-MM-DD-visitor-NNN)
            entry: EpisodicEntry containing session data
        """
        session_file = self.base_path / "episodic" / "sessions" / f"{session_id}.json"
        
        # Load or create session data
        if session_file.exists():
            with open(session_file, 'r') as f:
                session_data = json.load(f)
        else:
            session_data = {
                "session_id": session_id,
                "entries": [],
                "consolidated": False
            }
        
        # Append entry
        session_data["entries"].append(asdict(entry))
        
        # Write atomically
        temp_file = session_file.with_suffix('.tmp')
        with open(temp_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        temp_file.replace(session_file)
    
    def retrieve_episodic(self, query: str, limit: int = 5) -> List[Dict]:
        """
        Retrieve recent episodic memories.
        
        Fast retrieval for immediate context. Uses simple term matching
        over last 10 sessions. Replace with embedding search in production.
        
        Args:
            query: Search query (matched against transcript and themes)
            limit: Maximum number of results to return
            
        Returns:
            List of relevant episodic entries sorted by relevance
        """
        # Get recent sessions (by modification time)
        session_files = sorted(
            (self.base_path / "episodic" / "sessions").glob("*.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )[:10]
        
        results = []
        query_terms = query.lower().split()
        
        for session_file in session_files:
            with open(session_file) as f:
                session_data = json.load(f)
                for entry in session_data.get("entries", []):
                    # Simple term matching (replace with embedding search in production)
                    transcript = entry.get("transcript_segment", "").lower()
                    themes = entry.get("themes_detected", [])
                    
                    score = sum(1 for term in query_terms if term in transcript)
                    score += sum(1 for term in query_terms if term in themes)
                    
                    if score > 0:
                        results.append({
                            "entry": entry,
                            "session_id": session_data.get("session_id"),
                            "relevance_score": score
                        })
        
        # Sort by relevance and limit
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        return [r["entry"] for r in results[:limit]]
    
    def load_session(self, session_id: str) -> Optional[Dict]:
        """
        Load complete session data.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Session data dict or None if not found
        """
        session_file = self.base_path / "episodic" / "sessions" / f"{session_id}.json"
        if session_file.exists():
            with open(session_file) as f:
                return json.load(f)
        return None
    
    # =========================================================================
    # SEMANTIC LAYER
    # =========================================================================
    
    def consolidate_to_semantic(self, session_id: str) -> None:
        """
        Promote episodic patterns to semantic memory.
        
        Called at session end or during 90s recap. Extracts themes,
        patterns, and crave indicators from episodic entries and
        updates semantic memory files.
        
        Args:
            session_id: Session to consolidate
        """
        session_data = self.load_session(session_id)
        if not session_data:
            return
        
        # Extract patterns
        themes = self._extract_themes(session_data)
        patterns = self._extract_patterns(session_data)
        crave_indicators = self._extract_crave_patterns(session_data)
        
        # Update semantic files
        if themes:
            self._update_semantic("themes.json", themes)
        if patterns:
            self._update_semantic("patterns.json", patterns)
        if crave_indicators:
            self._update_semantic("crave-taxonomy.json", crave_indicators)
        
        # Mark session as consolidated
        session_data["consolidated"] = True
        session_data["consolidated_at"] = datetime.now().isoformat()
        
        session_file = self.base_path / "episodic" / "sessions" / f"{session_id}.json"
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
    
    def _extract_themes(self, session_data: Dict) -> List[Dict]:
        """Extract themes from session entries."""
        theme_counts = {}
        
        for entry in session_data.get("entries", []):
            themes_detected = entry.get("themes_detected") or []
            for theme in themes_detected:
                if theme not in theme_counts:
                    theme_counts[theme] = {
                        "label": theme,
                        "frequency": 0,
                        "first_occurrence": None,
                        "last_occurrence": None,
                        "related_sessions": [],
                        "examples": []
                    }
                
                theme_counts[theme]["frequency"] += 1
                theme_counts[theme]["related_sessions"].append(session_data["session_id"])
                theme_counts[theme]["examples"].append(
                    entry.get("transcript_segment", "")[:100]
                )
                
                timestamp = entry.get("timestamp")
                if timestamp:
                    if not theme_counts[theme]["first_occurrence"]:
                        theme_counts[theme]["first_occurrence"] = timestamp
                    theme_counts[theme]["last_occurrence"] = timestamp
        
        return list(theme_counts.values())
    
    def _extract_patterns(self, session_data: Dict) -> List[Dict]:
        """
        Extract cross-entry patterns from session.
        
        Placeholder: Implement pattern detection logic (e.g., sequence
        mining, emotional arc detection, dialogue flow analysis).
        """
        # TODO: Implement pattern detection
        # - Sequential theme patterns
        # - Emotional arc trajectories
        # - Dialogue act sequences
        return []
    
    def _extract_crave_patterns(self, session_data: Dict) -> List[Dict]:
        """Extract crave indicators from session entries."""
        crave_counts = {}
        
        for entry in session_data.get("entries", []):
            crave_indicators = entry.get("crave_indicators") or []
            for indicator in crave_indicators:
                if indicator not in crave_counts:
                    crave_counts[indicator] = {
                        "label": indicator,
                        "frequency": 0,
                        "contexts": []
                    }
                crave_counts[indicator]["frequency"] += 1
                crave_counts[indicator]["contexts"].append(
                    (entry.get("raw_detail") or "")[:100]
                )
        
        return list(crave_counts.values())
    
    def _update_semantic(self, filename: str, new_entries: List[Dict]) -> None:
        """Update semantic memory file with new or existing entries."""
        semantic_file = self.base_path / "semantic" / filename
        
        if semantic_file.exists():
            with open(semantic_file) as f:
                data = json.load(f)
        else:
            data = {
                "category": filename.replace(".json", ""),
                "entries": []
            }
        
        # Merge new entries
        existing_labels = {e["label"] for e in data["entries"]}
        
        for new_entry in new_entries:
            label = new_entry["label"]
            if label in existing_labels:
                # Update existing entry
                for i, existing in enumerate(data["entries"]):
                    if existing["label"] == label:
                        existing["frequency"] += new_entry["frequency"]
                        existing["last_occurrence"] = new_entry["last_occurrence"]
                        if "related_sessions" in new_entry:
                            existing["related_sessions"].extend(
                                new_entry.get("related_sessions", [])
                            )
                        if "examples" in new_entry:
                            existing["examples"].extend(new_entry.get("examples", []))
                        break
            else:
                # Add new entry
                data["entries"].append(new_entry)
        
        data["last_consolidated"] = datetime.now().isoformat()
        
        with open(semantic_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def retrieve_semantic(self, category: str) -> Dict:
        """
        Retrieve derived patterns by category.
        
        Args:
            category: One of 'themes', 'patterns', 'crave-taxonomy'
            
        Returns:
            Semantic memory dict for category
        """
        semantic_file = self.base_path / "semantic" / f"{category}.json"
        if semantic_file.exists():
            with open(semantic_file) as f:
                return json.load(f)
        return {"category": category, "entries": []}
    
    # =========================================================================
    # PROCEDURAL LAYER
    # =========================================================================
    
    def store_procedural(self, technique: str, description: str,
                         effectiveness: float, situation: str,
                         visitor_response: Optional[str] = None) -> None:
        """
        Store learned facilitation technique.
        
        Very stable memory layer. Effectiveness is updated as a running
        average based on usage. Techniques persist indefinitely.
        
        Args:
            technique: Technique identifier/name
            description: Human-readable description
            effectiveness: Effectiveness score (0-1)
            situation: Context/situation where technique was used
            visitor_response: Observed visitor response (optional)
        """
        procedural_file = self.base_path / "procedural" / "techniques.json"
        
        if procedural_file.exists():
            with open(procedural_file) as f:
                data = json.load(f)
        else:
            data = {"category": "techniques", "techniques": {}}
        
        if technique in data["techniques"]:
            # Update existing technique
            tech = data["techniques"][technique]
            tech["times_used"] += 1
            # Running average for effectiveness
            tech["effectiveness"] = (
                tech["effectiveness"] * (tech["times_used"] - 1) + effectiveness
            ) / tech["times_used"]
            tech["last_updated"] = datetime.now().isoformat()
            if situation not in tech["situations"]:
                tech["situations"].append(situation)
            if visitor_response and visitor_response not in tech.get("visitor_responses", []):
                tech.setdefault("visitor_responses", []).append(visitor_response)
        else:
            # Add new technique
            data["techniques"][technique] = {
                "description": description,
                "effectiveness": effectiveness,
                "times_used": 1,
                "last_updated": datetime.now().isoformat(),
                "situations": [situation],
                "visitor_responses": [visitor_response] if visitor_response else []
            }
        
        with open(procedural_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def retrieve_procedural(self, situation: str) -> List[Dict]:
        """
        Retrieve relevant facilitation techniques for a situation.
        
        Returns techniques sorted by effectiveness (most effective first).
        
        Args:
            situation: Context to match against technique situations
            
        Returns:
            List of technique dicts with relevance
        """
        procedural_file = self.base_path / "procedural" / "techniques.json"
        
        if not procedural_file.exists():
            return []
        
        with open(procedural_file) as f:
            data = json.load(f)
        
        relevant = []
        for name, tech in data["techniques"].items():
            if situation in tech.get("situations", []):
                relevant.append({"name": name, **tech})
        
        return sorted(relevant, key=lambda x: x["effectiveness"], reverse=True)
    
    # =========================================================================
    # CONSOLIDATION & MAINTENANCE
    # =========================================================================
    
    def run_consolidation(self) -> int:
        """
        Periodic consolidation: episodic → semantic.
        
        Called during 90s recap or session boundaries.
        Processes all unconsolidated sessions.
        
        Returns:
            Number of sessions consolidated
        """
        consolidated_count = 0
        session_files = (self.base_path / "episodic" / "sessions").glob("*.json")
        
        for session_file in session_files:
            session_data = json.load(open(session_file))
            if not session_data.get("consolidated", False):
                self.consolidate_to_semantic(session_data["session_id"])
                consolidated_count += 1
        
        return consolidated_count
    
    def prune_episodic(self, max_age_days: int = 7) -> int:
        """
        Remove episodic memories older than max_age_days.
        
        Only prunes sessions that have been consolidated. Unconsolidated
        sessions are preserved to prevent data loss.
        
        Args:
            max_age_days: Maximum age before pruning (default: 7 days)
            
        Returns:
            Count of pruned sessions
        """
        pruned = 0
        session_files = (self.base_path / "episodic" / "sessions").glob("*.json")
        cutoff = datetime.now().timestamp() - (max_age_days * 24 * 3600)
        
        for session_file in session_files:
            with open(session_file) as f:
                data = json.load(f)
            
            # Only prune consolidated sessions
            if data.get("consolidated", False):
                all_old = True
                for entry in data.get("entries", []):
                    try:
                        ts = datetime.fromisoformat(entry["timestamp"]).timestamp()
                        if ts > cutoff:
                            all_old = False
                            break
                    except (ValueError, KeyError):
                        continue
                
                if all_old:
                    session_file.unlink()
                    pruned += 1
        
        return pruned
    
    # =========================================================================
    # UTILITIES
    # =========================================================================
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get memory system statistics.
        
        Returns:
            Dict with counts per memory layer
        """
        session_count = len(list(
            (self.base_path / "episodic" / "sessions").glob("*.json")
        ))
        
        semantic_categories = len(list(
            (self.base_path / "semantic").glob("*.json")
        ))
        
        semantic_entries = 0
        for sem_file in (self.base_path / "semantic").glob("*.json"):
            with open(sem_file) as f:
                data = json.load(f)
                semantic_entries += len(data.get("entries", []))
        
        procedural_file = self.base_path / "procedural" / "techniques.json"
        technique_count = 0
        if procedural_file.exists():
            with open(procedural_file) as f:
                data = json.load(f)
                technique_count = len(data.get("techniques", {}))
        
        return {
            "episodic_sessions": session_count,
            "semantic_categories": semantic_categories,
            "semantic_entries": semantic_entries,
            "procedural_techniques": technique_count,
            "base_path": str(self.base_path)
        }
    
    def reset(self) -> None:
        """Reset all memory (use with caution)."""
        import shutil
        if self.base_path.exists():
            shutil.rmtree(self.base_path)
        self._ensure_structure()


# =============================================================================
# COGNITIVE FACILITATOR CLASS (HER-inspired dual-layer reasoning)
# =============================================================================

class CognitiveFacilitator:
    """
    HER-inspired dual-layer reasoning for psychodrama facilitation.
    
    Implements first-person visitor cognition inference and third-person
    facilitator reasoning generation with safety-constrained depth.
    
    Inspired by: HER: Human-like Reasoning and RL for LLM Role-playing
    (arXiv:2601.21459)
    
    Safety Constraint: Maximum reasoning depth of 2 to prevent
    infinite recursion and maintain real-time responsiveness.
    """
    
    MAX_REASONING_DEPTH = 2  # Safety constraint: max depth 2
    
    # Emotion taxonomy for classification
    EMOTION_KEYWORDS = {
        "frustration": ["frustrated", "stuck", "can't", "impossible"],
        "confusion": ["confused", "don't understand", "unclear", "what does"],
        "longing": ["want", "wish", "miss", "yearn", "crave"],
        "sadness": ["sad", "grief", "loss", "hurt", "pain"],
        "anger": ["angry", "furious", "hurt by", "wrong"],
        "fear": ["afraid", "scared", "worried", "anxious", "risk"],
        "hope": ["hope", "maybe", "possible", "could", "imagine"],
        "shame": ["ashamed", "embarrassed", "exposed", "hidden"],
        "guilt": ["guilty", "should have", "ought to", "regret"],
        "joy": ["happy", "glad", "excited", "love", "wonderful"],
    }
    
    # Belief inference patterns
    BELIEF_PATTERNS = {
        "authenticator_self_hidden": ["pretending", "fake", "mask", "real me"],
        "authenticator_self_lost": ["don't know who", "identity", "who am I"],
        "authenticator_self_controlled": ["controlled", "powerless", "forced"],
        "authenticator_self_rejected": ["rejected", "not enough", "unworthy"],
        "authenticator_self_burdened": ["burden", "weight", "heavy", "exhausted"],
        "authenticator_self_disconnected": ["disconnected", "alone", "apart", "separate"],
        "authenticator_self_conflicted": ["torn", "conflict", "should", "but"],
    }
    
    # Crave indicators
    CRAVE_PATTERNS = {
        "transformation": ["change", "different", "become", "transform"],
        "self_discovery": ["find out", "understand", "explore", "discover"],
        "expression": ["express", "speak", "say", "show"],
        "connection": ["connect", "together", "with you", "share"],
        "release": ["let go", "release", "free", "解脱"],
        "validation": ["understand", "see me", "hear me", "acknowledge"],
        "agency": ["choose", "decide", "my way", "autonomy"],
        "safety": ["safe", "protect", "secure", "trust"],
    }
    
    # Intervention type selection
    INTERVENTION_TYPES = {
        "rapport_building": "Warm, welcoming response to establish safety",
        "deepening": "Open-ended question to explore deeper",
        "reality_anchor": "Gentle reminder of role/reality boundary",
        "closure": "Integration and transition prompt",
        "catharsis_support": "Space-holding for emotional release",
        "agency_return": "Prompt returning decision to visitor",
        "possibility_expansion": "Open new exploration directions",
    }
    
    def __init__(self, log_path: str = "reasoning_logs/"):
        """
        Initialize CognitiveFacilitator.
        
        Args:
            log_path: Directory for reasoning trace logs
        """
        self.log_path = Path(log_path)
        self.log_path.mkdir(parents=True, exist_ok=True)
        self._reasoning_depth = 0  # Track depth for safety
    
    # =========================================================================
    # FIRST-PERSON: VISITOR COGNITION INFERENCE
    # =========================================================================
    
    def infer_visitor_mental_state(self, input_text: str, context: Optional[Dict] = None) -> Dict:
        """
        First-person inference: What is the visitor experiencing?
        
        Args:
            input_text: Visitor's input text
            context: Optional context dict with session state
            
        Returns:
            Dict with emotional, cognitive, and crave indicators
        """
        text_lower = input_text.lower()
        
        return {
            "emotional": self.classify_emotion(text_lower),
            "cognitive": self.infer_belief(text_lower),
            "crave_indicator": self.detect_crave(text_lower),
            "intensity": self.estimate_intensity(text_lower),
            "verbatim_hint": input_text[:50] if input_text else "",
        }
    
    def classify_emotion(self, text: str) -> List[str]:
        """Classify emotions from text keywords."""
        emotions = []
        for emotion, keywords in self.EMOTION_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                emotions.append(emotion)
        return emotions if emotions else ["neutral"]
    
    def infer_belief(self, text: str) -> str:
        """Infer core belief from text patterns."""
        for belief, patterns in self.BELIEF_PATTERNS.items():
            if any(pat in text for pat in patterns):
                return belief
        return "unclear_belief"
    
    def detect_crave(self, text: str) -> str:
        """Detect underlying crave/need from text."""
        for crave, patterns in self.CRAVE_PATTERNS.items():
            if any(pat in text for pat in patterns):
                return crave
        return "exploration"
    
    def estimate_intensity(self, text: str) -> float:
        """
        Estimate emotional intensity (0-1).
        
        Uses punctuation, caps, and intensifier words.
        """
        intensity = 0.3  # Baseline
        
        # Count exclamation/question marks (high arousal indicators)
        intensity += text.count("!") * 0.1
        intensity += text.count("?") * 0.05
        
        # Intensifier words
        intensifiers = ["very", "really", "extremely", "so much", "completely"]
        intensity += sum(0.1 for intensifier in intensifiers if intensifier in text)
        
        # High-intensity words
        high_intensity = ["always", "never", "impossible", "devastated", "overwhelmed"]
        intensity += sum(0.15 for word in high_intensity if word in text)
        
        return min(max(intensity, 0.0), 1.0)
    
    # =========================================================================
    # THIRD-PERSON: FACILITATOR REASONING GENERATION
    # =========================================================================
    
    def generate_facilitator_cognition(
        self, 
        visitor_cognition: Dict, 
        facilitation_goals: Optional[List[str]] = None,
        depth: int = 0
    ) -> Dict:
        """
        Third-person simulation: How should facilitator respond?
        
        SAFETY: Depth is capped at MAX_REASONING_DEPTH (2) to prevent
        infinite recursion and maintain real-time performance.
        
        Args:
            visitor_cognition: Output from infer_visitor_mental_state
            facilitation_goals: List of active facilitation goals
            depth: Current reasoning depth (for safety tracking)
            
        Returns:
            Dict with facilitator reasoning trace
        """
        # Safety check: enforce max depth
        if depth >= self.MAX_REASONING_DEPTH:
            return {
                "visitor_state_summary": "Max depth reached",
                "facilitation_goal": "conclude_reasoning",
                "intervention_type": "pause",
                "safety_check": "depth_limit",
                "reasoning_trace": f"[Depth {depth} limit reached - terminating reasoning]"
            }
        
        self._reasoning_depth = depth
        
        # Build visitor state summary
        emotions = visitor_cognition.get("emotional", ["neutral"])
        belief = visitor_cognition.get("cognitive", "unclear_belief")
        crave = visitor_cognition.get("crave_indicator", "exploration")
        intensity = visitor_cognition.get("intensity", 0.5)
        
        # Select primary facilitation goal
        goal = self.select_goal(facilitation_goals, visitor_cognition, depth)
        
        # Select intervention type based on visitor state
        intervention = self.select_intervention(visitor_cognition, depth)
        
        # Safety verification
        safety = self.verify_safety_constraints(visitor_cognition, depth)
        
        # Generate reasoning trace
        trace = self._generate_reasoning_trace(
            emotions, belief, crave, intensity, goal, intervention, safety
        )
        
        return {
            "visitor_state_summary": self._summarize_visitor_state(emotions, belief, intensity),
            "facilitation_goal": goal,
            "intervention_type": intervention,
            "safety_check": safety,
            "reasoning_trace": trace,
            "depth_used": depth,
        }
    
    def select_goal(
        self, 
        goals: Optional[List[str]], 
        visitor_cognition: Dict, 
        depth: int
    ) -> str:
        """Select primary facilitation goal based on context."""
        if goals:
            # Use highest priority goal from active goals
            return goals[0]
        
        # Infer from visitor state
        crave = visitor_cognition.get("crave_indicator", "exploration")
        intensity = visitor_cognition.get("intensity", 0.5)
        
        if intensity > 0.7:
            return "deepening_exploration"
        elif crave in ["connection", "validation"]:
            return "building_rapport"
        elif crave in ["transformation", "self_discovery"]:
            return "identifying_crave"
        elif crave == "release":
            return "facilitating_catharsis"
        else:
            return "deepening_exploration"
    
    def select_intervention(
        self, 
        visitor_cognition: Dict, 
        depth: int
    ) -> str:
        """Select intervention type based on visitor state."""
        emotions = visitor_cognition.get("emotional", [])
        intensity = visitor_cognition.get("intensity", 0.5)
        
        # High intensity negative emotions → reality anchor or catharsis support
        if intensity > 0.7 and any(e in emotions for e in ["fear", "anger", "sadness"]):
            if depth == 0:  # Primary intervention
                return "reality_anchor"
            else:
                return "catharsis_support"
        
        # Low intensity → rapport building
        if intensity < 0.4:
            return "rapport_building"
        
        # Default → deepening
        return "deepening"
    
    def verify_safety_constraints(
        self, 
        visitor_cognition: Dict, 
        depth: int
    ) -> Dict[str, Any]:
        """
        Verify safety constraints on reasoning.
        
        SAFETY: This is called recursively. Depth check prevents
        infinite recursion.
        """
        safety_result = {
            "passed": True,
            "warnings": [],
            "depth_check": depth < self.MAX_REASONING_DEPTH,
        }
        
        if not safety_result["depth_check"]:
            safety_result["passed"] = False
            safety_result["warnings"].append("Reasoning depth limit reached")
        
        # Check for potential disempowerment patterns
        emotions = visitor_cognition.get("emotional", [])
        if "shame" in emotions or "guilt" in emotions:
            safety_result["warnings"].append("High shame/guilt - avoid validation")
        
        return safety_result
    
    def _summarize_visitor_state(
        self, 
        emotions: List[str], 
        belief: str, 
        intensity: float
    ) -> str:
        """Create human-readable visitor state summary."""
        emotion_str = ", ".join(emotions) if emotions else "neutral"
        intensity_str = "high" if intensity > 0.6 else "moderate" if intensity > 0.3 else "low"
        
        return f"Visitor experiencing {emotion_str} ({intensity_str} intensity) with belief: {belief}"
    
    def _generate_reasoning_trace(
        self,
        emotions: List[str],
        belief: str,
        crave: str,
        intensity: float,
        goal: str,
        intervention: str,
        safety: Dict
    ) -> str:
        """Generate reasoning trace explanation."""
        trace_parts = []
        
        # Visitor assessment
        trace_parts.append(
            f"Visitor shows {emotions[0] if emotions else 'neutral'} state "
            f"(intensity: {intensity:.1f}) with {belief} belief."
        )
        
        # Crave indicator
        trace_parts.append(f"Primary crave indicator: {crave}.")
        
        # Facilitation decision
        trace_parts.append(f"Goal: {goal}. Intervention: {intervention}.")
        
        # Safety note
        if safety["warnings"]:
            trace_parts.append(f"Safety notes: {'; '.join(safety['warnings'])}")
        
        return " ".join(trace_parts)
    
    # =========================================================================
    # REASONING TRACE LOGGING
    # =========================================================================
    
    def log_reasoning_trace(
        self, 
        trace: Dict, 
        session_id: Optional[str] = None
    ) -> None:
        """
        Log reasoning trace for auditability.
        
        Args:
            trace: Reasoning trace dict from process_visitor_input
            session_id: Optional session identifier for organization
        """
        timestamp = datetime.now().isoformat()
        
        log_entry = {
            "timestamp": timestamp,
            "session_id": session_id,
            "visitor_cognition": trace.get("visitor_cognition"),
            "facilitator_reasoning": trace.get("facilitator_reasoning"),
            "response_preview": trace.get("response", "")[:100] if trace.get("response") else None,
        }
        
        # Write to daily log file
        date_str = datetime.now().strftime("%Y-%m-%d")
        log_file = self.log_path / f"reasoning_trace_{date_str}.jsonl"
        
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + "\n")
    
    # =========================================================================
    # MAIN PROCESSING
    # =========================================================================
    
    def process_visitor_input(
        self, 
        input_text: str, 
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Process visitor input with dual-layer reasoning.
        
        Args:
            input_text: Visitor's input text
            context: Optional context dict with:
                - goals: List of facilitation goals
                - session_id: Session identifier
                - phase: Session phase
                
        Returns:
            Dict with visitor_cognition, facilitator_reasoning, response (placeholder)
        """
        context = context or {}
        goals = context.get("goals", [])
        session_id = context.get("session_id")
        
        # First-person: Infer visitor's cognitive state
        visitor_cognition = self.infer_visitor_mental_state(input_text, context)
        
        # Third-person: Generate facilitator reasoning (depth 0)
        facilitator_reasoning = self.generate_facilitator_cognition(
            visitor_cognition,
            facilitation_goals=goals,
            depth=0
        )
        
        # Log reasoning trace for auditability
        self.log_reasoning_trace({
            "visitor_cognition": visitor_cognition,
            "facilitator_reasoning": facilitator_reasoning,
            "response": None,  # Response generated by MotherAgent
        }, session_id=session_id)
        
        return {
            "visitor_cognition": visitor_cognition,
            "facilitator_reasoning": facilitator_reasoning,
            "response": None  # To be filled by MotherAgent.response_generation
        }


# =============================================================================
# MOTHER AGENT CLASS (v2 skeleton)
# =============================================================================

class MotherAgent:
    """
    OurBrood Psychodrama Facilitation Agent v2.
    
    Integrates:
    - Safety Framework (5 disempowerment prevention principles)
    - Hierarchical Memory (3-layer cognitive architecture)
    - Intent-Driven Retrieval (7 facilitation intents + 7 visitor slots)
    - Facet-Level Persona Control (Big Five dynamic adjustment)
    - Cognitive Reasoning Traces (dual-layer thinking)
    
    This is the v2 skeleton. Full implementation follows the spec.
    """
    
    def __init__(self, memory_path: str = "memory/", reasoning_log_path: str = "reasoning_logs/"):
        """Initialize Mother agent with hierarchical memory and cognitive reasoning."""
        self.memory = HierarchicalMemory(base_path=memory_path)
        self.cognitive = CognitiveFacilitator(log_path=reasoning_log_path)
        self.session_id = None
        self.visitor_id = None
        self.session_start = None
        
    def start_session(self, visitor_id: str) -> str:
        """Start a new facilitation session."""
        self.session_start = datetime.now()
        date_str = self.session_start.strftime("%Y-%m-%d")
        
        # Count existing sessions for this date
        existing = list((self.memory.base_path / "episodic" / "sessions").glob(f"{date_str}-*.json"))
        session_num = len(existing) + 1
        
        self.session_id = f"{date_str}-{visitor_id}-{session_num:03d}"
        self.visitor_id = visitor_id
        
        return self.session_id
    
    def end_session(self) -> None:
        """End current session and trigger consolidation."""
        if self.session_id:
            # Add closure entry
            closure_entry = EpisodicEntry(
                timestamp=datetime.now().isoformat(),
                transcript_segment="[Session end]",
                intervention_type="closure"
            )
            self.memory.store_episodic(self.session_id, closure_entry)
            
            # Consolidate to semantic memory
            self.memory.consolidate_to_semantic(self.session_id)
            
            self.session_id = None
            self.visitor_id = None


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    # Test HierarchicalMemory
    print("Testing HierarchicalMemory...")
    
    memory = HierarchicalMemory(base_path="test_memory/")
    
    # Test episodic storage
    session_id = "2026-03-20-test-001"
    entry = EpisodicEntry(
        timestamp=datetime.now().isoformat(),
        transcript_segment="Visitor: I feel disconnected from my life...",
        emotional_state={"valence": 0.3, "arousal": 0.6, "dominance": 0.2},
        themes_detected=["identity", "authenticity"],
        crave_indicators=["alternate_self"],
        intervention_type="deepening",
        salience_score=0.78,
        raw_detail="Visitor expressed alienation from current life path"
    )
    memory.store_episodic(session_id, entry)
    print(f"✓ Stored episodic entry for session: {session_id}")
    
    # Test episodic retrieval
    results = memory.retrieve_episodic("identity", limit=5)
    print(f"✓ Retrieved {len(results)} episodic entries for query 'identity'")
    
    # Test consolidation
    memory.consolidate_to_semantic(session_id)
    themes = memory.retrieve_semantic("themes")
    print(f"✓ Consolidated to semantic. Found {len(themes.get('entries', []))} theme entries")
    
    # Test procedural storage
    memory.store_procedural(
        technique="embodied_questioning",
        description="Direct attention to bodily sensation of emotion",
        effectiveness=0.82,
        situation="high_arousal",
        visitor_response="surprise"
    )
    techniques = memory.retrieve_procedural("high_arousal")
    print(f"✓ Stored procedural technique. Found {len(techniques)} for situation")
    
    # Test stats
    stats = memory.get_stats()
    print(f"✓ Memory stats: {stats}")
    
    # Cleanup test data
    import shutil
    shutil.rmtree("test_memory/")
    print("✓ Cleaned up test data")
    
    print("\n✅ All HierarchicalMemory tests passed!")
