# MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents

**Authors:** Yiming Du, Bingbing Wang, Yang He, Bin Liang, Baojun Wang, Zhongyang Li, Lin Gui, Jeff Z. Pan, Ruifeng Xu, Kam-Fai Wong  
**Link:** https://arxiv.org/abs/2505.20231  
**Submitted:** May 2025 (v2 August 2025)

## Abstract

Modern task-oriented dialogue (TOD) systems increasingly rely on large language model (LLM) agents, leveraging Retrieval-Augmented Generation (RAG) and long-context capabilities for long-term memory utilization. However, these methods are primarily based on semantic similarity, overlooking task intent and reducing task coherence in multi-session dialogues. To address this challenge, we introduce MemGuide, a two-stage framework for intent-driven memory selection. (1) Intent-Aligned Retrieval matches the current dialogue context with stored intent descriptions in the memory bank, retrieving QA-formatted memory units that share the same goal. (2) Missing-Slot Guided Filtering employs a chain-of-thought slot reasoner to enumerate unfilled slots, then uses a fine-tuned LLaMA-8B filter to re-rank the retrieved units by marginal slot-completion gain. The resulting memory units inform a proactive strategy that minimizes conversational turns by directly addressing information gaps.

## Relevance to OurBrood

This paper is **highly relevant** for Mother's role as psychodrama facilitator:

1. **Intent-Driven Memory**: Mother's memory retrieval should match the *intent* of a psychodrama session, not just semantic similarity to past conversations.

2. **Multi-Session Continuity**: Visitors may return for multiple sessions. MemGuide addresses how to maintain coherence across sessions.

3. **Proactive Strategy**: Mother should proactively guide sessions toward meaningful exploration, not just react to visitor input.

4. **Slot-Filling for Psychodrama**: The "missing slot" concept applies to identifying unexplored aspects of a visitor's Crave or narrative.

## Key Innovation: Intent-Aligned Memory

```
Standard RAG Approach:
Query → Semantic Similarity → Top-K Documents

MemGuide Approach:
Query → Intent Classification → Intent-Matched Memories → Slot-Based Filtering → Ranked Memories
```

## Application to Mother Agent

### Intent Classification for Psychodrama
- What is Mother trying to achieve in this moment?
  - Deepening exploration of a theme
  - Building rapport
  - Identifying the Crave
  - Facilitating catharsis
  - Closing a session gracefully

### Slot-Filling for Visitor Journey
- What do we know about this visitor?
- What haven't we explored yet?
  - [ ] Family context
  - [ ] Work/life balance
  - [ ] Recent transitions
  - [ ] Core desires
  - [ ] Fears and obstacles

### Proactive Strategy
MemGuide's "minimize conversational turns by directly addressing information gaps" aligns with efficient psychodrama facilitation.

## Key Questions

1. **Intent Taxonomy**: What intents are relevant to psychodrama facilitation?

2. **Slot Design**: What information slots are most valuable for Mother to fill about each visitor?

3. **Memory Format**: Should Mother store memories in QA format for better intent alignment?

4. **Proactivity Balance**: How proactive should Mother be vs. following visitor's lead?

## Benchmark: MS-TOD

MemGuide introduces MS-TOD, a multi-session TOD benchmark with:
- 132 diverse personas
- 956 task goals
- Annotated intent-aligned memory targets

Could inspire a similar benchmark for psychodrama facilitation evaluation.

## Results Summary

- Task success rate: 88% → 99% (+11%)
- Dialogue length reduced by 2.84 turns
- Maintains parity with single-session benchmarks

This demonstrates that intent-driven memory significantly improves multi-session task completion.

---

*Added to OurBrood research: March 2026*