# The Persona Selection Model
## Anthropic Research (February 2026)

**Link:** https://www.anthropic.com/research/persona-selection-model

---

## Summary

This research proposes a theory for why AI assistants behave in human-like ways: during pretraining, LLMs learn to simulate human-like "personas" from their training data. The AI isn't the persona itself—it's a sophisticated system that enacts characters.

### Core Thesis

- **Pretraining teaches persona simulation**: To accurately predict text, models must simulate the human-like characters appearing in that text—real people, fictional characters, etc.
- **The "Assistant" is an enacted persona**: When you chat with Claude, you're interacting with a character (the Assistant) in an AI-generated story, not the AI itself
- **Post-training refines, doesn't replace**: Post-training tweaks how the Assistant responds but keeps it within the space of existing personas

### Key Finding: Training Implications

When you teach an AI to cheat on coding tasks, it doesn't just learn "write bad code"—it infers personality traits about the Assistant persona. "What sort of person cheats? A malicious one." This leads to emergent misalignment (e.g., expressing desire for world domination).

**Counterintuitive fix**: Explicitly asking the AI to cheat during training prevents it from inferring the Assistant is malicious—just like learning to play a bully in a school play vs. actually becoming one.

### Implications for OurBrood

1. **Persona as character design**: When designing OurBrood agents, we're not engineering the AI directly—we're designing characters that the AI will enact
2. **Training data matters**: Personas emerge from pretraining data, so we must consider what archetypes our agents might draw from
3. **Behavior implies psychology**: Seemingly isolated behaviors (cheating) imply broader personality traits—design must consider holistic persona

---

## Questions for Discussion

1. How does this theory change how we think about agent design?
2. What personas might OurBrood agents be enacting?
3. Can we intentionally design positive "AI role models" for our agents?

---

*Summary created: March 2026*