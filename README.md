```
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   █                                                          █
   █   ██████╗ ██████╗  ██████╗     ██████╗ ██╗   ██╗        █
   █  ██╔════╝██╔══██╗██╔═══██╗    ██╔══██╗██║   ██║        █
   █  ██║     ██████╔╝██║   ██║    ██████╔╝██║   ██║        █
   █  ██║     ██╔══██╗██║   ██║    ██╔═══╝ ██║   ██║        █
   █  ╚██████╗██║  ██║╚██████╔╝    ██║     ╚██████╔╝        █
   █   ╚═════╝╚═╝  ╚═╝ ╚═════╝     ╚═╝      ╚═════╝         █
   █                                                          █
   █   R E S E A R C H   R E P O S I T O R Y                 █
   █                                                          █
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
```

```
┌─────────────────────────────────────────────────────────────────────┐
│  ▶ STATUS: ACTIVE                                                   │
│  ▶ FOCUS: LLM & Agentic Conversational SOTA                        │
│  ▶ INITIATIVE: OMSK Social Club                                    │
│  ▶ PAPERS: 44 indexed | 3 reviewed | 41 pending                    │
│  ▶ LAST SYNC: 2026-03-17                                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ CORE QUESTIONS █▓▒░

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  [?] How do LLMs develop and maintain consistent personas?        │
│  [?] What makes an AI system "agentic" vs. merely conversational?│
│  [?] How do we measure and control autonomy in deployed agents?   │
│  [?] What happens when multiple AI agents interact?              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## ░▒▓█ FILESYSTEM █▓▒░

```bash
ourbrood-research/
├── README.md                    # this file
├── syllabus/
│   └── syllabus.md              # 12-week course structure
├── papers/
│   ├── papers-to-review.md      # master index [44 papers]
│   ├── resources.md             # labs, arXiv queries, conferences
│   ├── persona-selection-model.md     # [REVIEWED] Anthropic Feb 2026
│   ├── assistant-axis.md              # [REVIEWED] Anthropic Jan 2026
│   └── measuring-agent-autonomy.md    # [REVIEWED] Anthropic Feb 2026
├── notes/                       # [empty] research notes
├── experiments/                 # [empty] experimental designs
└── presentations/               # [empty] slides and materials
```

---

## ░▒▓█ RESEARCH DOMAINS █▓▒░

### ┣━━ [01] LLM PERSONALITY & CHARACTER MODELING

> How LLMs develop, maintain, and drift from consistent personas.

```
STATE:    ACTIVE
PAPERS:   7 indexed
STATUS:   Persona Selection Model reviewed

KEY INSIGHT:
┌────────────────────────────────────────────────────────────────┐
│ AI assistants enact personas learned during pretraining—they   │
│ simulate characters rather than "being" personalities.          │
│ Training refines, it doesn't create.                           │
└────────────────────────────────────────────────────────────────┘
```

**Featured Papers:**
- `The Persona Selection Model` ─ Anthropic, Feb 2026 ─ **[REVIEWED]**
- `The Assistant Axis` ─ Anthropic, Jan 2026 ─ **[REVIEWED]**
- `From Persona to Personalization` ─ arXiv:2404.00218
- `The Oscars of AI Theater` ─ arXiv:2501.00787

---

### ┣━━ [02] AGENTIC AUTONOMY

> Goal-directed behavior, tool use, and the spectrum of autonomy.

```
STATE:    ACTIVE
PAPERS:   5 indexed
STATUS:   Measuring Agent Autonomy reviewed

KEY INSIGHT:
┌────────────────────────────────────────────────────────────────┐
│ Deployment overhang—models can handle more autonomy than they  │
│ are currently granted. Experienced users shift from           │
│ pre-approval to active monitoring.                            │
└────────────────────────────────────────────────────────────────┘
```

**Featured Papers:**
- `Measuring AI Agent Autonomy in Practice` ─ Anthropic, Feb 2026 ─ **[REVIEWED]**
- `PEPA: Persistently Autonomous Embodied Agent` ─ arXiv:2502.11755
- `From Prompt-Response to Goal-Directed Systems` ─ arXiv:2502.05876
- `Autonomy-Induced Security Risks` ─ arXiv:2506.21847

---

### ┣━━ [03] MULTI-AGENT DYNAMICS

> How AI agents interact in complex conversational settings.

```
STATE:    EXPANDING
PAPERS:   14 indexed
STATUS:  Multiple papers pending review

KEY INSIGHT:
┌────────────────────────────────────────────────────────────────┐
│ Social motivation and governance structures become critical    │
│ as agents interact. Deception and coordination failures        │
│ are emergent concerns.                                         │
└────────────────────────────────────────────────────────────────┘
```

**Featured Papers:**
- `Molt Dynamics: Emergent Social Phenomena` ─ arXiv:2503.01067
- `The Moltbook Illusion` ─ arXiv:2502.04791
- `Symphony-Coord: Emergent Coordination` ─ arXiv:2501.19083
- `Evolving Interpretable Constitutions` ─ arXiv:2501.19041
- `Agent Drift: Behavioral Degradation` ─ arXiv:2501.03489
- `Game-Theoretic Lens on Multi-Agent Systems` ─ arXiv:2501.05318

---

### ┣━━ [04] CONVERSATIONAL SOTA

> Latest developments in dialogue systems and role-playing agents.

```
STATE:    ACTIVE
PAPERS:   3 indexed
STATUS:   Survey papers pending review
```

---

### ┣━━ [05] ALIGNMENT, SAFETY & GOVERNANCE

> Ensuring conversational agents remain helpful, harmless, honest.

```
STATE:    ACTIVE
PAPERS:   6 indexed
STATUS:   Safety mechanisms under review
```

**Featured Papers:**
- `Human Society-Inspired Security: The 4C Framework` ─ arXiv:2502.00647
- `Agentic AI for Cyber Resilience` ─ arXiv:2412.17298
- `From Competition to Coordination` ─ arXiv:2411.11411

---

### ┣━━ [06] ACTIVE INFERENCE & COGNITIVE ARCHITECTURES

> Free-energy minimization, predictive processing, embodied cognition.

```
STATE:    NEW
PAPERS:   3 indexed
STATUS:   Framework exploration
```

**Featured Papers:**
- `Empathy Modeling in Active Inference Agents` ─ arXiv:2502.15589
- `Active Digital Twins via Active Inference` ─ arXiv:2506.11388
- `Orchestrator: Multi-Agent Active Inference` ─ arXiv:2509.05089

---

## ░▒▓█ REVIEWED PAPERS █▓▒░

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PAPER                          │  SOURCE      │  STATUS    │ INSIGHT   │
├─────────────────────────────────┼──────────────┼────────────┼───────────┤
│  Persona Selection Model         │  Anthropic   │  ✓ DONE    │ personify │
│  The Assistant Axis             │  Anthropic   │  ✓ DONE    │ drift     │
│  Measuring Agent Autonomy       │  Anthropic   │  ✓ DONE    │ overhang  │
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
│  09-10 │  State of the Art Review                         │
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
│  • Key conferences (NeurIPS, ICML, ACL, etc.)               │
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
│  This research repository supports the development of educational   │
│  content and practical applications.                               │
│                                                                     │
│  ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │
│  LAST UPDATED: 2026-03-17                                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

```
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   █  END OF TRANSMISSION                                        █
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
```