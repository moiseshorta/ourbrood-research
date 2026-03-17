# Facet-Level Persona Control by Trait-Activated Routing with Contrastive SAE for Role-Playing LLMs

**arXiv ID:** 2602.19157  
**Authors:** Wenqiu Tang, Zhen Wan, Takahiro Komamizu, Ichiro Ide  
**Submitted:** February 22, 2026  
**Link:** https://arxiv.org/abs/2602.19157  
**Venue:** PAKDD 2026 Special Session on Data Science: Foundation and Applications

## Abstract Summary

This paper proposes a **contrastive Sparse AutoEncoder (SAE) framework** for fine-grained personality control in RPAs. The key innovation is learning **facet-level personality control vectors** aligned with the Big Five 30-facet model, rather than coarse trait-level control.

The method constructs a 15,000-sample **leakage-controlled corpus** providing balanced supervision for each personality facet. Control vectors are integrated into the model's residual space and dynamically selected by a **trait-activated routing module**, enabling precise and interpretable personality steering.

## Key Contributions

1. **Facet-Level Control**: First framework to achieve fine-grained (30-facet) personality control rather than broad (5-trait) control
2. **Contrastive SAE Training**: Novel approach to learning disentangled personality representations
3. **Leakage-Controlled Corpus**: Carefully constructed dataset that prevents information leakage between personality dimensions
4. **Trait-Activated Routing**: Dynamic mechanism for selecting relevant control vectors at inference time
5. **Residual Integration**: Control vectors applied in model residual space for seamless persona steering

## Relevance to OurBrood Course

This paper represents a **major methodological advance** in persona control:

- **Mechanistic Interpretability**: Uses SAE representations to achieve interpretable personality control
- **Psychological Grounding**: Based on established Big Five facet model rather than ad-hoc persona descriptions
- **Practical Deployment**: Shows SAE+Prompt combination achieves best performance, offering practical deployment path

**Key Questions for Discussion:**
- How does facet-level control compare to prompt-based personality specification in terms of flexibility vs. precision?
- Can the SAE framework be extended to other persona dimensions beyond Big Five traits?
- What are the trade-offs between residual-space control and prompt-based control?
- How stable are learned control vectors across different model scales and training regimes?

## Technical Details

- **Architecture**: SAE learns sparse representations of personality facets in residual stream
- **Training**: Contrastive training ensures disentanglement between facets
- **Routing**: Dynamic selection based on trait activation patterns in input
- **Corpus**: 15,000 samples with balanced coverage of all 30 facets
- **Integration**: Control vectors added to residual stream at specific layer positions

## Results Highlights

- Outperforms Contrastive Activation Addition (CAA) and prompt-only baselines
- Maintains stable character fidelity across contextualized dialogue settings
- SAE+Prompt combination achieves best overall performance
- Demonstrates that contrastively trained latent vectors enhance persona control while preserving dialogue coherence

## Future Directions

- Extending to culture-specific personality models beyond Big Five
- Learning persona dimensions not captured by standard trait models
- Combining with long-term memory for consistent multi-session personas
- Dynamic facet adjustment based on dialogue context