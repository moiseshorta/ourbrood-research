# Rethinking Role-Playing Evaluation: Anonymous Benchmarking and a Systematic Study of Personality Effects

**arXiv ID:** 2603.03915  
**Authors:** Ji-Lun Peng, Yun-Nung Chen  
**Submitted:** March 4, 2026  
**Link:** https://arxiv.org/abs/2603.03915

## Abstract Summary

Current RPA evaluation suffers from a critical bias: models rely on memorized associations with famous character names rather than genuinely enacting personas. This paper proposes an **anonymous evaluation method** that removes name-based shortcuts, revealing that anonymization significantly degrades role-playing performance—confirming that character names carry implicit information not captured by persona descriptions alone.

The authors systematically compare personality augmentation strategies, finding that:
- Incorporating personality information consistently improves RPA performance
- **Self-generated personalities achieve performance comparable to human-annotated ones**
- This establishes both a fairer evaluation protocol and a scalable framework for robust RPAs

## Key Contributions

1. **Anonymous Benchmarking Protocol**: First systematic methodology to eliminate name-memorization bias in RPA evaluation
2. **Personality Augmentation Study**: Rigorous comparison of human-annotated vs. model-generated personality profiles
3. **Scalability Insight**: Self-generated personalities match human annotation quality, enabling cost-effective RPA construction
4. **Evaluation Framework**: Establishes fairer evaluation by disentangling memorization from persona enactment

## Relevance to OurBrood Course

This paper addresses a **foundational methodological concern** in persona research: how do we evaluate whether an LLM is truly "acting as" a persona versus simply retrieving cached knowledge about a famous character? The anonymous evaluation method should become standard practice for persona fidelity research.

**Key Questions for Discussion:**
- How does anonymous evaluation change our understanding of current RPA capabilities?
- What persona attributes are hardest to maintain without name-based shortcuts?
- Can we develop better persona descriptions that close the anonymous/non-anonymous performance gap?
- How does personality augmentation interact with different model scales and architectures?

## Methodology Notes

- Multiple benchmarks tested across anonymous/non-anonymous conditions
- Personality information derived from Big Five trait frameworks
- Self-generated personalities created via model introspection without human annotation
- Performance metrics include character fidelity, dialogue coherence, and behavioral consistency

## Future Directions

The paper opens paths toward:
- Persona descriptions that encode sufficient information without relying on fame
- Self-improving RPA systems that generate and refine their own personality profiles
- Evaluation metrics specifically designed for anonymous personas
- Understanding what makes certain characters "memorizable" vs. requiring genuine enactment