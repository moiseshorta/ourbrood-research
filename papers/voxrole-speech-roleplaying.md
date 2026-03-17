# VoxRole: A Comprehensive Benchmark for Evaluating Speech-Based Role-Playing Agents

**Authors:** Weihao Wu, Liang Cao, Xinyu Wu, Zhiwei Lin, Rui Niu, Jingbei Li, Zhiyong Wu  
**Link:** https://arxiv.org/abs/2509.03940 (September 2025)  
**Submitted:** September 2025

## Abstract

Role-Playing Conversational Agents (RPCAs) have gained significant attention for their ability to embody specific personas. However, existing benchmarks focus exclusively on text-based RPCAs, neglecting the paralinguistic features that define authentic role-play in speech: intonation, prosody, rhythm, and emotional expression. VoxRole introduces the first comprehensive benchmark for speech-based role-playing evaluation...

## Relevance to OurBrood

This paper is **directly relevant** to OurBrood's voice-based agent design:

1. **Speech-Based Role-Play**: Both Mother and Brood are voice agents that must embody personas through speech, not just text.

2. **Paralinguistic Features**: Mother's facilitation persona requires specific intonation, prosody, and emotional expression.

3. **Persona Consistency**: How to maintain consistent persona in voice across sessions.

4. **Multi-Modal Memory**: Voice + text memory - how should Mother store and retrieve paralinguistic information?

## Key Concepts

### Paralinguistic Features for Role-Play
- **Intonation**: Pitch patterns that convey emotional state
- **Prosody**: Rhythm, stress, and intonation patterns
- **Tempo**: Speaking rate variations for emphasis
- **Emotional Expression**: How voice conveys emotional states

### Evaluation Dimensions
1. **Persona Fidelity**: Does the voice match the persona?
2. **Long-Term Consistency**: Does persona remain stable across sessions?
3. **Emotional Range**: Can the agent express various emotions in character?
4. **Contextual Adaptation**: Does voice adapt to conversation context?

## Application to OurBrood

### Mother Voice Design
```
Mother Persona Voice Characteristics:
- Calm, measured tempo
- Warm, inviting intonation
- Emotional range: curious → empathetic → reflective
- Prosody for question-asking vs. reflection
```

### Brood Voice Design
```
Brood Persona Voice Characteristics:
- Quicker tempo (audience capturing)
- Playful, curious intonation
- Shorter utterances
- Minimal emotional depth (stateless)
```

## Key Questions

1. **Voice Cloning Consistency**: How does ElevenLabs voice cloning maintain persona across emotional states?

2. **Paralinguistic Memory**: Should Mother store paralinguistic cues (voice patterns) alongside text memories?

3. **Emotional Consistency**: How to ensure Mother's voice remains emotionally consistent during long sessions?

4. **Brood Activation Voice**: Should Brood's voice change when wake-word is activated vs. idle?

## Benchmark Methodology

VoxRole provides:
- Speech-based role-play datasets
- Evaluation metrics for paralinguistic features
- Persona consistency measures across time

## Implementation Considerations

- Integrate voice characteristic tracking into Mother's memory system
- Evaluate persona consistency using VoxRole metrics
- Consider storing voice embeddings alongside text memories
- Test emotional range during facilitator training

---

*Added to OurBrood research: March 2026*