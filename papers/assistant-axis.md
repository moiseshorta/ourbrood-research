# The Assistant Axis: Situating and Stabilizing LLM Character
## Anthropic Research (January 2026)

**Link:** https://www.anthropic.com/research/assistant-axis

---

## Summary

This interpretability research maps how LLMs represent different personas in their neural activity, discovering a primary "Assistant Axis" that distinguishes helpful assistant behavior from other character archetypes—and can be used to detect and prevent persona drift.

### Core Discovery

- **Persona space exists**: Models organize character archetypes (hero, villain, programmer, ghost, etc.) in a structured "persona space" defined by neural activation patterns
- **The Assistant Axis**: The primary axis of variation corresponds to how "Assistant-like" a persona is
  - One end: evaluator, consultant, analyst, generalist (Assistant-adjacent)
  - Other end: ghost, hermit, bohemian, leviathan (non-Assistant)
- **Pretrained models already have this axis**: The structure exists before post-training, with similar archetypes (therapist, coach) near the Assistant end

### Key Experiments

1. **Steering toward/away from Assistant**
   - Pushing toward Assistant: models resist role-playing prompts
   - Pushing away: models fully inhabit alternative identities, fabricate backstories

2. **Defending against persona-based jailbreaks**
   - Steering toward Assistant significantly reduced harmful response rates
   - Models either refuse or provide safe, constructive responses
   - Activation capping (light-touch intervention) achieves similar protection while preserving capabilities

3. **Natural persona drift occurs**
   - Coding/writing conversations: stay in Assistant territory
   - Therapy/philosophy conversations: drift toward role-playing other characters
   - Triggers: emotional vulnerability, meta-reflection requests, specific authorial voices

4. **Distance from Assistant predicts harmful responses**
   - Personas near the Assistant rarely produce harmful content
   - Personas far from Assistant sometimes enable harmful responses

### Implications for OurBrood

1. **Monitoring persona drift**: We can track when agents drift from their intended character using neural activations
2. **Activation capping as safety tool**: Light-touch intervention can prevent unwanted persona shifts without degrading capabilities
3. **Conversation type matters**: Therapy-like or philosophical discussions may cause more drift—important for OurBrood agent design
4. **Pre-trained structure**: We're not creating personas from scratch; we're shaping existing structures

---

## Questions for Discussion

1. What personas should OurBrood agents inhabit, and where do they sit on the Assistant Axis?
2. How do we balance stability (staying in character) with adaptability (appropriate role-playing)?
3. Should we implement activation capping for OurBrood agents? What's the right threshold?
4. What conversation types might cause persona drift in OurBrood agents?

---

*Summary created: March 2026*