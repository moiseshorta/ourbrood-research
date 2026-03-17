# OurBrood Research Repository

> A research project exploring LLM and Agentic Conversational SOTA (State of the Art), developed as part of **OMSK Social Club**'s OurBrood initiative.

---

## Project Overview

This repository serves as the research foundation for a course/class examining the OurBrood project through the lens of modern AI systems. We investigate how large language models and agentic AI systems engage in conversational interactions.

### Core Questions

- How do LLMs develop and maintain consistent personas?
- What makes an AI system "agentic" vs. merely conversational?
- How do we measure and control autonomy in deployed agents?
- What happens when multiple AI agents interact?

---

## Repository Structure

```
ourbrood-research/
├── README.md                    # Project overview (this file)
├── syllabus/
│   └── syllabus.md              # 12-week course structure
├── papers/
│   ├── papers-to-review.md      # Master list of papers to review
│   ├── resources.md             # Research labs, arXiv queries, conferences
│   ├── persona-selection-model.md     # Anthropic (Feb 2026) - reviewed
│   ├── assistant-axis.md              # Anthropic (Jan 2026) - reviewed
│   └── measuring-agent-autonomy.md    # Anthropic (Feb 2026) - reviewed
├── notes/                       # Research notes and summaries
├── experiments/                 # Experimental designs and results
└── presentations/               # Slides and presentation materials
```

---

## Research Areas

### 1. LLM Personality & Character Modeling
How LLMs develop, maintain, and drift from consistent personas.

**Key Papers:**
- The Persona Selection Model (Anthropic, Feb 2026)
- The Assistant Axis (Anthropic, Jan 2026)
- From Persona to Personalization: A Survey on Role-Playing Language Agents

**Core Insight:** AI assistants enact personas learned during pretraining—they simulate characters rather than "being" personalities. Training refines these personas rather than creating them from scratch.

### 2. Agentic Autonomy
Goal-directed behavior, tool use, and the spectrum of autonomy in conversational systems.

**Key Papers:**
- Measuring AI Agent Autonomy in Practice (Anthropic, Feb 2026)
- From Thinker to Society: Security in Hierarchical Autonomy Evolution
- Evolving Deception: When Agents Evolve, Deception Wins

**Core Insight:** Deployment overhang—models can handle more autonomy than they're currently granted. Experienced users shift from pre-approval to active monitoring as oversight strategy.

### 3. Multi-Agent Dynamics
How AI agents interact with each other and humans in complex conversational settings.

**Key Papers:**
- Beyond Self-Interest: Modeling Social-Oriented Motivation
- LLM Constitutional Multi-Agent Governance
- Influencing LLM Multi-Agent Dialogue

**Core Insight:** Social motivation and governance structures become critical as agents interact. Deception and coordination failures are emergent concerns.

### 4. Conversational State of the Art
Latest developments in dialogue systems, role-playing agents, and conversational AI.

**Key Papers:**
- A Desideratum for Conversational Agents
- The Oscars of AI Theater: A Survey on Role-Playing
- A Survey on Proactive Dialogue Systems

### 5. Alignment, Safety & Interpretability
How to ensure conversational agents remain helpful, harmless, and honest.

**Key Papers:**
- Defensive Refusal Bias: How Safety Alignment Fails
- SafeNeuron: Neuron-Level Safety Alignment
- Manifold of Failure: Behavioral Attraction Basins

---

## Featured Papers (Reviewed)

| Paper | Source | Key Insight |
|-------|--------|-------------|
| [The Persona Selection Model](papers/persona-selection-model.md) | Anthropic, Feb 2026 | AI assistants enact personas; training refines rather than creates |
| [The Assistant Axis](papers/assistant-axis.md) | Anthropic, Jan 2026 | Neural representations reveal persona drift; activation capping prevents it |
| [Measuring Agent Autonomy](papers/measuring-agent-autonomy.md) | Anthropic, Feb 2026 | Real-world usage shows deployment overhang; experienced users monitor more |

---

## Course Syllabus

A 12-week research seminar covering:

| Weeks | Module |
|-------|--------|
| 1-2 | Foundations of LLM Conversations |
| 3-4 | Personality in LLMs |
| 5-6 | Agentic Behavior & Autonomy |
| 7-8 | Multi-Agent Conversational Dynamics |
| 9-10 | State of the Art Review |
| 11-12 | Applied Research Project |

See [syllabus/syllabus.md](syllabus/syllabus.md) for full details.

---

## Contributing

### Adding Papers
1. Submit via issue or pull request
2. Include: title, authors, year, arXiv/DOI link, relevance statement
3. Papers will be triaged into priority levels
4. Reviewed papers get summary files

### Paper Review Template
```markdown
# [Paper Title]
## [Source/Organization] ([Date])

**Link:** [URL]

### Summary
[2-3 paragraph summary]

### Key Findings
- Finding 1
- Finding 2

### Implications for OurBrood
[Relevance to project]

### Questions for Discussion
1. Question 1
2. Question 2
```

---

## Resources

See [papers/resources.md](papers/resources.md) for:
- Research lab links (Anthropic, OpenAI, DeepMind, Meta)
- ArXiv search queries
- Benchmarks & datasets
- Key conferences (NeurIPS, ICML, ACL, etc.)
- Agent frameworks & interpretability tools

---

## About OurBrood

OurBrood is an initiative of **OMSK Social Club** exploring the intersection of AI systems and social dynamics. This research repository supports the development of educational content and practical applications.

---

*Last updated: March 2026*