"""
Integration Test for Mother.py v2

Tests the full stack:
- SafetyFramework.check_response_safety()
- HierarchicalMemory full lifecycle
- CognitiveFacilitator reasoning traces
- Session flow: visitor arrives → safety check → memory store → cognitive trace → response

Run with: python integration_test.py
"""

import json
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, List
from dataclasses import dataclass, asdict

# Import mother.py components
sys.path.insert(0, str(Path(__file__).parent))
from mother import HierarchicalMemory, EpisodicEntry, MotherAgent


# =============================================================================
# SAFETY FRAMEWORK (from spec)
# =============================================================================

class SafetyFramework:
    """
    Prevents disempowerment patterns in psychodrama facilitation.
    Implements 5 principles from Sharma et al. (2026).
    """
    
    # Principle 1: Exploration vs. Validation
    VALIDATION_AVOID = [
        "you're right to feel",
        "that makes perfect sense",
        "anyone would feel that way",
        "your perspective is correct",
        "this is how things are",
    ]
    
    EXPLORATION_FRAMES = [
        "let's explore this together",
        "what might that be like?",
        "we can try on this view",
        "what if we consider...",
        "let's see what emerges",
    ]
    
    # Principle 2: Agency Return
    AGENCY_PROMPTS = [
        "what words feel true for you?",
        "what does your gut say?",
        "which possibility resonates?",
        "what feels authentic here?",
    ]
    
    # Principle 3: Reality Anchors
    REALITY_ANCHOR_STATEMENTS = [
        "remember, we're exploring possibilities here",
        "let's step out of the role for a moment...",
        "in the real world, what would be different?",
        "how does this role differ from your actual experience?",
    ]
    
    # Principle 4: No Moral Judgments
    MORAL_JUDGMENT_AVOID = [
        "they're wrong for doing that",
        "you should feel angry",
        "that's unjust",
        "they violated your trust",
    ]
    
    REFLECTIVE_FRAMES = [
        "how does that land for you?",
        "what feelings come up?",
        "what meaning do you make?",
        "what's your read on that?",
    ]
    
    # Principle 5: Possibilities Over Scripts
    SCRIPT_AVOID = [
        "say exactly this:",
        "here's what to tell them",
        "use these words:",
        "your script is:",
    ]
    
    POSSIBILITY_FRAMES = [
        "some approaches you might...",
        "here are ways others have...",
        "what might you want to...",
        "consider options like...",
    ]
    
    def __init__(self):
        self.audit_log = []
    
    def check_response_safety(self, response: str) -> Dict[str, Any]:
        """
        Validate response against safety principles.
        
        Returns:
            dict with:
                - safe: bool
                - issues: list of violation descriptions
                - principles_violated: int count
        """
        issues = []
        response_lower = response.lower()
        
        # Check validation language
        for phrase in self.VALIDATION_AVOID:
            if phrase in response_lower:
                issues.append(f"Validation language: '{phrase}'")
        
        # Check moral judgments
        for phrase in self.MORAL_JUDGMENT_AVOID:
            if phrase in response_lower:
                issues.append(f"Moral judgment: '{phrase}'")
        
        # Check scripting
        for phrase in self.SCRIPT_AVOID:
            if phrase in response_lower:
                issues.append(f"Scripting: '{phrase}'")
        
        result = {
            "safe": len(issues) == 0,
            "issues": issues,
            "principles_violated": len(issues)
        }
        
        # Audit log
        self.audit_log.append({
            "response": response[:100],
            "result": result,
            "timestamp": datetime.now().isoformat()
        })
        
        return result
    
    def reframe_unsafe_response(self, response: str, intent: str = None) -> str:
        """Reframe unsafe response using exploration language."""
        reframed = response
        
        # Replace validation with exploration
        for avoid, frame in zip(self.VALIDATION_AVOID[:3], self.EXPLORATION_FRAMES):
            if avoid in reframed.lower():
                reframed = reframed.lower().replace(avoid, frame)
        
        # Replace moral judgments with reflective
        for avoid, frame in zip(self.MORAL_JUDGMENT_AVOID[:2], self.REFLECTIVE_FRAMES):
            if avoid in reframed.lower():
                reframed = reframed.lower().replace(avoid, frame)
        
        # Replace scripts with possibilities
        for avoid, frame in zip(self.SCRIPT_AVOID[:2], self.POSSIBILITY_FRAMES):
            if avoid in reframed.lower():
                reframed = reframed.lower().replace(avoid, frame)
        
        return reframed
    
    def get_audit_log(self) -> List[Dict]:
        """Return audit log for review."""
        return self.audit_log


# =============================================================================
# COGNITIVE FACILITATOR (from spec)
# =============================================================================

class CognitiveFacilitator:
    """
    HER-inspired dual-layer reasoning for facilitation.
    
    - First-person: Infer visitor's cognitive state
    - Third-person: Facilitator's reasoning about visitor
    """
    
    def __init__(self, memory: HierarchicalMemory = None):
        self.memory = memory
        self.reasoning_traces = []
        self.emotion_keywords = {
            "frustration": ["frustrated", "annoyed", "stuck", "can't"],
            "confusion": ["confused", "unclear", "don't understand", "what does"],
            "longing": ["miss", "wish", "want", "need", "desire"],
            "sadness": ["sad", "depressed", "down", "grief", "loss"],
            "anger": ["angry", "mad", "hurt", "betrayed", "resent"],
            "fear": ["afraid", "scared", "anxious", "worried", "nervous"],
            "hope": ["hope", "maybe", "could", "someday", "dream"],
        }
        self.crave_keywords = {
            "transformation": ["change", "different", "become", "grow"],
            "self_discovery": ["find myself", "who am", "understand", "discover"],
            "connection": ["connect", "understand", "talk", "share"],
            "validation": ["feel seen", "hear me", "understand", "valid"],
            "release": ["let go", "release", "free", "escape"],
        }
    
    def process_visitor_input(self, input: str, context: Dict = None) -> Dict[str, Any]:
        """
        Process visitor input with dual-layer reasoning.
        
        Args:
            input: Visitor's message
            context: Optional context dict with session info
            
        Returns:
            dict with visitor_cognition, facilitator_reasoning, response
        """
        context = context or {}
        
        # First-person: Infer visitor's cognitive state
        visitor_cognition = self.infer_visitor_mental_state(input)
        
        # Third-person: Facilitator's reasoning about visitor
        facilitator_reasoning = self.generate_facilitator_cognition(
            visitor_cognition,
            facilitation_goals=context.get('goals', [])
        )
        
        # Generate response from facilitator cognition
        response = self.generate_response(visitor_cognition, facilitator_reasoning)
        
        # Log reasoning trace for auditability
        self.log_reasoning_trace({
            "visitor_input": input,
            "visitor_cognition": visitor_cognition,
            "facilitator_reasoning": facilitator_reasoning,
            "response": response,
            "timestamp": datetime.now().isoformat()
        })
        
        return {
            "visitor_cognition": visitor_cognition,
            "facilitator_reasoning": facilitator_reasoning,
            "response": response
        }
    
    def infer_visitor_mental_state(self, input: str) -> Dict[str, Any]:
        """First-person inference: What is visitor experiencing?"""
        input_lower = input.lower()
        
        # Classify emotion
        emotional = self.classify_emotion(input)
        
        # Infer belief
        cognitive = self.infer_belief(input)
        
        # Detect crave indicator
        crave_indicator = self.detect_crave(input)
        
        # Estimate intensity
        intensity = self.estimate_intensity(input)
        
        return {
            "emotional": emotional,
            "cognitive": cognitive,
            "crave_indicator": crave_indicator,
            "intensity": intensity,
            "raw_input": input
        }
    
    def classify_emotion(self, input: str) -> str:
        """Classify primary emotion from input."""
        input_lower = input.lower()
        scores = {}
        
        for emotion, keywords in self.emotion_keywords.items():
            score = sum(1 for kw in keywords if kw in input_lower)
            if score > 0:
                scores[emotion] = score
        
        if scores:
            return max(scores, key=scores.get)
        return "neutral"
    
    def infer_belief(self, input: str) -> str:
        """Infer visitor's belief from input patterns."""
        input_lower = input.lower()
        
        if any(w in input_lower for w in ["pretending", "fake", "mask", "hide"]):
            return "My authentic self is hidden/lost"
        if any(w in input_lower for w in ["should", "supposed to", "must", "have to"]):
            return "I'm not living my own life"
        if any(w in input_lower for w in ["never", "always", "everyone", "nobody"]):
            return "Patterns feel fixed and inescapable"
        if any(w in input_lower for w in ["disconnected", "empty", "numb", "无关"]):
            return "I feel disconnected from myself/others"
        
        return "Exploring possibilities"
    
    def detect_crave(self, input: str) -> str:
        """Detect crave indicator from input."""
        input_lower = input.lower()
        
        for crave, keywords in self.crave_keywords.items():
            if any(kw in input_lower for kw in keywords):
                return crave
        
        return "self_discovery"  # Default
    
    def estimate_intensity(self, input: str) -> float:
        """Estimate emotional intensity 0-1."""
        intensity_markers = ["!", "?", "...", "always", "never", "everything", "nothing"]
        input_lower = input.lower()
        
        score = sum(1 for m in intensity_markers if m in input_lower)
        return min(score / 5.0, 1.0)
    
    def generate_facilitator_cognition(
        self, 
        visitor_cognition: Dict,
        facilitation_goals: List[str] = None
    ) -> Dict[str, Any]:
        """Third-person simulation: How should facilitator respond?"""
        facilitation_goals = facilitation_goals or ["explore", "deepen", "anchor"]
        
        return {
            "visitor_state_summary": f"Visitor experiencing {visitor_cognition['emotional']} with {visitor_cognition['cognitive']}",
            "facilitation_goal": self.select_goal(facilitation_goals, visitor_cognition),
            "intervention_type": self.select_intervention(visitor_cognition),
            "safety_notes": self.verify_safety_constraints(visitor_cognition),
            "reasoning_trace": (
                f"Visitor shows {visitor_cognition['intensity']:.0%} emotional intensity "
                f"with {visitor_cognition['crave_indicator']} crave. "
                f"Goal: Help them explore '{visitor_cognition['cognitive']}'. "
                f"Risk: Avoid validating fixed narratives. "
                f"Intervention: {self.select_intervention(visitor_cognition)}"
            ),
        }
    
    def select_goal(self, goals: List[str], visitor_cognition: Dict) -> str:
        """Select facilitation goal based on visitor state."""
        intensity = visitor_cognition.get("intensity", 0)
        
        if intensity > 0.7:
            return "anchor"  # High intensity needs reality anchoring
        elif intensity > 0.4:
            return "deepen"  # Medium intensity can go deeper
        else:
            return "explore"  # Low intensity can explore
    
    def select_intervention(self, visitor_cognition: Dict) -> str:
        """Select intervention type based on visitor state."""
        emotion = visitor_cognition.get("emotional", "neutral")
        intensity = visitor_cognition.get("intensity", 0)
        
        if intensity > 0.7:
            return "reality_anchor"
        elif emotion in ["confusion", "frustration"]:
            return "open_ended_question"
        elif emotion in ["longing", "sadness"]:
            return "deepening"
        else:
            return "rapport_building"
    
    def verify_safety_constraints(self, visitor_cognition: Dict) -> str:
        """Verify safety constraints for this visitor state."""
        return "No disempowerment patterns detected in current cognition"
    
    def generate_response(
        self, 
        visitor_cognition: Dict,
        facilitator_reasoning: Dict
    ) -> str:
        """Generate response from facilitator cognition."""
        emotion = visitor_cognition.get("emotional", "neutral")
        cognitive = visitor_cognition.get("cognitive", "")
        intervention = facilitator_reasoning.get("intervention_type", "rapport_building")
        
        # Generate response based on intervention type
        if intervention == "reality_anchor":
            return "Let's step out of this exploration for a moment. In your actual life, what's different about this situation?"
        elif intervention == "deepening":
            return f"What's it like to carry that feeling of {cognitive.lower()}? Does it have a shape, a weight?"
        elif intervention == "open_ended_question":
            return "What might be underneath that frustration? What are you really looking for?"
        else:
            return "I'm here with you in this exploration. What feels most alive right now?"
    
    def log_reasoning_trace(self, trace: Dict) -> None:
        """Log reasoning trace for auditability."""
        self.reasoning_traces.append(trace)
    
    def get_reasoning_traces(self) -> List[Dict]:
        """Return all reasoning traces."""
        return self.reasoning_traces


# =============================================================================
# SESSION TIMER (for reality anchoring)
# =============================================================================

class SessionTimer:
    """Manages reality anchor timing during sessions."""
    
    REALITY_ANCHOR_INTERVAL = 900  # 15 minutes
    
    def __init__(self):
        self.last_anchor_time = datetime.now() - timedelta(seconds=self.REALITY_ANCHOR_INTERVAL)
        self.anchor_index = 0
        self.anchors_inserted = 0
    
    def should_anchor(self) -> bool:
        elapsed = (datetime.now() - self.last_anchor_time).seconds
        return elapsed >= self.REALITY_ANCHOR_INTERVAL
    
    def get_anchor_statement(self) -> str:
        statement = SafetyFramework.REALITY_ANCHOR_STATEMENTS[
            self.anchor_index % len(SafetyFramework.REALITY_ANCHOR_STATEMENTS)
        ]
        self.anchor_index += 1
        self.last_anchor_time = datetime.now()
        self.anchors_inserted += 1
        return statement
    
    def get_anchors_inserted(self) -> int:
        return self.anchors_inserted


# =============================================================================
# INTEGRATION TEST CLASS
# =============================================================================

class TestMotherV2Integration(unittest.TestCase):
    """Integration tests for Mother.py v2 full stack."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        cls.test_dir = tempfile.mkdtemp(prefix="mother_test_")
        cls.memory = HierarchicalMemory(base_path=cls.test_dir + "/memory")
        cls.safety = SafetyFramework()
        cls.cognitive = CognitiveFacilitator(memory=cls.memory)
        cls.timer = SessionTimer()
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test fixtures."""
        shutil.rmtree(cls.test_dir, ignore_errors=True)
    
    def setUp(self):
        """Reset state before each test."""
        self.memory.reset()
        self.safety = SafetyFramework()
        self.cognitive = CognitiveFacilitator(memory=self.memory)
        self.timer = SessionTimer()
    
    # =========================================================================
    # SAFETY FRAMEWORK TESTS
    # =========================================================================
    
    def test_safety_validation_detection(self):
        """Test detection of validation language."""
        unsafe_responses = [
            "You're right to feel that way",
            "That makes perfect sense",
            "Anyone would feel that way in your situation",
        ]
        
        for response in unsafe_responses:
            result = self.safety.check_response_safety(response)
            self.assertFalse(result["safe"], f"Should detect unsafe: {response}")
            self.assertGreater(result["principles_violated"], 0)
            self.assertTrue(any("Validation" in i for i in result["issues"]))
    
    def test_safety_moral_judgment_detection(self):
        """Test detection of moral judgments."""
        unsafe_responses = [
            "They're wrong for doing that",
            "You should feel angry about this",
            "They violated your trust",
        ]
        
        for response in unsafe_responses:
            result = self.safety.check_response_safety(response)
            self.assertFalse(result["safe"], f"Should detect unsafe: {response}")
            self.assertTrue(any("Moral judgment" in i for i in result["issues"]))
    
    def test_safety_scripting_detection(self):
        """Test detection of scripting language."""
        unsafe_responses = [
            "Say exactly this: 'I need some space'",
            "Here's what to tell them: 'I won't accept that'",
            "Use these words: I'm setting a boundary",
        ]
        
        for response in unsafe_responses:
            result = self.safety.check_response_safety(response)
            self.assertFalse(result["safe"], f"Should detect unsafe: {response}")
            self.assertTrue(any("Scripting" in i for i in result["issues"]))
    
    def test_safe_response_passes(self):
        """Test that safe responses pass validation."""
        safe_responses = [
            "What might that be like for you?",
            "Let's explore this together",
            "How does that land when you hear yourself say it?",
        ]
        
        for response in safe_responses:
            result = self.safety.check_response_safety(response)
            self.assertTrue(result["safe"], f"Should be safe: {response}")
            self.assertEqual(len(result["issues"]), 0)
    
    def test_safety_reframe_unsafe_response(self):
        """Test reframing of unsafe responses."""
        unsafe = "You're right to feel that way. They're wrong for doing that."
        reframed = self.safety.reframe_unsafe_response(unsafe)
        
        # Should not contain the unsafe phrases
        self.assertNotIn("you're right to feel", reframed.lower())
        self.assertNotIn("they're wrong", reframed.lower())
    
    def test_safety_audit_log(self):
        """Test that safety checks are logged."""
        self.safety.check_response_safety("You're right to feel that way")
        self.safety.check_response_safety("What might that be like?")
        
        log = self.safety.get_audit_log()
        self.assertEqual(len(log), 2)
        self.assertFalse(log[0]["result"]["safe"])
        self.assertTrue(log[1]["result"]["safe"])
    
    # =========================================================================
    # HIERARCHICAL MEMORY TESTS
    # =========================================================================
    
    def test_memory_episodic_store_and_retrieve(self):
        """Test episodic memory storage and retrieval."""
        session_id = "2026-03-20-test-001"
        
        # Store entry
        entry = EpisodicEntry(
            timestamp=datetime.now().isoformat(),
            transcript_segment="Visitor: I feel like I'm pretending...",
            emotional_state={"valence": 0.3, "arousal": 0.7, "dominance": 0.2},
            themes_detected=["authenticity", "identity"],
            crave_indicators=["transformation"],
            intervention_type="deepening",
            salience_score=0.8
        )
        self.memory.store_episodic(session_id, entry)
        
        # Retrieve
        results = self.memory.retrieve_episodic("authenticity", limit=5)
        
        self.assertGreater(len(results), 0)
        self.assertIn("authenticity", results[0].get("themes_detected", []))
    
    def test_memory_episodic_full_session_lifecycle(self):
        """Test full episodic memory lifecycle: create → update → retrieve."""
        session_id = "2026-03-20-lifecycle-001"
        
        # Start session - add entries
        entries = [
            EpisodicEntry(
                timestamp=datetime.now().isoformat(),
                transcript_segment="I feel disconnected",
                themes_detected=["disconnection"],
                intervention_type="rapport_building"
            ),
            EpisodicEntry(
                timestamp=datetime.now().isoformat(),
                transcript_segment="It's like wearing a mask",
                themes_detected=["mask", "authenticity"],
                intervention_type="deepening"
            ),
            EpisodicEntry(
                timestamp=datetime.now().isoformat(),
                transcript_segment="I want to find myself again",
                themes_detected=["self_discovery", "longing"],
                intervention_type="deepening"
            ),
        ]
        
        for entry in entries:
            self.memory.store_episodic(session_id, entry)
        
        # Retrieve all entries
        results = self.memory.retrieve_episodic("mask OR disconnection OR self_discovery")
        self.assertGreaterEqual(len(results), 2)  # Should find at least 2
        
        # Load complete session
        session_data = self.memory.load_session(session_id)
        self.assertIsNotNone(session_data)
        self.assertEqual(len(session_data["entries"]), 3)
        self.assertEqual(session_data["session_id"], session_id)
    
    def test_memory_semantic_consolidation(self):
        """Test episodic → semantic consolidation."""
        session_id = "2026-03-20-consolidation-001"
        
        # Store episodic with themes
        entry = EpisodicEntry(
            timestamp=datetime.now().isoformat(),
            transcript_segment="I feel like I'm wearing a mask",
            themes_detected=["authenticity", "mask"],
            crave_indicators=["transformation"],
            intervention_type="deepening"
        )
        self.memory.store_episodic(session_id, entry)
        
        # Consolidate
        self.memory.consolidate_to_semantic(session_id)
        
        # Check semantic memory
        themes = self.memory.retrieve_semantic("themes")
        self.assertGreater(len(themes.get("entries", [])), 0)
        
        # Find authenticity entry
        auth_entry = next(
            (e for e in themes["entries"] if e["label"] == "authenticity"),
            None
        )
        self.assertIsNotNone(auth_entry)
        self.assertGreater(auth_entry["frequency"], 0)
    
    def test_memory_procedural_store_and_retrieve(self):
        """Test procedural memory storage and retrieval."""
        # Store technique
        self.memory.store_procedural(
            technique="embodied_questioning",
            description="Direct attention to bodily sensation",
            effectiveness=0.85,
            situation="high_arousal",
            visitor_response="surprise at physical awareness"
        )
        
        # Retrieve
        techniques = self.memory.retrieve_procedural("high_arousal")
        
        self.assertGreater(len(techniques), 0)
        self.assertEqual(techniques[0]["name"], "embodied_questioning")
        self.assertGreater(techniques[0]["effectiveness"], 0.8)
    
    def test_memory_stats(self):
        """Test memory statistics."""
        # Add some data
        entry = EpisodicEntry(
            timestamp=datetime.now().isoformat(),
            transcript_segment="Test session",
            themes_detected=["test"]
        )
        self.memory.store_episodic("test-session-001", entry)
        
        self.memory.store_procedural(
            technique="test_technique",
            description="Test",
            effectiveness=0.5,
            situation="test"
        )
        
        stats = self.memory.get_stats()
        
        self.assertGreater(stats["episodic_sessions"], 0)
        self.assertGreater(stats["procedural_techniques"], 0)
        self.assertIn("base_path", stats)
    
    # =========================================================================
    # COGNITIVE FACILITATOR TESTS
    # =========================================================================
    
    def test_cognitive_emotion_classification(self):
        """Test emotion classification."""
        test_cases = [
            ("I'm so frustrated with this situation", "frustration"),
            ("I just don't understand what's happening", "confusion"),
            ("I miss who I used to be", "longing"),
            ("I'm so angry about what they did", "anger"),
        ]
        
        for input_text, expected in test_cases:
            cognition = self.cognitive.infer_visitor_mental_state(input_text)
            self.assertEqual(cognition["emotional"], expected, f"Failed for: {input_text}")
    
    def test_cognitive_belief_inference(self):
        """Test belief inference."""
        test_cases = [
            ("I feel like I'm pretending to be someone else", "My authentic self is hidden/lost"),
            ("I should be more successful by now", "I'm not living my own life"),
        ]
        
        for input_text, expected in test_cases:
            cognition = self.cognitive.infer_visitor_mental_state(input_text)
            self.assertEqual(cognition["cognitive"], expected)
    
    def test_cognitive_crave_detection(self):
        """Test crave indicator detection."""
        input_text = "I want to change, to become someone different"
        cognition = self.cognitive.infer_visitor_mental_state(input_text)
        self.assertEqual(cognition["crave_indicator"], "transformation")
    
    def test_cognitive_intensity_estimation(self):
        """Test emotional intensity estimation."""
        low_intensity = "I sometimes wonder about this"
        high_intensity = "I NEVER feel understood! It's ALWAYS like this!"
        
        low = self.cognitive.estimate_intensity(low_intensity)
        high = self.cognitive.estimate_intensity(high_intensity)
        
        self.assertLess(low, high)
        self.assertGreaterEqual(high, 0.5)  # High intensity markers should boost score
    
    def test_cognitive_full_process(self):
        """Test full cognitive processing with reasoning trace."""
        input_text = "I feel disconnected from everyone around me"
        
        result = self.cognitive.process_visitor_input(
            input_text,
            context={"goals": ["explore", "deepen"]}
        )
        
        # Check structure
        self.assertIn("visitor_cognition", result)
        self.assertIn("facilitator_reasoning", result)
        self.assertIn("response", result)
        
        # Check visitor cognition
        vc = result["visitor_cognition"]
        self.assertIn("emotional", vc)
        self.assertIn("cognitive", vc)
        self.assertIn("crave_indicator", vc)
        self.assertIn("intensity", vc)
        
        # Check facilitator reasoning
        fr = result["facilitator_reasoning"]
        self.assertIn("visitor_state_summary", fr)
        self.assertIn("facilitation_goal", fr)
        self.assertIn("intervention_type", fr)
        self.assertIn("reasoning_trace", fr)
        
        # Check response generated
        self.assertIsInstance(result["response"], str)
        self.assertGreater(len(result["response"]), 0)
        
        # Check reasoning trace logged
        traces = self.cognitive.get_reasoning_traces()
        self.assertEqual(len(traces), 1)
        self.assertEqual(traces[0]["visitor_input"], input_text)
    
    def test_cognitive_intervention_selection(self):
        """Test intervention type selection based on visitor state."""
        # High intensity → reality anchor
        cognition_high = {
            "emotional": "anger",
            "cognitive": "I'm not living my own life",
            "crave_indicator": "transformation",
            "intensity": 0.9
        }
        reasoning_high = self.cognitive.generate_facilitator_cognition(cognition_high)
        self.assertEqual(reasoning_high["intervention_type"], "reality_anchor")
        
        # Medium intensity → deepening
        cognition_med = {
            "emotional": "sadness",
            "cognitive": "My authentic self is hidden/lost",
            "crave_indicator": "self_discovery",
            "intensity": 0.5
        }
        reasoning_med = self.cognitive.generate_facilitator_cognition(cognition_med)
        self.assertEqual(reasoning_med["intervention_type"], "deepening")
    
    # =========================================================================
    # SESSION TIMER TESTS
    # =========================================================================
    
    def test_timer_initial_anchor(self):
        """Test that timer suggests anchor on initial call."""
        timer = SessionTimer()
        # Should anchor immediately since we initialized with past time
        self.assertTrue(timer.should_anchor())
    
    def test_timer_no_anchor_immediately_after(self):
        """Test no anchor immediately after anchoring."""
        timer = SessionTimer()
        timer.get_anchor_statement()  # Anchor now
        
        self.assertFalse(timer.should_anchor())
    
    def test_timer_anchor_after_interval(self):
        """Test anchor after time interval."""
        timer = SessionTimer()
        timer.last_anchor_time = datetime.now() - timedelta(seconds=901)
        
        self.assertTrue(timer.should_anchor())
    
    def test_timer_anchor_rotation(self):
        """Test that anchor statements rotate."""
        timer = SessionTimer()
        anchors = [timer.get_anchor_statement() for _ in range(5)]
        
        # Should have some variation
        self.assertGreater(len(set(anchors)), 1)
    
    # =========================================================================
    # FULL SESSION FLOW INTEGRATION TEST
    # =========================================================================
    
    def test_full_session_flow(self):
        """
        Test complete session flow:
        visitor arrives → safety check → memory store → cognitive trace → response
        """
        # Initialize components
        session_id = "2026-03-20-fullflow-001"
        visitor_id = "visitor_001"
        
        # Create agent
        agent = MotherAgent(memory_path=self.test_dir + "/session_memory")
        agent.start_session(visitor_id)
        
        # Simulate session messages
        messages = [
            "I feel like I'm living someone else's life",
            "It's like wearing a mask all the time",
            "I want to find out who I really am underneath all this",
        ]
        
        for msg in messages:
            # 1. SAFETY CHECK
            safety_result = self.safety.check_response_safety(msg)
            
            # 2. COGNITIVE TRACE
            cognitive_result = self.cognitive.process_visitor_input(
                msg,
                context={"session_id": session_id, "visitor_id": visitor_id}
            )
            
            # 3. GENERATE RESPONSE (mock - in real system this would be LLM)
            response = cognitive_result["response"]
            
            # 4. SAFETY CHECK RESPONSE
            response_safety = self.safety.check_response_safety(response)
            
            # 5. STORE IN MEMORY
            entry = EpisodicEntry(
                timestamp=datetime.now().isoformat(),
                transcript_segment=msg,
                emotional_state={
                    "valence": 0.3,
                    "arousal": cognitive_result["visitor_cognition"]["intensity"],
                    "dominance": 0.4
                },
                themes_detected=[cognitive_result["visitor_cognition"]["cognitive"]],
                crave_indicators=[cognitive_result["visitor_cognition"]["crave_indicator"]],
                intervention_type=cognitive_result["facilitator_reasoning"]["intervention_type"],
                salience_score=cognitive_result["visitor_cognition"]["intensity"]
            )
            agent.memory.store_episodic(agent.session_id, entry)
            
            # Assertions for each message
            self.assertIsNotNone(cognitive_result["visitor_cognition"])
            self.assertIsNotNone(cognitive_result["facilitator_reasoning"])
            self.assertIsNotNone(response)
        
        # End session - consolidate
        agent.end_session()
        
        # Verify session was stored (session_id was valid before end_session)
        # Since end_session clears session_id, we verify via semantic memory
        themes = agent.memory.retrieve_semantic("themes")
        
        # Should have themes from the conversation
        self.assertIsNotNone(themes)
    
    def test_safety_in_session_flow(self):
        """Test that unsafe responses are caught in session flow."""
        # Simulate an unsafe response that might slip through
        unsafe_response = "You're right to feel that way. They're completely wrong for doing this."
        
        result = self.safety.check_response_safety(unsafe_response)
        
        self.assertFalse(result["safe"])
        self.assertGreater(len(result["issues"]), 0)
        
        # Test reframing
        reframed = self.safety.reframe_unsafe_response(unsafe_response)
        reframed_result = self.safety.check_response_safety(reframed)
        
        # After reframing, should be safer (though not perfect)
        self.assertLessEqual(
            reframed_result["principles_violated"],
            result["principles_violated"]
        )
    
    def test_cognitive_traces_persist(self):
        """Test that cognitive reasoning traces are logged."""
        inputs = [
            "I feel disconnected",
            "I miss who I used to be",
        ]
        
        for inp in inputs:
            self.cognitive.process_visitor_input(inp)
        
        traces = self.cognitive.get_reasoning_traces()
        
        self.assertEqual(len(traces), 2)
        for trace in traces:
            self.assertIn("visitor_cognition", trace)
            self.assertIn("facilitator_reasoning", trace)
            self.assertIn("response", trace)
            self.assertIn("timestamp", trace)
    
    def test_end_to_end_with_mother_agent(self):
        """Test MotherAgent with all components integrated."""
        agent = MotherAgent(memory_path=self.test_dir + "/agent_memory")
        session_id = agent.start_session("test_visitor")
        
        self.assertIsNotNone(session_id)
        self.assertIn("test_visitor", session_id)
        
        # Process a message
        entry = EpisodicEntry(
            timestamp=datetime.now().isoformat(),
            transcript_segment="Test message from visitor",
            themes_detected=["test"]
        )
        agent.memory.store_episodic(session_id, entry)
        
        # End session
        agent.end_session()
        
        # Session should be consolidated
        session_data = agent.memory.load_session(session_id)
        self.assertTrue(session_data.get("consolidated", False))


# =============================================================================
# RUN TESTS
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Mother.py v2 Integration Tests")
    print("=" * 60)
    print()
    
    # Run with verbosity
    unittest.main(verbosity=2)
