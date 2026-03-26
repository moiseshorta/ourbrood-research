# LTS-VoiceAgent: A Listen-Think-Speak Framework for Efficient Streaming Voice Interaction via Semantic Triggering and Incremental Reasoning

**Authors:** Wenhao Zou, Yuwei Miao, Zhanyu Ma, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He, Jingwen Xu  
**Link:** https://arxiv.org/abs/2601.19952 (January 2026)  
**Submitted:** January 2026

## Abstract

Real-time voice agents require efficient streaming pipelines. LTS-VoiceAgent presents a Listen-Think-Speak framework with semantic triggering and incremental reasoning...

## Relevance to OurBrood

This paper addresses **streaming voice agent architecture** - the core of OurBrood's real-time interaction:

1. **Listen-Think-Speak Pipeline**: Directly maps to OurBrood's MIC → WEBSOCKET → LLM → TTS → SPEAKER flow.

2. **Semantic Triggering**: Brood's wake-word system is a form of semantic triggering. This paper provides formal framework.

3. **Incremental Reasoning**: Mother's responses during psychodrama benefit from incremental reasoning as visitor speaks.

## Key Architecture Pattern

```
LTS-VoiceAgent Pipeline:

┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│  Listen │ ──→ │  Think  │ ──→ │ Reason  │ ──→ │  Speak  │
│ (Stream)│     │ (Semantic│    │ (Incr.) │     │ (TTS)   │
│         │     │ Trigger)│     │         │     │         │
└─────────┘     └─────────┘     └─────────┘     └─────────┘
     ↑                              │
     │                              ↓
     └────────── Interrupt ←────────┘
```

## Application to OurBrood

### Semantic Triggering for Brood
- Wake-word "brood" is a semantic trigger
- Paper provides methods for more sophisticated triggering
- Could extend to topic-based activation beyond single phrase

### Incremental Reasoning for Mother
- Begin formulating response before visitor finishes speaking
- Update reasoning as new information arrives
- Handle interruptions gracefully

### Real-Time Considerations
- Latency budget for Listen → Think → Speak pipeline
- How incremental reasoning affects WebSocket streaming
- Trade-offs between response quality and latency

## Key Questions

1. **Trigger Design**: What semantic patterns should trigger Brood beyond the wake-word?

2. **Incremental vs. Complete Reasoning**: When should Mother wait for complete utterance vs. start reasoning incrementally?

3. **Interruption Handling**: How to handle visitor interruptions during Mother's reasoning phase?

4. **Streaming Latency**: What are acceptable latencies for semantic trigger detection?

## Streaming Architecture Comparison

```
Current OurBrood:
MIC → RESAMPLE → WEBSOCKET → [Full Utterance] → LLM → TTS

LTS-VoiceAgent Approach:
MIC → STREAM → [Semantic Detection] → Incremental Reasoning → TTS
         ↓              ↓
    [Wake-word]    [Begin thinking]
```

---

*Added to OurBrood research: March 2026*
