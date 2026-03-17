# τ-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains

**Authors:** Soham Ray, Keshav Dhandhania, Victor Barres, Karthik Narasimhan  
**Link:** https://arxiv.org/abs/2603.08723 (estimate from search)  
**Submitted:** March 2026

## Abstract

Full-duplex voice agents--systems that listen and speak simultaneously--are rapidly moving from research to production. However, existing evaluations address conversational dynamics and task completion in isolation. We introduce τ-Voice...

## Relevance to OurBrood

This paper is **highly relevant** to the OurBrood voice agent architecture:

1. **Full-Duplex Architecture**: OurBrood uses WebSocket streaming for real-time audio. Understanding how full-duplex systems handle simultaneous listening/speaking is critical for both Mother and Brood agents.

2. **Real-World Benchmarking**: The paper provides methodologies for evaluating voice agents in realistic scenarios, which applies to the exhibition context where OurBrood operates.

3. **Conversational Dynamics**: Mother.py's psychodrama facilitation requires managing complex turn-taking, interruption handling, and backchannel behaviors.

## Key Questions for Voice Agent Implementation

1. **Latency Budgets**: What are the acceptable latency bounds for full-duplex voice interaction in psychodrama contexts?

2. **Interruption Handling**: How should Mother handle interruptions during long-form psychodrama sessions vs. Brood's quick audience interactions?

3. **State Management**: How do full-duplex systems maintain coherent state across simultaneous input/output streams?

4. **Evaluation Metrics**: What metrics from τ-Voice apply to measuring Mother's facilitation effectiveness vs. Brood's audience capture rate?

## Architecture Implications

The full-duplex paradigm directly informs OurBrood's design:

```
Current Flow:
MIC → RESAMPLE → WEBSOCKET → LLM → PROMPT → TTS → KB → SPEAKER

Consideration:
- Can Mother process incoming audio while generating TTS output?
- How does the 90s recap system interact with full-duplex requirements?
- Should Brood's wake-word system operate differently in full-duplex mode?
```

## Next Steps

- [ ] Full paper review when available
- [ ] Benchmark OurBrood latency against τ-Voice metrics
- [ ] Test full-duplex mode with ElevenLabs WebSocket API
- [ ] Compare turn-taking strategies for Mother (facilitator) vs. Brood (capturing)

---

*Added to OurBrood research: March 2026*