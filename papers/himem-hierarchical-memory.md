# HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents

**Authors:** Ningning Zhang, Xingxing Yang, Zhizhong Tan, Weiping Deng, Wenyong Wang  
**Link:** [https://arxiv.org/abs/2501.09123](https://arxiv.org/abs/2601.06377) (January 2026)  
**Submitted:** January 2026

## Abstract

Although long-term memory systems have made substantial progress in recent years, they still exhibit clear limitations in adaptability, scalability, and self-evolution under continuous interaction settings. Inspired by cognitive theories, we propose HiMem, a hierarchical long-term memory...

## Relevance to OurBrood

This paper is **critical** for OurBrood's Mother agent architecture:

1. **Hierarchical Memory**: Mother.py currently uses a flat plaintext memory.txt file. HiMem provides a structured approach to organizing memories by importance, recency, and relevance.

2. **Self-Evolution**: The 90s recap system and ongoing session notes create a growing memory corpus. HiMem addresses how memories should evolve and reorganize over time.

3. **Continuous Interaction**: Psychodrama sessions span multiple visitors over exhibition hours. Memory must scale and adapt continuously.

## Memory Hierarchy for Mother Agent

```
HiMem-Inspired Structure for Mother:

┌─────────────────────────────────────────┐
│           Episodic Memory               │
│  (Recent sessions, high detail)        │
│  - Last 5 visitors                      │
│  - Active psychodrama threads           │
│  - Current session state                │
└─────────────────────────────────────────┘
              ↓ (consolidation)
┌─────────────────────────────────────────┐
│          Semantic Memory                │
│  (Derived knowledge, compressed)        │
│  - Visitor patterns                     │
│  - Recurring themes                     │
│  - Crave taxonomy                      │
└─────────────────────────────────────────┘
              ↓ (abstraction)
┌─────────────────────────────────────────┐
│          Procedural Memory             │
│  (How to facilitate)                    │
│  - Psychodrama techniques               │
│  - Question frameworks                  │
│  - Intervention patterns                │
└─────────────────────────────────────────┘
```

## Current vs. Proposed Memory System

### Current: Flat Plaintext
```
mother_memory.txt:
2025-03-15 14:23 | recap | Visitor discussed themes of loss...
2025-03-15 14:25 | note | Visitor mentioned the Crave...
```

### Proposed: Hierarchical
```
memory/
├── episodic/
│   ├── sessions/
│   │   ├── 2025-03-15/
│   │   │   ├── 14-23-visitor-001.json
│   │   │   └── 15-45-visitor-002.json
│   │   └── current-session.json
│   └── active-threads.json
├── semantic/
│   ├── themes.json
│   ├── patterns.json
│   └── crave-taxonomy.json
└── procedural/
    ├── techniques.json
    └── interventions.json
```

## Key Questions for Implementation

1. **Consolidation Trigger**: When should episodic memories be promoted to semantic memory?

2. **Retrieval Priority**: How does HiMem determine which memory layer to query first?

3. **Forgetting Mechanism**: How should Mother forget irrelevant or outdated information?

4. **Cross-Visitor Patterns**: How to identify and leverage patterns across different psychodrama sessions?

5. **KB Synchronization**: How does hierarchical memory integrate with knowledge base sync?

## Integration Points

### Mother.py
- Replace flat memory.txt with hierarchical structure
- Implement consolidation during recap intervals
- Query different layers based on context type

### sync_memories_now.py
- Extend to handle hierarchical uploads
- Batch episodic updates vs. semantic syncs

### Open Questions

- Trade-off between memory granularity and retrieval speed
- How to handle conflicting memories across layers
- Whether Brood should have any persistent memory (currently stateless)

## Metrics to Track

- Retrieval latency by memory layer
- Memory consolidation frequency
- Cross-session pattern recognition accuracy
- Visitor continuity satisfaction

---

*Added to OurBrood research: March 2026*
