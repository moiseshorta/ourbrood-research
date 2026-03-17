# MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents

## Metadata
- **Authors:** Yiming Du, Bingbing Wang, Yang He, Bin Liang, Baojun Wang, Zhongyang Li, Lin Gui, Jeff Z. Pan, Ruifeng Xu, Kam-Fai Wong
- **Link:** https://arxiv.org/abs/2505.20231
- **Submitted:** May 2025 (v2 August 2025)
- **Status:** Reviewed
- **arXiv ID:** 2505.20231
- **Venue:** arXiv preprint

## Abstract Summary

This paper introduces MemGuide, a two-stage framework for intent-driven memory selection in goal-oriented multi-session dialogue. The framework addresses a key challenge: existing LLM agents using RAG and long-context capabilities rely primarily on semantic similarity for memory retrieval, overlooking **task intent** and reducing coherence in multi-session dialogues.

MemGuide introduces:
1. **Intent-Aligned Retrieval:** Matches current dialogue context with stored intent descriptions
2. **Missing-Slot Guided Filtering:** Uses chain-of-thought reasoning to identify information gaps

The paper also introduces MS-TOD, the first multi-session task-oriented dialogue benchmark with 132 diverse personas, 956 task goals, and annotated intent-aligned memory targets.

**Results:** MemGuide raises task success rate from 88% to 99% and reduces dialogue length by 2.84 turns in multi-session settings.

## Key Contributions

### 1. Intent-Driven Memory Selection
- Memory retrieval based on task intent, not just semantic similarity
- QA-formatted memory units organized by shared goals
- Proactive strategy that minimizes conversational turns

### 2. Two-Stage Framework
**Stage 1: Intent-Aligned Retrieval**
- Match dialogue context with intent descriptions in memory bank
- Retrieve memory units sharing the same goal

**Stage 2: Missing-Slot Guided Filtering**
- Chain-of-thought slot reasoner enumerates unfilled slots
- Fine-tuned LLaMA-8B filter re-ranks by marginal slot-completion gain
- Resulting units inform proactive strategy

### 3. MS-TOD Benchmark
- First multi-session task-oriented dialogue benchmark
- 132 diverse personas
- 956 task goals
- Intent-aligned memory targets
- Supports multi-session task completion evaluation

### 4. Performance Gains
- Task success: 88% → 99%
- Dialogue length: reduced by 2.84 turns
- Parity with single-session benchmarks

## Relevance to OurBrood

### Multi-Session Psychodrama Facilitation

**Mother.py facilitates psychodrama sessions that may span multiple conversations.** This creates specific memory and coherence challenges:

### 1. Session Continuity
Psychodrama is not a single-session activity. Users may:
- Return days/weeks later to continue exploration
- Reference characters or scenarios from previous sessions
- Build upon insights from past role-plays

**MemGuide's Intent-Driven Approach:**
- Store session content organized by exploration goals, not just semantic similarity
- Retrieve relevant past session material based on current intent
- Maintain continuity across sessions

### 2. Goal-Oriented Facilitation
Unlike casual conversation, psychodrama has goals:
- Explore particular emotional themes
- Try on alternate selves
- Work through conflicts with real people

**MemGuide's Goal Structure:**
- Intent-aligned memory enables goal-aware retrieval
- Slot-based filtering identifies what's been explored vs. unexplored
- Proactive strategy addresses information gaps

### 3. Persona Memory
Mother.py needs to remember:
- User's explored personas across sessions
- Which "alternate selves" have been tried
- What emotional territory has been covered
- User's stated goals for psychodrama work

**Memory Organization:**
- Intent: "Exploring conflict with partner"
- Slots: ["current relationship dynamic explored?", "alternate communication approaches tried?", "underlying needs identified?"]
- Retrieval based on current session intent, not just topic similarity

## Key Questions for Psychodrama Facilitation

### 1. Intent Modeling for Exploration
How do we represent "exploration intent" in psychodrama?
- Not task completion like MS-TOD
- What are the "slots" of psychodrama work?
- Example: "tried role-playing with mother?" "explored feelings of X?" "tested communication approach Y?"

### 2. Memory for Facilitation vs. Task Completion
MemGuide optimizes for task success. What's the equivalent for psychodrama?
- Insight generation?
- Emotional processing?
- Behavioral change intention?

### 3. Persona Consistency Across Sessions
How does Mother.py maintain:
- Consistent facilitator persona across sessions?
- Memory of user's previous personas and roles?
- Awareness of what emotional work has been done?

### 4. Proactive Facilitation
MemGuide uses missing slots for proactive strategy. How does Mother.py:
- Identify unexplored emotional territory?
- Suggest directions for psychodrama work?
- Balance user-led exploration with facilitator guidance?

### 5. Multi-Session Evaluation
How do we measure success in multi-session psychodrama?
- Not task completion
- Depth of exploration?
- User self-reported growth?
- Behavioral change in real life?

### 6. Memory Privacy and Boundaries
Psychodrama involves sensitive material:
- What should be stored vs. forgotten?
- How does user control memory retention?
- What happens when user wants to "start fresh"?

## Implementation Considerations

### Memory Structure for Psychodrama:
```json
{
  "session_id": "session_123",
  "intent": "exploring_relationship_conflict",
  "slots": {
    "theme_introduced": true,
    "emotions_expressed": true,
    "alternate_self_tried": false,
    "communication_approached": true,
    "action_plan": false
  },
  "key_memories": [
    "User described argument about finances",
    "Role-played saying 'I feel hurt when...'",
    "Explored mother's perspective"
  ],
  "user_goals": ["understand own feelings", "try new communication"],
  "boundaries": ["don't proactively bring up mother unless user initiates"]
}
```

### Proactive Facilitation Strategy:
1. **Intent Detection:** "What is user trying to explore this session?"
2. **Memory Retrieval:** Find relevant past sessions
3. **Slot Analysis:** What's been covered? What's missing?
4. **Proactive Prompt:** "Would you like to continue exploring X?"

## Technical Insights

### Intent-Aligned Retrieval:
- Stores intent descriptions with memory units
- Current context matched against intent, not just content
- Retrieves units sharing the same goal

### Missing-Slot Reasoning:
- Chain-of-thought identifies what's missing
- Marginal gain calculation prioritizes completion
- Fine-tuned filter for slot completion relevance

### Multi-Session Optimization:
- Minimizes turns by addressing gaps proactively
- Maintains goal tracking across sessions
- Preserves task coherence over time

## Limitations for Psychodrama Application

1. **Task vs. Exploration:** MemGuide designed for task completion, not open-ended exploration
2. **No Emotional Awareness:** Doesn't consider emotional weight of memories
3. **No Privacy Controls:** No mechanism for user to control what's remembered
4. **No Therapeutic Boundaries:** No framework for what should/shouldn't be surfaced
5. **Single User:** No multi-user privacy considerations

## Future Directions for OurBrood

1. **Psychodrama Memory Schema:** Define intent and slot structure for exploration sessions
2. **Emotional Memory Weighting:** Weight retrieval by emotional significance, not just intent match
3. **User-Controlled Memory:** Let users mark what to remember/forget
4. **Boundary-Aware Retrieval:** Respect therapeutic boundaries in proactive suggestions
5. **Multi-Session Evaluation:** Define success metrics beyond task completion

## Citation

```bibtex
@article{du2025memguide,
  title={MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents},
  author={Du, Yiming and Wang, Bingbing and He, Yang and Liang, Bin and Wang, Baojun and Li, Zhongyang and Gui, Lin and Pan, Jeff Z. and Xu, Ruifeng and Wong, Kam-Fai},
  journal={arXiv preprint arXiv:2505.20231},
  year={2025}
}
```

---

*Summary prepared for OurBrood course on LLM & Agentic Conversational SOTA research. Created March 2026.*