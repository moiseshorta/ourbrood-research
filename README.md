```
  ███  █   █ █████ █████ █████ ███  ███  ████  
 █   █ █   █ █     █     █     █   █ █   █ █   █ 
 █   █ █   █ █████ █████ █████ █   █ █   █ █   █
 █   █ █   █ █   █ █   █ █   █ █   █ █   █ █  █ 
  ████  ███  █████ █████ █████ ████   ███  ████  
                                                
           R E S E A R C H   R E P O S I T O R Y
```

```
┌─────────────────────────────────────────────────────────────────────┐
│  ▶ STATUS: ACTIVE                                                   │
│  ▶ FOCUS: OurBrood AI Agent Architecture                           │
│  ▶ INITIATIVE: OMSK Social Club / SEMILLA.AI Studio               │
│  ▶ PAPERS: 52 indexed | 29 reviewed | Architecture-aligned         │
│  ▶ LAST SYNC: 2026-03-17                                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ ARCHITECTURE ALIGNMENT █▓▒░

This research repository is aligned with the **OurBrood AI Agent Architecture**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  mother.py (1271 lines)          brood.py (693 lines)              │
│  ─────────────────────           ─────────────────────             │
│  • Guardian/facilitator          • Wake-word activated             │
│  • Psychodrama sessions          • Stateless, session-scoped       │
│  • Persistent memory (KB)        • Multi-channel audio            │
│  • ElevenLabs TTS                • 15-second activation window    │
│  • Long-term recall              • Captures audience interactions  │
│                                                                     │
│  Research focus:                  Research focus:                   │
│  ─ Psychodrama facilitation      ─ Voice agent architectures       │
│  ─ Empathy modeling              ─ Wake-word systems               │
│  ─ Multi-session memory          ─ Stateless agent design          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

See [`syllabus/architecture.md`](syllabus/architecture.md) for full architecture documentation.

---

## ░▒▓█ CORE QUESTIONS █▓▒░

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [?] How do AI facilitators guide psychodrama sessions?          │
│  [?] What makes voice agents effective in immersive contexts?    │
│  [?] How does Real Game Play methodology translate to AI?       │
│  [?] What are the safety implications of AI-guided exploration? │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ FILESYSTEM █▓▒░

```bash
ourbrood-research/
├── README.md                       # this file
├── syllabus/
│   ├── syllabus.md                 # 12-week course structure
│   └── architecture.md             # Mother/Brood AI architecture
├── papers/
│   ├── papers-to-review.md         # master index [52 papers]
│   ├── resources.md                # labs, arXiv queries, conferences
│   ├── participatory-ai-art-findings.md  # [NEW] RGP methodology
│   │
│   ├── Priority 0: OurBrood Core ─────────────────────────────────
│   ├── voxrole-*.md                # Voice role-playing evaluation
│   ├── disempowerment-*.md         # Safety framework
│   ├── memguide-*.md               # Multi-session memory
│   ├── tau-voice-*.md              # Full-duplex voice
│   ├── himem-*.md                  # Hierarchical memory
│   ├── empathy-*.md                # Active inference empathy
│   │
│   ├── Priority 1-2: Persona & Character ────────────────────────
│   ├── persona-selection-model.md  # [REVIEWED]
│   ├── assistant-axis.md           # [REVIEWED]
│   ├── her-*.md                    # Human-like reasoning
│   ├── anonymous-*.md              # Role-playing evaluation
│   │
│   └── Priority 3-7: Multi-Agent, Alignment, etc. ────────────────
│       └── [29 additional papers]
├── notes/                          # [empty] research notes
├── experiments/                    # [empty] experimental designs
└── presentations/                   # [empty] slides and materials
```

---

## ░▒▓█ RESEARCH DOMAINS █▓▒░

### ┣━━ [00] OURBROOD CORE (Architecture-Aligned)

> Papers directly applicable to Mother.py and Brood.py implementation.

```
STATE:    ACTIVE
PAPERS:   24 indexed
STATUS:   Integration in progress

KEY INSIGHT:
┌────────────────────────────────────────────────────────────────┐
│ Three research streams aligned with our two-agent architecture: │
│                                                                 │
│ 1. Psychodrama Facilitation ── Mother.py as guide/facilitator   │
│ 2. Voice + Memory Architecture ─ Both agents (TTS, KB, state)  │
│ 3. Real Game Play ─────────── OMSK methodology, participatory  │
└────────────────────────────────────────────────────────────────┘
```

**Featured Papers:**

| Paper | Focus | OurBrood Connection |
|-------|-------|---------------------|
| `VoxRole` | Speech role-playing evaluation | Mother's voice persona |
| `Disempowerment Patterns` | Safety in guided exploration | Mother.py safety |
| `MemGuide` | Multi-session intent-driven memory | Mother's KB retrieval |
| `τ-Voice` | Full-duplex voice agents | Real-time listening/speaking |
| `VoiceAgentRAG` | Fast/Slow Thinker pattern | Brood (fast) / Mother (slow) |
| `HiMem` | Hierarchical memory | Mother's memory architecture |
| `AdaMARP` | Multi-agent immersive role-play | RGP collective storytelling |
| `Drama Machine` | Character simulation | RGP character transformation |
| `Human-AI Sovereignty` | Power dynamics in co-creation | Negotiating responsibility |

---

### ┣━━ [01] LLM PERSONALITY & CHARACTER MODELING

> How LLMs develop, maintain, and drift from consistent personas.

```
STATE:    ACTIVE
PAPERS:   13 indexed
STATUS:   Persona Selection Model reviewed

KEY INSIGHT:
┌────────────────────────────────────────────────────────────────┐
│ AI assistants enact personas learned during pretraining—they   │
│ simulate characters rather than "being" personalities.        │
│ Training refines, it doesn't create.                         │
└────────────────────────────────────────────────────────────────┘
```

**Featured Papers:**
- `The Persona Selection Model` ─ Anthropic, Feb 2026 ─ **[REVIEWED]**
- `The Assistant Axis` ─ Anthropic, Jan 2026 ─ **[REVIEWED]**
- `HER: Human-like Reasoning for Role-playing` ─ arXiv:2601.21459
- `Facet-level Persona Control via SAE` ─ arXiv:2602.19157

---

### ┣━━ [02] AGENTIC AUTONOMY

> Goal-directed behavior, tool use, and the spectrum of autonomy.

```
STATE:    ACTIVE
PAPERS:   6 indexed
STATUS:   Measuring Agent Autonomy reviewed

KEY INSIGHT:
┌────────────────────────────────────────────────────────────────┐
│ Deployment overhang—models can handle more autonomy than they  │
│ are currently granted. Experienced users shift from          │
│ pre-approval to active monitoring.                            │
└────────────────────────────────────────────────────────────────┘
```

**Featured Papers:**
- `Measuring AI Agent Autonomy in Practice` ─ Anthropic, Feb 2026 ─ **[REVIEWED]**
- `Yerkes-Dodson Curve for AI Agents` ─ arXiv:2603.07360
- `Unintended Misalignment from Agentic Fine-Tuning` ─ arXiv:2508.11952

---

### ┣━━ [03] MULTI-AGENT DYNAMICS

> How AI agents interact in complex conversational settings.

```
STATE:    EXPANDING
PAPERS:   14 indexed
STATUS:   Multiple papers pending review

KEY INSIGHT:
┌────────────────────────────────────────────────────────────────┐
│ Social motivation and governance structures become critical    │
│ as agents interact. Deception and coordination failures       │
│ are emergent concerns.                                       │
└────────────────────────────────────────────────────────────────┘
```

**Featured Papers:**
- `Institutional AI Governance` ─ arXiv:2601.10863
- `Social Catalysts, Not Moral Agents` ─ arXiv:2602.02598
- `Game-Theoretic Lens on Multi-Agent Systems` ─ arXiv:2501.05318

---

### ┣━━ [04] ALIGNMENT, SAFETY & GOVERNANCE

> Ensuring conversational agents remain helpful, harmless, honest.

```
STATE:    ACTIVE
PAPERS:   6 indexed
STATUS:   Safety mechanisms under review
```

**Featured Papers:**
- `Who's in Charge? Disempowerment Patterns` ─ Anthropic, Jan 2026
- `Empathy Modeling in Active Inference Agents` ─ arXiv:2502.01947
- `ODAR: Principled Adaptive Routing` ─ arXiv:2502.07745

---

### ┣━━ [05] ACTIVE INFERENCE & COGNITIVE ARCHITECTURES

> Free-energy minimization, predictive processing, embodied cognition.

```
STATE:    ACTIVE
PAPERS:   4 indexed
STATUS:   Framework exploration
```

**Featured Papers:**
- `Empathy Modeling in Active Inference Agents` ─ arXiv:2502.01947
- `Resilient by Design: Active Inference` ─ arXiv:2511.10835
- `ODAR: LLM Routing via Active Inference` ─ arXiv:2502.07745

---

## ░▒▓█ REVIEWED PAPERS █▓▒░

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PAPER                              │  SOURCE      │  STATUS    │ INSIGHT   │
├──────────────────────────────────────┼──────────────┼────────────┼───────────┤
│  Persona Selection Model             │  Anthropic   │  ✓ DONE    │ personify │
│  The Assistant Axis                  │  Anthropic   │  ✓ DONE    │ drift     │
│  Measuring Agent Autonomy            │  Anthropic   │  ✓ DONE    │ overhang  │
│  VoxRole Speech Role-Playing         │  arXiv       │  ✓ DONE    │ voice     │
│  Disempowerment Patterns              │  Anthropic   │  ✓ DONE    │ safety    │
│  MemGuide Multi-Session              │  arXiv       │  ✓ DONE    │ memory    │
│  AdaMARP Immersive Role-Play         │  arXiv       │  ✓ DONE    │ rgp       │
│  ... and 22 more                     │              │            │           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ SYLLABUS █▓▒░

```
┌─────────────────────────────────────────────────────────────┐
│  WEEK  │  MODULE                                          │
├────────┼──────────────────────────────────────────────────┤
│  01-02 │  Foundations of LLM Conversations                │
│  03-04 │  Personality in LLMs                             │
│  05-06 │  Agentic Behavior & Autonomy                     │
│  07-08 │  Multi-Agent Conversational Dynamics              │
│  09-10 │  Psychodrama Facilitation with AI                 │
│  11-12 │  Applied Research Project                        │
└─────────────────────────────────────────────────────────────┘
```

See [`syllabus/syllabus.md`](syllabus/syllabus.md) for full details.

---

## ░▒▓█ RESOURCES █▓▒░

See [`papers/resources.md`](papers/resources.md) for:

```
┌─────────────────────────────────────────────────────────────┐
│  • Research labs (Anthropic, OpenAI, DeepMind, Meta)       │
│  • ArXiv search queries                                     │
│  • Benchmarks & datasets                                   │
│  • Key conferences (NeurIPS, ICML, ACL, DAFx, etc.)         │
│  • Agent frameworks & interpretability tools               │
└─────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ ABOUT █▓▒░

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  OurBrood is an initiative of OMSK Social Club exploring the       │
│  intersection of AI systems and social dynamics.                    │
│                                                                     │
│  AI Architecture by SEMILLA.AI Studio (Moisés Horta)               │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│  mother.py ─ Guardian/facilitator (psychodrama sessions)           │
│  brood.py  ─ Wake-word activated audience agent (stateless)        │
│                                                                     │
│  Commissioned by ArkDes and Nieuwe Instituut                       │
│  Presented at ArkDes, Stockholm 2025                               │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │
│  LAST UPDATED: 2026-03-17                                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

```
  ███  █   █ ████  
 █   █ █   █ █   █ 
 █   █ █   █ █   █
 █   █ █   █ █  █ 
  ████  ███  ████  
```