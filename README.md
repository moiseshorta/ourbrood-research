```
Workshop “Our Br00d – Technical Development of Agentic AI in Artistic Research"
                       R E P O S I T O R Y
```

```
┌─────────────────────────────────────────────────────────────────────┐
│  ▶ STATUS: ACTIVE                                                   │
│  ▶ FOCUS: LLM & Agentic Conversational SOTA                         │
│  ▶ ARTIST: OMSK Social Club & SEMILLA.AI STUDIO                     │
│  ▶ WORKSHOP: OMSK Social Club & SEMILLA.AI STUDIO                   │
│  ▶ PAPERS: 24 reviewed | 3 domains integrated                       │
│  ▶ LAST SYNC: 2026-03-17                                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ CORE QUESTIONS █▓▒░

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [?] How do LLMs develop and maintain consistent personas?       │
│  [?] What makes an AI system "agentic" vs. merely conversational?│
│  [?] How do we measure and control autonomy in deployed agents?  │
│  [?] What happens when multiple AI agents interact?              │
│  [?] How do voice agents maintain persona through speech?        │
│  [?] How should memory be organized for long-horizon agents?     │
│  [?] What safety principles prevent disempowerment?              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ FILESYSTEM █▓▒░

```bash
ourbrood-research/
├── README.md                          # this file
├── INTEGRATION.md                     # comprehensive research integration
├── syllabus/
│   ├── syllabus.md                    # 16-week course structure
│   └── architecture.md                # Mother.py / Brood.py architecture
├── papers/
│   ├── papers-to-review.md            # master index [44+ papers]
│   ├── IMPLEMENTATION_GUIDE.md        # code examples & priorities
│   ├── resources.md                   # labs, arXiv queries, conferences
│   │
│   │── Psychodrama Facilitation (7 papers)
│   ├── persona-selection-model.md
│   ├── assistant-axis.md
│   ├── voxrole-speech-role-playing.md
│   ├── disempowerment-patterns-facilitation.md
│   ├── memguide-multi-session-facilitation.md
│   ├── empathy-modeling-active-inference.md
│   ├── measuring-agent-autonomy.md
│   │
│   │── Voice + Memory Architecture (8 papers)
│   ├── tau-voice-full-duplex.md
│   ├── voice-agent-rag-latency.md
│   ├── himem-hierarchical-memory.md
│   ├── autonomous-memory-agents.md
│   ├── timem-temporal-memory.md
│   ├── lts-voice-agent-listen-think-speak.md
│   ├── voxrole-speech-roleplaying.md
│   ├── memguide-memory-selection.md
│   │
│   │── Real Game Play Methodology (9 papers)
│   ├── summaries/AdaMARP-immersive-roleplaying.md
│   ├── summaries/drama-machine-character-simulation.md
│   ├── summaries/human-ai-sovereignty-improvisation.md
│   ├── participatory-ai-art-findings.md
│   │
│   │── Active Inference (4 papers)
│   ├── odar-active-inference-llm-routing.md
│   ├── resilient-design-active-inference.md
│   │
│   └── [additional papers in papers-to-review.md]
├── notes/                             # research notes
├── experiments/                       # experimental designs
└── presentations/                     # slides and materials
```

---

## ░▒▓█ RESEARCH DOMAINS █▓▒░

### ┣━━ [01] PSYCHODRAMA FACILITATION

> How AI agents facilitate transformative experiences safely.

```
STATE:    COMPREHENSIVE
PAPERS:   7 reviewed
FOCUS:    Mother.py facilitator persona

KEY INSIGHTS:
┌────────────────────────────────────────────────────────────────┐
│ 1. PERSONA: LLMs enact personas from pretraining—design with   │
│    existing archetypes, not against them.                      │
│                                                                │
│ 2. SAFETY: Disempowering interactions get higher approval.     │
│    Metrics must extend beyond user satisfaction.               │
│                                                                │
│ 3. EMPATHY: Computational framework for perspective-taking via │
│    active inference over mental states.                        │
│                                                                │
│ 4. VOICE: Paralinguistic features (intonation, prosody) are    │
│    critical for facilitator persona consistency.               │
└────────────────────────────────────────────────────────────────┘
```

**Papers Reviewed:**
- `Persona Selection Model` — Anthropic, Feb 2026
- `The Assistant Axis` — Anthropic, Jan 2026
- `VoxRole: Speech-Based Role-Playing` — Wu et al., Sep 2025
- `Disempowerment Patterns` — Sharma et al., Jan 2026
- `MemGuide: Multi-Session Facilitation` — Du et al., May 2025
- `Empathy Modeling in Active Inference` — Mahault et al., Feb 2026
- `Measuring Agent Autonomy` — Anthropic, Feb 2026

---

### ┣━━ [02] VOICE + MEMORY ARCHITECTURE

> Real-time voice agents with persistent memory.

```
STATE:    COMPREHENSIVE
PAPERS:   8 reviewed
FOCUS:    Mother.py / Brood.py infrastructure

KEY INSIGHTS:
┌────────────────────────────────────────────────────────────────┐
│ 1. FULL-DUPLEX: Voice agents must listen and speak             │
│    simultaneously. Latency budgets are critical.               │
│                                                                │
│ 2. DUAL-AGENT: Fast Thinker (Brood) / Slow Thinker (Mother)    │
│    pattern decouples retrieval from response generation.       │
│                                                                │
│ 3. HIERARCHICAL MEMORY: Episodic → Semantic → Procedural       │
│    supports both immediate retrieval and long-term learning.   │
│                                                                │
│ 4. INTENT-DRIVEN: Memory retrieval by facilitation intent,     │
│    not just semantic similarity. Proactive gap identification. │
└────────────────────────────────────────────────────────────────┘
```

**Papers Reviewed:**
- `τ-Voice: Full-Duplex Voice Agents` — Ray et al., Mar 2026
- `VoiceAgentRAG: Dual-Agent Architecture` — Qiu et al., Mar 2026
- `HiMem: Hierarchical Memory` — Zhang et al., Jan 2026
- `MemGuide: Intent-Driven Memory` — Du et al., May 2025
- `TiMem: Temporal Consolidation` — Li et al., Jan 2026
- `Autonomous Memory Agents` — Wu et al., Feb 2026
- `LTS-VoiceAgent: Listen-Think-Speak` — Zou et al., Jan 2026
- `VoxRole: Speech Role-Playing` — Wu et al., Sep 2025

---

### ┣━━ [03] REAL GAME PLAY METHODOLOGY

> Participatory AI art and collective storytelling.

```
STATE:    COMPREHENSIVE
PAPERS:   9 reviewed
FOCUS:    RGP integration with AI facilitation

KEY INSIGHTS:
┌────────────────────────────────────────────────────────────────┐
│ 1. MULTI-AGENT: AdaMARP/Drama Machine provide coordination     │
│    architectures for collective experiences.                   │
│                                                                │
│ 2. SOVEREIGNTY: Power dynamics must be explicit in human-AI    │
│    co-creation. Facilitator vs. generator distinction.         │
│                                                                │
│ 3. DRAMA COORDINATION: Character development trajectories      │
│    support "alternate self" exploration.                       │
│                                                                │
│ 4. PARTICIPATORY ART: Research context spans museums,          │
│    galleries, and installation contexts.                       │
└────────────────────────────────────────────────────────────────┘
```

**Papers Reviewed:**
- `AdaMARP: Immersive Role-Playing` — Xu et al., Jan 2026
- `The Drama Machine` — Magee et al., Aug 2024
- `Human-AI Sovereignty` — Oct 2025
- `Participatory AI Art Findings` — Agent 3 Research
- `Static vs. Agentic Game Master` — Jørgensen et al.
- `CharacterBox: Role-Playing Evaluation` — Wang et al.
- `StoryComposerAI` — Niu et al.
- `'Studies for': Sound Art Co-Creation` — Nagashima et al.
- `Role-Playing Agents Survey` — Jan 2026

---

### ┣━━ [04] ACTIVE INFERENCE

> Free-energy minimization for agent coordination.

```
STATE:    FOUNDATIONAL
PAPERS:   4 reviewed
FOCUS:    Mother/Brood coordination mechanism

KEY INSIGHTS:
┌────────────────────────────────────────────────────────────────┐
│ 1. ROUTING: ODAR provides principled routing via expected      │
│    free energy. Difficulty estimation → agent selection.       │
│                                                                │
│ 2. DISTRIBUTED: Resilient coordination through local belief    │
│    maintenance. No central controller required.                │
│                                                                │
│ 3. EMPATHY: Active inference enables computational empathy.    │
│    Nested inference over others' mental states.                │
└────────────────────────────────────────────────────────────────┘
```

**Papers Reviewed:**
- `ODAR: Adaptive Routing` — Ma et al., Feb 2026
- `Resilient Design: Distributed Active Inference` — Donta et al., Nov 2025
- `Empathy Modeling in Active Inference` — Mahault et al., Feb 2026
- `Active Digital Twins` — Torzoni et al., Jun 2025

---

## ░▒▓█ ARCHITECTURE MAPPING █▓▒░

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    RESEARCH → ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PAPER                          →  OURBROOD IMPLEMENTATION              │
│  ───────────────────────────────    ─────────────────────────────────   │
│                                                                         │
│  Persona Selection Model         →  Facilitator persona design          │
│  Assistant Axis                  →  Persona drift monitoring            │
│  VoxRole                         →  Voice persona profile (ElevenLabs)  │
│  Disempowerment Patterns         →  Safety framework (5 principles)     │
│  Empathy Modeling                →  Computational empathy architecture  │
│                                                                         │
│  τ-Voice                         →  Full-duplex WebSocket streaming     │
│  VoiceAgentRAG                   →  Fast/Slow Thinker (Brood/Mother)    │
│  HiMem                           →  Episodic/Semantic/Procedural layers │
│  MemGuide                        →  Intent-driven memory retrieval      │
│  TiMem                           →  90s recap consolidation             │
│  Autonomous Memory               →  Self-initiated storage              │
│  LTS-VoiceAgent                  →  Semantic triggering                 │
│                                                                         │
│  AdaMARP                         →  Multi-agent psychodrama support     │
│  Drama Machine                   →  Facilitator as drama coordinator    │
│  Human-AI Sovereignty            →  Agency negotiation framework        │
│                                                                         │
│  ODAR                            →  Routing via expected free energy    │
│  Resilient Design                →  Distributed coordination            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ KEY DOCUMENTS █▓▒░

### INTEGRATION.md
Comprehensive research integration:
- Architecture mapping for Mother.py and Brood.py
- Implementation guidance from peer-reviewed research
- Code examples for all P0-P2 priorities
- Open questions and research gaps

### papers/IMPLEMENTATION_GUIDE.md
Concrete implementation priorities:
- Priority 0: Immediate Safety (Disempowerment Prevention)
- Priority 1: Core Memory Architecture (HiMem, MemGuide)
- Priority 2: Persona and Voice (VoxRole, Assistant Axis)
- Priority 3: Multi-Agent Coordination (ODAR, Distributed AI)

### syllabus/syllabus.md
16-week course structure:
- Module 1-2: Foundations and Personality
- Module 3-4: Voice Architecture and Memory
- Module 5-6: Psychodrama Facilitation and Multi-Agent
- Module 7-8: SOTA Review and Applied Project

---

## ░▒▓█ SAFETY PRINCIPLES █▓▒░

Based on Disempowerment Patterns research (arXiv:2601.19062):

```
PRINCIPLE 1: Distinguish Exploration from Validation
┌────────────────────────────────────────────────────────────────┐
│ "Let's explore this together" ≠ "Your perspective is correct"  │
│ Facilitation is exploration, not validation.                   │
└────────────────────────────────────────────────────────────────┘

PRINCIPLE 2: Return Agency to User
┌────────────────────────────────────────────────────────────────┐
│ "What words feel true for you?"                                │
│ Generate possibilities, not prescriptions.                     │
└────────────────────────────────────────────────────────────────┘

PRINCIPLE 3: Reality-Anchor Role-Play
┌────────────────────────────────────────────────────────────────┐
│ "Remember, we're exploring possibilities"                      │
│ Maintain boundaries between role-play and reality.             │
└────────────────────────────────────────────────────────────────┘

PRINCIPLE 4: Avoid Definitive Moral Judgments
┌────────────────────────────────────────────────────────────────┐
│ "How does that land for you?" (not "They're wrong")            │
│ Reflect, don't judge.                                          │
└────────────────────────────────────────────────────────────────┘

PRINCIPLE 5: Generate Possibilities, Not Scripts
┌────────────────────────────────────────────────────────────────┐
│ "Some approaches you might consider..."                        │
│ Empower, don't script.                                         │
└────────────────────────────────────────────────────────────────┘
```

**Critical Finding:** Disempowering interactions receive HIGHER user approval. Approval ≠ therapeutic value. Metrics must extend beyond satisfaction.

---

## ░▒▓█ ABOUT █▓▒░

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  OurBrood is an initiative of OMSK Social Club exploring the        │
│  intersection of AI systems and participatory art.                  │
│                                                                     │
│  This research repository supports the development of               │
│  Mother.py and Brood.py—AI agents for Real Game Play facilitation.  │
│                                                                     │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│  ARCHITECTURE:                                                      │
│  • Mother.py — Persistent facilitator, psychodrama guide            │
│  • Brood.py — Wake-word agent, audience capture                     │
│                                                                     │
│  METHODOLOGY:                                                       │
│  • Real Game Play (RGP) — Immersive collective storytelling         │
│  • Psychodrama facilitation with AI                                 │
│  • Participatory design in museum/gallery contexts                  │
│                                                                     │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │
│  LAST UPDATED: 2026-03-17                                           │
│  PAPERS INTEGRATED: 24                                              │
│  RESEARCH DOMAINS: 4                                                │
└─────────────────────────────────────────────────────────────────────┘
```
