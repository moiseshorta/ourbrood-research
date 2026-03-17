# OMSK Student Skills Roadmap for On-Prem Build

**Goal:** Migrate OurBrood from cloud APIs to local, open-source, on-prem stack

---

## Current State (Baseline)

| Component | Current | Target |
|-----------|---------|--------|
| LLM | Cloud APIs (ElevenLabs) | Local models |
| RAG | ElevenLabs KB | Local vector DB |
| Voice | ElevenLabs TTS/Cloning | Local vocoder |
| Memory | Plaintext + KB sync | Local embedding DB |
| APIs | Mixed third-party | On-prem only |

---

## Architecture Migration

### Current Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│  mother.py                    brood.py                              │
│  ─────────────                ─────────                            │
│  • ElevenLabs TTS             • ElevenLabs TTS                      │
│  • ElevenLabs KB sync         • Stateless                            │
│  • Cloud LLM                  • Cloud LLM                           │
│  • Plaintext memory           • Session-scoped                      │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  Cloud APIs     │
                    │  (ElevenLabs)   │
                    └─────────────────┘
```

### Target Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│  mother.py                    brood.py                              │
│  ─────────────                ─────────                            │
│  • Local TTS (vocoder)        • Local TTS                           │
│  • Local embedding DB         • Session-scoped                      │
│  • Local LLM (vLLM/TGI)       • Local LLM                           │
│  • FAISS/Milvus retrieval     • No persistent memory                │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  On-Prem Stack  │
                    │  (Docker/GPU)   │
                    └─────────────────┘
```

---

## Skills Required by Domain

### 1. LLM & Model Engineering

**Current:** Cloud LLM via ElevenLabs Conversational AI  
**Target:** Local LLM with fine-tuning for psychodrama facilitation

#### Skills Needed
- PyTorch/Transformers fundamentals
- Model loading and serving (vLLM, TGI)
- Fine-tuning techniques:
  - LoRA/QLoRA for efficient adaptation
  - Quantization for GPU memory optimization
- Prompt engineering and guardrails
- Evaluation benchmarks for persona consistency

#### Tasks
1. Compare pretrained models vs. fine-tuned for facilitator persona
2. Implement persona drift monitoring
3. Optimize for latency < 500ms
4. Create evaluation benchmarks from research papers

#### Relevant Papers
- Persona Selection Model — Persona enactment from pretraining
- Assistant Axis — Persona drift detection
- VoxRole — Voice persona consistency metrics

---

### 2. RAG & Data

**Current:** ElevenLabs Knowledge Base API  
**Target:** Local vector database with curated knowledge

#### Skills Needed
- Text cleaning and chunking strategies
- Embedding generation (sentence-transformers, OpenAI embeddings)
- Vector databases:
  - FAISS for prototyping
  - Milvus for production
- Retrieval tuning and evaluation
- Domain knowledge curation (psychodrama, facilitation)

#### Tasks
1. Extract knowledge base from ElevenLabs
2. Build local embedding pipeline
3. Implement intent-driven retrieval (MemGuide framework)
4. Create evaluation for retrieval quality

#### Relevant Papers
- HiMem — Hierarchical memory (Episodic → Semantic → Procedural)
- MemGuide — Intent-driven retrieval with slot-filling
- TiMem — Temporal consolidation for 90s recap

---

### 3. Speech & Audio

**Current:** ElevenLabs real-time TTS + voice cloning  
**Target:** Local vocoder with voice cloning

#### Skills Needed
- Voice cloning toolchains:
  - VITS, Bark, Tortoise TTS
  - Coqui TTS
- Vocoder fundamentals
- Dataset creation and labeling
- Real-time TTS latency tuning
- Audio I/O and basic DSP
- Optional: ASR for speech-to-text

#### Tasks
1. Clone Mother and Brood voices locally
2. Integrate real-time vocoder into pipeline
3. Optimize for < 200ms latency
4. Create voice persona profiles from research

#### Relevant Papers
- τ-Voice — Full-duplex voice benchmarks
- VoxRole — Paralinguistic persona metrics

---

### 4. Systems & MLOps

**Current:** Running on cloud infrastructure  
**Target:** On-prem GPU deployment

#### Skills Needed
- NVIDIA GPU setup:
  - CUDA drivers
  - cuDNN
  - Container runtime
- Containerization:
  - Docker for service isolation
  - Docker Compose for orchestration
- Model serving:
  - vLLM for LLM inference
  - TGI (Text Generation Inference)
- API services:
  - FastAPI for REST endpoints
  - gRPC for low-latency communication
- Monitoring:
  - Prometheus/Grafana for metrics
  - Logging pipeline
- CI/CD for model updates
- On-prem security:
  - Network isolation
  - PII handling
  - Consent management

#### Tasks
1. Set up Docker environment
2. Deploy vLLM for LLM serving
3. Integrate vocoder as container service
4. Create monitoring dashboard
5. Document deployment procedures

---

### 5. Application & Integration

**Current:** ourbrood.py runs both agents with cloud APIs  
**Target:** Local agents with on-prem stack

#### Skills Needed
- Agent orchestration:
  - State machines for Mother
  - Wake-word handling for Brood
- Conversation memory:
  - Persistent storage for Mother
  - Session-scoped for Brood
- Low latency streaming I/O
- Error handling and resilience
- Stability testing

#### Tasks
1. Modify ourbrood.py for local LLM
2. Implement hierarchical memory for Mother
3. Create wake-word detection pipeline
4. Build resilience (reconnect, fallback)
5. Test for 3+ hour session stability

#### Relevant Papers
- LTS-VoiceAgent — Listen-Think-Speak pipeline
- VoiceAgentRAG — Fast/Slow Thinker pattern
- Autonomous Memory Agents — Self-directed memory

---

### 6. UX/Research & Ethics

**Current:** Museum exhibition context  
**Target:** Same, with on-prem privacy

#### Skills Needed
- User study design
- Qualitative evaluation methods
- Accessibility considerations
- Consent and PII handling
- Documentation

#### Tasks
1. Design evaluation for on-prem vs. cloud
2. Create user study protocol
3. Document consent flow
4. Accessibility audit

#### Relevant Papers
- Disempowerment Patterns — Safety framework
- Human-AI Sovereignty — Power dynamics
- Participatory AI Art Findings — Exhibition context

---

## Implementation Priorities

### P0: Proof of Concept (March-May)
- Local LLM serving (vLLM)
- Basic RAG with FAISS
- Simple TTS integration
- Docker environment

### P1: Feature Parity (June-August)
- Voice cloning for Mother/Brood
- Hierarchical memory
- Intent-driven retrieval
- Latency optimization

### P2: Production Hardening (September-November)
- Monitoring and logging
- Error handling
- Stability testing
- User studies

### P3: Exhibition Ready (December-February)
- Accessibility features
- Documentation
- Deployment automation
- Final evaluation

---

## Reference Architecture

```python
# Target pipeline for local on-prem

# MOTHER.PY (Local)
MIC → RESAMPLE → WHISPER (ASR) → LOCAL_LLM → VOCODER → SPEAKER
                              ↓
                        FAISS RETRIEVAL
                              ↓
                     HIERARCHICAL MEMORY
                              ↓
                      MOTHER_MEMORY.TXT

# BROOD.PY (Local)
MIC → RESAMPLE → WHISPER (ASR) → LOCAL_LLM → VOCODER → SPEAKER
                              ↓
                      WAKE_WORD_DETECTOR
                              ↓
                      SESSION_SCOPED_ONLY
```

---

## Resources

- `papers/IMPLEMENTATION_GUIDE.md` — Prioritized tasks
- `INTEGRATION.md` — Research integration
- `syllabus/architecture.md` — Current architecture
- OMSK Roadmap Document — This document

---

*Skills roadmap for student teams building on-prem OurBrood*