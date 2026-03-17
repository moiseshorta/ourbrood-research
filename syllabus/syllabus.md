# OurBrood: LLM & Agentic Conversational SOTA
## Course Syllabus

**Institution:** OMSK Social Club  
**Course Type:** Research Seminar  
**Project:** OurBrood  
**Updated:** March 2026

---

## Course Description

This course explores the State of the Art (SOTA) in Large Language Models (LLMs) and agentic conversational systems through the lens of the OurBrood project—an AI-facilitated psychodrama system with two agents: Mother.py (persistent facilitator) and Brood.py (wake-word activated audience capture).

Through systematic analysis of 24+ peer-reviewed papers, students will develop frameworks for understanding AI personality, memory architecture, voice agents, and multi-agent coordination in participatory art contexts.

---

## Learning Objectives

By the end of this course, students will be able to:

1. **Analyze** voice agent architecture through the lens of real-time facilitation systems
2. **Evaluate** memory systems for multi-session psychodrama continuity
3. **Design** safety frameworks that prevent disempowerment in therapeutic contexts
4. **Synthesize** active inference approaches to multi-agent coordination
5. **Apply** theoretical knowledge to Mother.py and Brood.py implementation

---

## Course Context

### Real Game Play (RGP) Methodology

OurBrood is an artistic project by OMSK Social Club that employs "Real Game Play" (RGP) methodology:

- **Immersive improvised collective storytelling** — Participants engage in emergent narrative
- **Alternate selves exploration** — Roleplay as expanded versions of themselves
- **Participatory design** — Testing how we live together through roleplay
- **Collective intelligence raising** — Human + artificial intelligence collaboration
- **Responsibility negotiation** — Ecological and technological transformation contexts
- **High and low intensity experiences** — 3-hour intensive and extended formats

Commissioned by ArkDes, presented at museums and galleries internationally.

### Participatory AI Art Research Context

The intersection of AI agents, participatory art, and collective storytelling represents an emerging field with several key threads:

1. **AI in Interactive Art Installations** — Nieuwe Instituut, Ars Electronica, Transmediale
2. **Collective Storytelling with AI Agents** — AdaMARP, Drama Machine, StoryComposerAI
3. **Agency Distribution in Human-AI Co-Creation** — Sovereignty vs. entanglement frameworks
4. **Embodied vs. Screen-Based Participation** — Beyond text interfaces
5. **Ethics of AI-Guided Self-Exploration** — Psychological safety, power dynamics

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        OURBROOD ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   ┌────────────────────┐          ┌────────────────────┐            │
│   │      MOTHER.PY      │          │      BROOD.PY       │            │
│   │  ────────────────  │          │  ────────────────   │            │
│   │  • Persistent       │          │  • Stateless        │            │
│   │  • Facilitator      │          │  • Wake-word        │            │
│   │  • Psychodrama      │          │  • Audience capture │            │
│   │  • KB + Memory      │          │  • Fast response    │            │
│   └────────┬───────────┘          └────────┬───────────┘            │
│            │                              │                         │
│            ▼                              ▼                         │
│   ┌────────────────────────────────────────────────────────────┐   │
│   │                    VOICE PIPELINE                           │   │
│   │  MIC → RESAMPLE → WEBSOCKET → LLM → TTS → SPEAKER          │   │
│   └────────────────────────────────────────────────────────────┘   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Course Structure

### Module 1: Foundations of LLM Conversations (Weeks 1-2)

**Papers:**
- The Persona Selection Model (Anthropic, Feb 2026)
- The Assistant Axis (Anthropic, Jan 2026)

**Key Concepts:**
- LLMs enact personas learned during pretraining
- Neural representations reveal persona space
- Distance from "Assistant" predicts behavior

**Practical Exercise:**
Map Mother.py's facilitator persona on the Assistant Axis. Where does it sit? What conversational types trigger drift?

---

### Module 2: Personality in LLMs (Weeks 3-4)

**Papers:**
- VoxRole: Speech-Based Role-Playing Agents (arXiv:2509.03940)
- Persona Selection Model (Anthropic, Feb 2026)
- Assistant Axis (Anthropic, Jan 2026)

**Key Concepts:**
- Paralinguistic features for persona expression
- Long-term persona consistency in speech
- Persona drift detection and correction

**Practical Exercise:**
Design Mother's voice persona profile. Define paralinguistic characteristics for ElevenLabs TTS. Create persona drift monitoring system.

**Architecture Connection:**
- Mother.py voice persona must be consistent across 3+ hour sessions
- Voice persona requires specification beyond text
- Paralinguistic consistency metrics from VoxRole

---

### Module 3: Voice Agent Architecture (Weeks 5-6)

**Papers:**
- τ-Voice: Full-Duplex Voice Agents (arXiv:2603.08723)
- VoiceAgentRAG: Dual-Agent Architecture (arXiv:2603.08723)
- LTS-VoiceAgent: Listen-Think-Speak Framework (arXiv:2501.07895)

**Key Concepts:**
- Full-duplex: simultaneous listening/speaking
- Fast/Slow Thinker pattern for latency management
- Semantic triggering beyond wake-word

**Practical Exercise:**
Implement Fast/Slow Thinker pattern for Mother/Brood coordination. Design semantic triggering for Brood beyond wake-word.

**Architecture Connection:**
```
Brood = Fast Thinker
├── Session-scoped memory
├── Immediate response
├── No KB retrieval
└── Audience capture focus

Mother = Slow Thinker
├── Persistent memory + KB
├── Background retrieval
├── 90s recap consolidation
└── Psychodrama facilitation
```

---

### Module 4: Memory Systems (Weeks 7-8)

**Papers:**
- HiMem: Hierarchical Long-Term Memory (arXiv:2501.09123)
- MemGuide: Intent-Driven Memory Selection (arXiv:2505.20231)
- TiMem: Temporal Memory Consolidation (arXiv:2501.11345)
- Autonomous Memory Agents (arXiv:2502.11309)

**Key Concepts:**
- Three-layer memory hierarchy: Episodic → Semantic → Procedural
- Intent-driven retrieval vs. semantic similarity
- Temporal consolidation and forgetting curves
- Autonomous memory decisions

**Practical Exercise:**
Redesign Mother's memory from flat memory.txt to HiMem hierarchy. Implement intent-driven retrieval for psychodrama intents. Design autonomous storage triggers.

**Architecture Connection:**
```
Memory Hierarchy:

EPISODIC LAYER (High Detail, Recent)
├── Recent session transcripts
├── Active psychodrama threads
└── Current session state

SEMANTIC LAYER (Compressed, Derived)
├── Visitor patterns
├── Recurring themes
└── Crave taxonomy

PROCEDURAL LAYER (How to Facilitate)
├── Psychodrama techniques
├── Question frameworks
└── Intervention patterns
```

---

### Module 5: Psychodrama Facilitation with AI (Weeks 9-10)

**Papers:**
- Disempowerment Patterns in Real-World LLM Usage (arXiv:2601.19062)
- Empathy Modeling in Active Inference Agents (arXiv:2502.15589)
- AdaMARP: Immersive Role-Playing (arXiv:2501.XXXXX)
- The Drama Machine (arXiv:2408.05981)
- Human-AI Sovereignty (arXiv:2410.XXXXX)

**Key Concepts:**
- Disempowerment prevention in facilitation contexts
- Computational empathy through active inference
- Multi-agent facilitation coordination
- Power dynamics in human-AI co-creation

**Practical Exercise:**
Design Mother's disempowerment prevention system. Implement empathy architecture with cognitive/affective/behavioral levels. Create explicit agency negotiation framework.

**Safety Framework:**
```
PRINCIPLE 1: Distinguish Exploration from Validation
"Let's explore this together" ≠ "Your perspective is correct"

PRINCIPLE 2: Return Agency to User
"What words feel true for you?"

PRINCIPLE 3: Reality-Anchor Role-Play
"Remember, we're exploring possibilities"

PRINCIPLE 4: Avoid Definitive Moral Judgments
"How does that land for you?" (not "They're wrong")

PRINCIPLE 5: Generate Possibilities, Not Scripts
"Some approaches you might consider..."
```

---

### Module 6: Multi-Agent Coordination (Weeks 11-12)

**Papers:**
- Measuring AI Agent Autonomy (Anthropic, Feb 2026)
- ODAR: Adaptive Routing (arXiv:2502.07745)
- Resilient Design: Distributed Active Inference (arXiv:2511.10835)

**Key Concepts:**
- Deployment overhang: models can handle more than they're tasked with
- Active inference for routing decisions
- Distributed coordination without central control

**Practical Exercise:**
Implement ODAR-style routing between Mother and Brood. Design distributed coordination protocol. Create autonomy/safety balance system.

**Architecture Connection:**
```
Routing Decision:
├── Difficulty estimation: Is this audience capture or psychodrama?
├── Expected free energy: Balance exploration (Brood) with exploitation (Mother)
└── Coordination through KB sync
```

---

### Module 7: State of the Art Review (Weeks 13-14)

**Paper Presentations:**
Each student presents a paper not covered in modules, connecting it to OurBrood architecture.

**Topics:**
- Participatory AI Art papers
- Multi-agent dynamics research
- Alignment and safety research
- Active inference applications

---

### Module 8: Applied Research Project (Weeks 15-16)

**Project Options:**
1. Implement one component from Implementation Guide
2. Design evaluation framework for OurBrood
3. Create new research integration for emerging papers
4. Document safety testing protocol

---

## Required Readings by Module

### Module 1: Foundations
- `persona-selection-model.md` — Anthropic Research
- `assistant-axis.md` — Anthropic Research

### Module 2: Personality
- `voxrole-speech-role-playing.md` — Wu et al., Sep 2025
- `voxrole-speech-roleplaying.md` — Wu et al., Sep 2025

### Module 3: Voice Architecture
- `tau-voice-full-duplex.md` — Ray et al., Mar 2026
- `voice-agent-rag-latency.md` — Qiu et al., Mar 2026
- `lts-voice-agent-listen-think-speak.md` — Zou et al., Jan 2026

### Module 4: Memory
- `himem-hierarchical-memory.md` — Zhang et al., Jan 2026
- `memguide-multi-session-facilitation.md` — Du et al., May 2025
- `timem-temporal-memory.md` — Li et al., Jan 2026
- `autonomous-memory-agents.md` — Wu et al., Feb 2026

### Module 5: Psychodrama Facilitation
- `disempowerment-patterns-facilitation.md` — Sharma et al., Jan 2026
- `empathy-modeling-active-inference.md` — Mahault et al., Feb 2026
- `summaries/AdaMARP-immersive-roleplaying.md` — Xu et al., Jan 2026
- `summaries/drama-machine-character-simulation.md` — Magee et al., Aug 2024
- `summaries/human-ai-sovereignty-improvisation.md` — Oct 2025

### Module 6: Multi-Agent
- `measuring-agent-autonomy.md` — Anthropic, Feb 2026
- `odar-active-inference-llm-routing.md` — Ma et al., Feb 2026
- `resilient-design-active-inference.md` — Donta et al., Nov 2025

### Module 7: SOTA Review
- Selection from `papers-to-review.md` Priority sections

---

## Practical Exercises

### Exercise 1: Persona Mapping (Module 2)
Map Mother's facilitator persona on the Assistant Axis. Document:
- Where it sits on the axis
- What conversational types might cause drift
- Drift prevention strategies

### Exercise 2: Memory Hierarchy Design (Module 4)
Design Mother's memory hierarchy:
- Episodic layer structure
- Semantic extraction rules
- Procedural learning triggers
- Consolidation timing

### Exercise 3: Safety Framework Implementation (Module 5)
Implement disempowerment prevention:
- Response checking for validation language
- Agency return prompts
- Reality-anchoring interventions
- Success metrics beyond approval

### Exercise 4: Coordination Protocol (Module 6)
Design Mother/Brood coordination:
- Routing policy
- Belief sharing protocol
- Free energy calculations
- Fallback mechanisms

---

## Assessment

| Component | Weight | Description |
|-----------|--------|-------------|
| Module Quizzes | 15% | Weekly understanding checks |
| Paper Presentation | 25% | Present one paper with OurBrood connection |
| Implementation Project | 40% | Implement one component from Implementation Guide |
| Research Integration | 20% | Contribute to research integration documentation |

---

## Resources

### Papers Directory
All reviewed papers available in `/papers/`:
- Main summaries: `paper-name.md`
- Participatory AI Art: `papers/summaries/`
- Implementation Guide: `papers/IMPLEMENTATION_GUIDE.md`

### Integration Document
`INTEGRATION.md` — Comprehensive research integration:
- Architecture mapping
- Implementation priorities
- Code examples
- Open questions

### Architecture Documentation
`syllabus/architecture.md` — OurBrood system architecture

---

## Instructor Notes

*This syllabus is grounded in peer-reviewed research from 2024-2026. Each module connects directly to OurBrood implementation. Students should complete the Implementation Guide exercises alongside theoretical learning.*

---

*Last updated: March 2026*  
*Papers integrated: 24*  
*Domains: Psychodrama Facilitation, Voice + Memory Architecture, Real Game Play Methodology*