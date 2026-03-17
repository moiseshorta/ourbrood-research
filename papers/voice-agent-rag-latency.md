# VoiceAgentRAG: Solving the RAG Latency Bottleneck in Real-Time Voice Agents Using Dual-Agent Architectures

**Authors:** Jielin Qiu, Jianguo Zhang, Zixiang Chen, Liangwei Yang, Ming Zhu, Juntao Tan, Haolin Chen, Wenting Zhao, Rithesh Murthy, Roshan Ram, Akshara Prabhakar, Shelby Heinecke, Caiming Xiong, Silvio Savarese, Huan Wang  
**Link:** https://arxiv.org/abs/2603.08723 (March 2026)  
**Submitted:** March 2026

## Abstract

We present VoiceAgentRAG, an open-source dual-agent memory router that decouples retrieval from response generation. A background Slow Thinker...

## Relevance to OurBrood

This paper is **directly applicable** to OurBrood's dual-agent architecture:

1. **Dual-Agent Architecture**: OurBrood uses Mother (persistent) and Brood (stateless) agents. VoiceAgentRAG's Slow/Fast Thinker pattern mirrors this division.

2. **RAG Latency Problem**: Mother.py uses KB sync for memory retrieval. Real-time psychodrama requires sub-second response times that RAG typically violates.

3. **Memory Router Design**: The paper's approach to routing memory queries could improve Mother's recall_memories() function efficiency.

## Key Architecture Insight

```
VoiceAgentRAG Pattern:
┌─────────────────┐     ┌─────────────────┐
│   Fast Thinker  │     │   Slow Thinker  │
│  (Real-time)    │ ←── │  (Background)   │
│  Low Latency    │     │  Deep Retrieval │
└─────────────────┘     └─────────────────┘

OurBrood Parallel:
┌─────────────────┐     ┌─────────────────┐
│     Brood       │     │     Mother      │
│  (Session-only) │     │  (Persistent)   │
│  Fast Response  │     │  KB + Memory    │
│  Wake-word gate │     │  90s Recaps     │
└─────────────────┘     └─────────────────┘
```

## Key Questions for Implementation

1. **Decoupling Retrieval**: How does VoiceAgentRAG handle immediate queries while background retrieval is in progress?

2. **Memory Consistency**: How does the dual-agent pattern prevent stale reads when Mother is both serving and updating memory?

3. **Latency Targets**: What are the specific latency targets for voice agents that must respond within conversational gaps?

4. **Streaming RAG**: Can retrieval be streamed incrementally as in our current WebSocket pipeline?

## Potential Improvements for OurBrood

### Mother.py Enhancement
- Implement async memory retrieval that doesn't block TTS generation
- Route urgent queries through fast path while KB sync happens in background
- Consider "memory warming" for anticipated topics in psychodrama sessions

### Brood.py Consideration
- Stateless design already matches "Fast Thinker" pattern
- Wake-word window (15s) may need adjustment based on latency benchmarks

## Technical Details to Investigate

- Open-source implementation availability
- Integration with ElevenLabs WebSocket streaming
- Memory routing algorithm specifics
- Benchmark methodology for voice agent latency

---

*Added to OurBrood research: March 2026*