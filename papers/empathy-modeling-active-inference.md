# Empathy Modeling in Active Inference Agents for Perspective-Taking and Alignment

## Metadata
- **Authors:** Albarracin Mahault, Mikeda Anna, Jimenez Rodriguez Alejandro, Namjoshi Sanjeev, Sakthivadivel Dalton, Pae Hongju, Shah Harshil, Wilson Philip
- **Link:** [https://arxiv.org/abs/2502.01947](https://arxiv.org/abs/2602.20936)
- **Submitted:** February 2026
- **Status:** To review
- **arXiv ID:** 2502.01947

## Abstract Summary

This paper introduces a computational framework for empathy modeling in active inference agents. The framework enables agents to understand and align with others' intentions through perspective-taking. The authors propose that computational empathy—implemented through active inference—can improve agent alignment by enabling agents to model and predict the goals, beliefs, and preferences of other agents (human or artificial).

## Key Contributions

1. **Empathy as Inference:** Formalizes empathy as Bayesian inference over others' mental states, grounded in the active inference framework. This provides a principled, quantitative approach to perspective-taking.

2. **Multi-Level Empathy:** Distinguishes between:
   - **Cognitive empathy:** Inferring others' beliefs and goals
   - **Affective empathy:** Inferring others' emotional states
   - **Behavioral empathy:** Predicting others' actions

3. **Perspective-Taking Architecture:** Proposes a nested inference architecture where agents maintain:
   - A model of their own generative model
   - A model of others' generative models
   - Beliefs about how others model them (recursive perspective-taking)

4. **Alignment Through Empathy:** Demonstrates that agents with empathy models can achieve better alignment with human intentions, as measured by task success and preference satisfaction.

5. **Computational Implementation:** Provides computational details for implementing empathy in active inference agents, including:
   - Hierarchical generative models
   - Variational inference procedures
   - Action selection with empathy-weighted objectives

## Relevance to OurBrood Course

### Empathy Modeling in Agents (Priority Focus)
- **Direct relevance:** This is core to understanding how agents can understand and align with human preferences.
- **Computational approach:** Provides mathematical grounding for empathy, moving beyond philosophical discussions.

### AI Safety & Alignment (Priority Focus)
- **Alignment mechanism:** Empathy modeling offers an alternative alignment approach—rather than external constraints, agents develop internal models of human preferences.
- **Robustness:** Perspective-taking can help agents generalize to novel situations by reasoning about human mental states.

### Active Inference & Cognitive Architectures
- **Natural extension:** Empathy fits naturally within the active inference framework as nested inference over generative models.
- **Cognitive plausibility:** Mirrors human empathy mechanisms—humans use theory of mind to understand others.

### Multi-Agent Governance
- **Multi-agent empathy:** The framework extends to agents modeling other agents, relevant for multi-agent coordination.
- **Trust building:** Empathy can serve as a foundation for trust between agents and between agents and humans.

## Key Questions for Discussion

1. How does empathy-based alignment compare to reward-based alignment? What are the trade-offs?
2. Can agents develop "super-human" empathy—predicting human preferences better than humans can themselves?
3. How do we prevent empathy from being used for manipulation rather than alignment?
4. What is the computational complexity of nested perspective-taking? When does it become intractable?
5. How does empathy interact with deception? Can empathic agents be deceived, or does empathy provide defense?

## Connection to Active Inference Framework

The paper is deeply grounded in active inference:

- **Generative Models:** Empathy involves constructing generative models of others' mental states
- **Variational Free Energy:** Perspective-taking minimizes surprise about others' behavior
- **Expected Free Energy:** Empathic action selection balances alignment with others' goals and information gain
- **Precision-weighting:** Beliefs about others' mental states are precision-weighted, reflecting uncertainty

## Open Problems

- **Ground truth:** How do we evaluate whether an agent's empathy model correctly captures human preferences?
- **Scalability:** Can the approach scale to complex, high-dimensional preference spaces?
- **Misaligned empathy:** What happens when agents develop accurate empathy models that are used for manipulation?
- **Cultural variation:** How do we handle different cultural models of empathy?

## Related Work

- **Theory of Mind:** AI agents modeling other agents' beliefs
- **Inverse Reinforcement Learning:** Inferring preferences from behavior
- **Constitutional AI:** Alternative approach to alignment
- **Value Learning:** General problem of inferring human values

## Citation

```bibtex
@article{mahault2026empathy,
  title={Empathy Modeling in Active Inference Agents for Perspective-Taking and Alignment},
  author={Mahault, Albarracin and Anna, Mikeda and Alejandro, Jimenez Rodriguez and Sanjeev, Namjoshi and Dalton, Sakthivadivel and Hongju, Pae and Harshil, Shah and Philip, Wilson},
  journal={arXiv preprint arXiv:2502.01947},
  year={2026}
}
```

---

*Summary prepared for OurBrood course on LLM & Agentic Conversational SOTA research.*
