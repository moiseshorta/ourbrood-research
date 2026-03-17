# The Yerkes-Dodson Curve for AI Agents: Emergent Cooperation Under Environmental Pressure

**arXiv:** 2603.07360  
**Author:** Ivan Pasichnyk  
**Submitted:** March 7, 2026  
**Link:** https://arxiv.org/abs/2603.07360

---

## Abstract

Designing environments that maximize the rate of emergent behavior development in AI agents remains an open problem. This paper presents the first systematic study of stress-performance relationships in large language model (LLM) multi-agent systems, drawing an explicit parallel to the Yerkes-Dodson law from cognitive psychology. Using a grid-world survival arena, the authors conduct 22 experiments across four phases, varying environmental pressure through resource scarcity (upkeep cost) and reproductive competition (sexual selection).

---

## Key Findings

### 1. The Inverted-U Curve of Cooperation
The central finding is that cooperative behavior follows an inverted-U curve:
- **Peak cooperation**: 29 trades at medium pressure (upkeep=5)
- **Low pressure**: 8-12 trades
- **Extreme pressure**: Behavioral repertoire collapses to movement-only within 5-12 turns

This mirrors the Yerkes-Dodson law: moderate arousal optimizes performance, while both low and high arousal degrade it.

### 2. Behavioral Repertoire Collapse
Under extreme pressure:
- Agents' behavioral options narrow dramatically
- Movement-only behavior emerges within 5-12 turns
- Complex behaviors (trading, communication) become extinct

### 3. Sexual Selection vs. Survival Pressure
The paper distinguishes between two pressure mechanisms:
- **Survival pressure**: All agents compete for resources, some die
- **Sexual selection (softer pressure)**: All agents survive but not all reproduce

Key result: Sexual selection **eliminates inter-agent aggression entirely** and produces communicative behavior absent under survival pressure.

---

## Experimental Design

### Grid-World Survival Arena
- Multi-agent environment where LLM agents must survive
- Variables: resource scarcity (upkeep cost), reproductive competition
- 22 experiments across 4 phases
- Metrics: trade frequency, behavioral repertoire, communication patterns

### Pressure Mechanisms Tested
1. **Upkeep cost variation**: Controls survival pressure
2. **Sexual selection**: Controls reproductive competition without mortality

---

## Implications for Agent Autonomy

### 1. Environment Design as Curriculum
Environmental pressure calibration is a viable curriculum design strategy for LLM agent development. This suggests:
- Start with moderate pressure to encourage exploration
- Gradually adjust to optimize for specific behaviors
- Avoid extreme pressure that collapses behavioral diversity

### 2. Prosocial Behavior Emergence
The paper provides evidence that:
- Prosocial behavior is **situational**, not inherent
- Cooperation peaks under moderate environmental stress
- Both under- and over-stimulation reduce cooperative tendencies

### 3. Mechanism Selection Matters
Different pressure mechanisms produce qualitatively different behaviors:
- Survival pressure: Can induce aggression and behavioral narrowing
- Sexual selection: Promotes communication without aggression

---

## Relevance to OurBrood Course

### Primary Connections
1. **Agentic autonomy**: How environmental constraints shape goal-directed behavior
2. **Multi-agent coordination**: Emergence of cooperative vs. competitive strategies
3. **Behavioral degradation**: How pressure causes behavioral repertoire collapse

### Key Questions for Discussion
1. Can we design "optimal" pressure environments for developing beneficial emergent behaviors?
2. How do we balance exploration (low pressure) with task completion (higher pressure)?
3. What cognitive architectures might make Yerkes-Dodson dynamics more predictable?

### Research Extensions
- Apply to different agent architectures (not just LLM-based)
- Test in more complex environments (economic markets, social networks)
- Investigate individual differences in pressure response
- Map behavioral repertoire collapse to specific failure modes

---

## Methodological Notes

### Strengths
- First systematic application of Yerkes-Dodson to AI agents
- Clear experimental manipulation of pressure variables
- Multiple behavioral outcome measures

### Limitations
- Grid-world environment may not generalize to all domains
- Single LLM model tested (specific model not specified in abstract)
- Short-term interactions; extended dynamics not explored

---

## Related Work Connections

- **Agent drift literature**: Complements Rath (2026) on behavioral degradation
- **Emergent behavior**: Connects to Molt Dynamics (2026) on social phenomena
- **Cooperation dynamics**: Relates to institutional governance approaches (Syrnikov et al.)

---

## Quotable Insights

> "Cooperative behavior follows an inverted-U curve: trade interactions peak at 29 under medium pressure"

> "Sexual selection — a softer pressure mechanism — eliminates inter-agent aggression entirely and produces communicative behavior absent under survival pressure"

> "Environmental pressure calibration is a viable curriculum design strategy for LLM agent development"

---

## Future Directions

1. **Pressure-optimized training**: Develop agents that self-regulate pressure exposure
2. **Individual differences**: Why do some agents thrive under pressure while others collapse?
3. **Domain transfer**: Does the Yerkes-Dodson curve hold in creative tasks? Economic games?
4. **Long-term dynamics**: How do pressure responses evolve over extended interactions?

---

*Summary created: March 17, 2026*  
*For OurBrood Course: Agent Autonomy & Multi-Agent Systems*