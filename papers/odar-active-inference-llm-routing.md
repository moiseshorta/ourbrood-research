# ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference

## Metadata
- **Authors:** Siyuan Ma, Bo Gao, Xiaojun Jia, Simeng Qin, Tianlin Li, Ke Ma, Xiaoshuang Jia, Wenqi Ren, Yang Liu
- **Link:** https://arxiv.org/abs/2502.07745
- **Submitted:** February 2026
- **Status:** To review
- **arXiv ID:** 2502.07745

## Abstract Summary

The paper proposes ODAR-Expert, an adaptive routing framework for LLM reasoning that optimizes the accuracy-efficiency trade-off via principled resource allocation. ODAR uses a difficulty estimator grounded in amortized inference and active inference principles to dynamically route reasoning tasks to appropriate model capabilities. The framework addresses the problem of "overthinking" where models waste compute on easy problems.

## Key Contributions

1. **Active Inference for Routing:** Novel application of active inference to the model routing problem. The framework treats routing decisions as Bayesian inference over task difficulty, selecting models that minimize expected free energy.

2. **Difficulty Estimation:** Introduces a principled approach to estimating task difficulty using amortized inference. Unlike heuristic routing, this provides calibrated uncertainty estimates.

3. **Accuracy-Efficiency Trade-off:** Demonstrates significant efficiency gains while maintaining accuracy:
   - Reduces unnecessary compute on easy tasks
   - Routes complex tasks to larger/expert models
   - Provides principled stopping criteria

4. **Principled Resource Allocation:** Grounds routing decisions in Bayesian decision theory rather than arbitrary thresholds or heuristics.

## Relevance to OurBrood Course

### Active Inference & Cognitive Architectures (Priority Focus)
- **Direct application of active inference:** This paper demonstrates how active inference can be applied to practical LLM deployment problems.
- **Cognitive architecture relevance:** The routing mechanism mirrors biological systems that allocate cognitive resources based on expected information gain.
- **Uncertainty quantification:** Active inference provides natural uncertainty estimates that inform routing decisions.

### Multi-Agent Governance
- The routing problem generalizes to multi-agent systems where tasks must be allocated across agents with different capabilities.
- Principles developed here could inform multi-agent coordination strategies.

### Alignment & Safety
- Efficient resource allocation prevents waste and reduces environmental impact
- Proper routing prevents models from being applied to tasks beyond their capability, improving safety

## Key Questions for Discussion

1. How does the active inference framework compare to reinforcement learning approaches for routing?
2. Can the difficulty estimation be extended to multi-modal inputs?
3. How do we calibrate the expected free energy estimates for novel task distributions?
4. What is the relationship between routing confidence and task safety (routing critical tasks)?
5. How does this approach scale to hierarchical model systems?

## Connection to Active Inference Framework

The paper connects to core active inference concepts:

- **Expected Free Energy (EFE):** The routing decision minimizes EFE, balancing information gain (exploration) with task utility (exploitation)
- **Precision-weighted inference:** Difficulty estimates are precision-weighted, reflecting uncertainty
- **Amortized inference:** Uses learned mappings from task features to routing decisions

## Open Problems

- **Novel tasks:** How does difficulty estimation perform on out-of-distribution tasks?
- **Hierarchical routing:** Can the framework be extended to multi-level routing hierarchies?
- **Learning to route:** How should routing policies be learned and updated?
- **Safety constraints:** How do we incorporate safety constraints into the routing objective?

## Related Work

- **Mixture of experts:** ODAR provides principled routing compared to learned routing in MoE
- **Adaptive computation time:** Active inference provides theoretical grounding for when to stop computing
- **Model cascades:** Routing decisions in sequential model application
- **Budget-aware inference:** Efficient resource allocation under constraints

## Citation

```bibtex
@article{ma2026odar,
  title={ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference},
  author={Ma, Siyuan and Gao, Bo and Jia, Xiaojun and Qin, Simeng and Li, Tianlin and Ma, Ke and Jia, Xiaoshuang and Ren, Wenqi and Liu, Yang},
  journal={arXiv preprint arXiv:2502.07745},
  year={2026}
}
```

---

*Summary prepared for OurBrood course on LLM & Agentic Conversational SOTA research.*