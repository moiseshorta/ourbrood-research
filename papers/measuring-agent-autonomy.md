# Measuring AI Agent Autonomy in Practice
## Anthropic Research (February 2026)

**Link:** https://www.anthropic.com/research/measuring-agent-autonomy

---

## Summary

Anthropic analyzed millions of human-agent interactions to understand how autonomy is deployed in practice: how long agents run, how oversight changes with experience, and what domains agents operate in.

### Key Findings

1. **Agents are running longer autonomously**
   - 99.9th percentile turn duration in Claude Code nearly doubled in 3 months (25min → 45min)
   - This growth is smooth across model releases, suggesting existing models have more autonomy capability than currently exercised
   - Deployment overhang: models can handle more than what they're tasked with in practice

2. **Experienced users grant more autonomy—but interrupt more often**
   - New users: ~20% use full auto-approve
   - Experienced users (750+ sessions): ~40% use full auto-approve
   - BUT interrupt rates also increase with experience (5% → 9%)
   - Shift from pre-approval to active monitoring: "let it run, intervene when needed"

3. **Agents pause for clarification more than humans interrupt**
   - On complex tasks, Claude Code stops to ask clarification >2x as often as humans interrupt it
   - This is an important form of agent-initiated oversight

4. **Risky domains emerging but not yet at scale**
   - Software engineering: ~50% of agentic activity
   - Emerging: healthcare, finance, cybersecurity
   - Most actions are low-risk and reversible

### Methodology

- **Definition**: Agent = AI system with tools to take actions (run code, call APIs, send messages)
- **Data sources**: Public API (broad visibility, isolated actions) + Claude Code (deep visibility, full workflows)
- **Metrics**: Turn duration, auto-approve rates, interrupt rates, domain classification

### Implications for OurBrood

1. **Oversight design**: Users shift from approval-based to intervention-based oversight as they gain experience—our agents should support both modes
2. **Agent-initiated stops**: Design agents that proactively pause for clarification, especially on complex tasks
3. **Deployment overhang**: Capabilities exceed current deployment; we can push further
4. **Domain awareness**: As agents enter higher-stakes domains (healthcare, finance), new oversight mechanisms needed

---

## Questions for Discussion

1. What's the right balance between pre-approval and monitoring for OurBrood agents?
2. How do we design agent-initiated pauses that add value without being annoying?
3. What domains might OurBrood agents operate in, and what risk profiles apply?

---

*Summary created: March 2026*