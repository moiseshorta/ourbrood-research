# VoxRole: A Comprehensive Benchmark for Evaluating Speech-Based Role-Playing Agents

## Metadata
- **Authors:** Weihao Wu, Liang Cao, Xinyu Wu, Zhiwei Lin, Rui Niu, Jingbei Li, Zhiyong Wu
- **Link:** https://arxiv.org/abs/2509.03940
- **Submitted:** September 2025
- **Status:** Reviewed
- **arXiv ID:** 2509.03940
- **Venue:** arXiv preprint

## Abstract Summary

This paper introduces VoxRole, the first comprehensive benchmark specifically designed for evaluating speech-based Role-Playing Conversational Agents (RPCAs). The benchmark addresses a critical gap in RPCA research: existing work focuses almost exclusively on textual modality, overlooking paralinguistic features essential for conveying character emotions and shaping vivid identities—intonation, prosody, and rhythm in speech.

The benchmark comprises 13,335 multi-turn dialogues totaling 65.6 hours of speech from 1,228 unique characters across 261 movies. The authors propose a two-stage automated pipeline that aligns movie audio with scripts and employs an LLM to build multi-dimensional character profiles.

## Key Contributions

### 1. Speech-Based Role-Playing Evaluation
- First benchmark specifically designed for speech-based RPCAs
- Addresses paralinguistic features: intonation, prosody, rhythm
- Long-term persona consistency in speech modality

### 2. VoxRole Dataset
- 13,335 multi-turn dialogues
- 65.6 hours of speech
- 1,228 unique characters
- 261 movies as source material
- Multi-dimensional character profiles

### 3. Automated Pipeline
- Stage 1: Audio-script alignment
- Stage 2: LLM-based character profile construction

### 4. Multi-Dimensional Evaluation
- Persona consistency metrics
- Speech feature analysis
- Character fidelity assessment

## Relevance to OurBrood

### Voice-Based Facilitation (Mother.py)
**Directly Relevant:** OurBrood's Mother.py uses ElevenLabs TTS for voice-based psychodrama facilitation. VoxRole provides:

1. **Paralinguistic Framework:** Understanding how intonation, prosody, and rhythm convey character—critical for a facilitator persona
2. **Long-Term Consistency:** Methods for maintaining persona across extended sessions—essential for psychodrama sessions that may last hours
3. **Multi-Dimensional Profiling:** LLM-based character profile construction could inform Mother.py's persona design

### Facilitator vs Character Persona
**Important Distinction:** While VoxRole focuses on role-playing AS characters, the benchmark's evaluation methodology transfers to facilitator personas:
- Persona fidelity metrics apply to facilitator consistency
- Speech-based consistency extends to voice-based therapeutic agents
- Character profile construction informs facilitator persona development

### Safety for Voice Agents
**Psychodrama Considerations:**
- Paralinguistic features signal emotional safety (tone, pacing)
- Consistency in voice builds trust during facilitation
- Long-term persona stability prevents jarring user experiences

## Key Questions for Psychodrama Facilitation

1. **Voice Persona Fidelity:** How can Mother.py maintain consistent vocal characteristics (tone, pacing, warmth) across extended psychodrama sessions?

2. **Paralinguistic Emotional Cues:** What speech features signal safety, empathy, and attunement in therapeutic contexts? How do we measure these?

3. **Character vs Facilitator Profiles:** How does persona profile construction differ for facilitators (who guide) vs characters (who embody)?

4. **Long-Term Consistency:** How do we prevent persona drift in multi-session psychodrama facilitation? What's the equivalent of "long-term persona consistency" for therapeutic agents?

5. **Emotional Range:** VoxRole evaluates characters across emotional states—what's the appropriate emotional range for a psychodrama facilitator?

6. **User Experience Evaluation:** How do users perceive facilitator voice quality? What makes a voice persona feel "safe" for emotional exploration?

## Citation

```bibtex
@article{wu2025voxrole,
  title={VoxRole: A Comprehensive Benchmark for Evaluating Speech-Based Role-Playing Agents},
  author={Wu, Weihao and Cao, Liang and Wu, Xinyu and Lin, Zhiwei and Niu, Rui and Li, Jingbei and Wu, Zhiyong},
  journal={arXiv preprint arXiv:2509.03940},
  year={2025}
}
```

---

*Summary prepared for OurBrood course on LLM & Agentic Conversational SOTA research. Created March 2026.*