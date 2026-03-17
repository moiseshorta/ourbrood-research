# Our Br00d Seminar — Summer Semester 2026

**Institution:** Hochschule München University of Applied Sciences (HM) / Hochschule für Musik und Theater München (HMTM)  
**Course:** AI in Culture and Arts (AICA) — Project Workshop  
**Module:** Wahlpflichtmodul MUC.DAI  
**ECTS:** 6 credits  
**Workload:** 72 contact hours + 108h self-study  

---

## Workshop Dates

### Day 1 (25 March) — Introduction to Our Br00d: Concept, System, and Challenges

| Time | Session | Topics |
|------|---------|--------|
| 10:00-10:30 | Welcome & Introduction | Workshop structure, project-based workflow |
| 10:30-11:20 | Introduction to "Our Br00d" | Concept, implementation, role-play environments, installation setting |
| 11:20-11:30 | Break | — |
| 11:30-12:00 | Get to know each other | Background, expectations, interests |
| 12:00-13:00 | Lunch | — |
| 13:00-13:50 | Introduction to System Architecture | LLM dialogue systems, RAG, voice synthesis, API dependencies |
| 13:50-14:30 | Coffee break | — |
| 14:30-15:30 | Development Challenges | Scope, feasibility, technical requirements |
| 15:30-16:00 | Discussion | First ideas, key insights, Q&A |

### Day 2 (26 March) — Team Formation and Project Planning

| Time | Session | Topics |
|------|---------|--------|
| 10:00-10:15 | Recap of Day 1 | — |
| 10:15-11:00 | Tasks & Technical Clarifications | Open discussion, feasibility |
| 11:00-11:15 | Break | — |
| 11:15-12:00 | Team Formation | Interdisciplinary teams (3-4 students), competencies, interests |
| 12:00-13:00 | Lunch | — |
| 13:00-14:00 | Task Selection | Teams choose challenges |
| 14:00-14:15 | Break | — |
| 14:15-15:15 | Project Planning | Problem definition, research, timeline |
| 15:15-16:00 | Team Presentations | Approach, steps until May, feedback |

---

## Instructors

- **Mariya Dzhimova** — Workshop facilitation
- **Penny Rafferty** — Our Br00d concept, development challenges
- **Moisés Horta Valenzuela** — System architecture, AI development

---

## Project Roadmap: Local On-Prem Model

### Goal

Build an on-prem interactive art installation with two AI agents:
- **M0ther**: Wise, multilingual caregiver that responds on call
- **Brood**: Maturing, babbling entity in a metal oloid that evolves over narrative timeline

Public interaction alternates between:
- Facilitated high-intensity roleplays
- Quieter viewing periods

### Current Tech (Baseline)

| Component | Current Implementation |
|-----------|----------------------|
| LLMs | Contextual understanding, character-consistent dialogue |
| RAG | Curated literature/traits database, hallucination reduction |
| Voice | ElevenLabs voice cloning + real-time TTS |
| APIs | Mixed third-party dependencies |

### Primary Objective

**Migrate to local, open-source, on-prem stack:**
- Remove external dependencies
- Lower latency
- Improve privacy
- Increase customization/control

### Student Team Skills Required

#### LLM & Model Engineering
- PyTorch/Transformers
- Fine-tuning (LoRA/QLoRA)
- Quantization & optimization
- Prompt/guardrails
- Evaluation & benchmarks

#### RAG & Data
- Text cleaning & chunking
- Embedding generation
- Vector databases (FAISS/Milvus)
- Retrieval tuning & evaluation
- Domain knowledge curation

#### Speech & Audio
- Voice-cloning toolchains and vocoders
- Dataset creation/labeling
- Real-time TTS latency tuning
- Audio I/O & basic DSP
- Optional ASR familiarity

#### Systems & MLOps
- NVIDIA GPU setup (CUDA/drivers)
- Containerization (Docker)
- Model serving (vLLM/TGI)
- API services (FastAPI/gRPC)
- Batching & orchestration
- Monitoring/logging
- CI/CD
- On-prem security & privacy

#### Application & Integration
- Agent orchestration/state machines
- Conversation memory & logging
- Low latency streaming I/O
- Error handling
- Resilience & stability testing

#### UX/Research & Ethics
- User studies & qualitative evaluation
- Accessibility
- Consent/PII handling
- Clear documentation

---

## Development Challenges

From Day 1 presentation:

1. **LLM Migration** — Local models vs. cloud APIs
2. **RAG Implementation** — Knowledge base curation and retrieval
3. **Voice Synthesis** — Local TTS with distinct agent voices
4. **Latency Optimization** — Real-time interaction requirements
5. **Memory Architecture** — Persistent (M0ther) vs. stateless (Brood)
6. **Agent Coordination** — Wake-word switching, stereo separation
7. **Privacy & Security** — On-prem requirements, consent handling

---

## Course Deliverables

### Assessment

- **Project Presentation** — Final colloquium (end of semester)
- **Group Paper** — 10 pages documenting project evolution
- **Artifacts** — Working code, documentation, demonstrations

### Timeline

- **March 25-26**: Workshop kickoff, team formation
- **March-May**: Independent team work
- **May**: Second meeting (preliminary results)
- **End of semester**: Final colloquium

---

## Connection to OurBrood Research Repository

This seminar aligns with the ourbrood-research repository:

| Seminar Focus | Research Domain | Papers |
|---------------|-----------------|--------|
| LLM dialogue systems | Persona & Character Modeling | 13 papers |
| RAG for knowledge base | Memory Architecture | 4 papers |
| Voice synthesis | Voice Agents | 8 papers |
| Agent coordination | Multi-Agent Dynamics | 14 papers |
| Privacy & consent | Safety & Governance | 6 papers |

Students can reference the research integration in `INTEGRATION.md` and `papers/IMPLEMENTATION_GUIDE.md`.

---

## Resources

- [ourbrood-research](https://github.com/moiseshorta/ourbrood-research) — Research repository
- [ourBrood](https://github.com/moiseshorta/ourBrood) — Code repository
- `syllabus/architecture.md` — System architecture documentation
- `INTEGRATION.md` — Research integration for implementation
- `papers/IMPLEMENTATION_GUIDE.md` — Prioritized implementation tasks

---

*Course materials for Our Br00d Summer Semester 2026, Hochschule München*