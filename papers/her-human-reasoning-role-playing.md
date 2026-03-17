# HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing

**arXiv ID:** 2601.21459  
**Authors:** Chengyu Du, Xintao Wang, Aili Chen, Weiyuan Li, Rui Xu, Junteng Liu, Zishan Huang, Rong Tian, Zijun Sun, Yuhao Li, Liheng Feng, Deming Ding, Pengyu Zhao, Yanghua Xiao  
**Submitted:** January 29, 2026 (v3: February 8, 2026)  
**Link:** https://arxiv.org/abs/2601.21459

## Abstract Summary

HER addresses a critical gap in LLM role-playing: while current models capture character tones and knowledge, they struggle to simulate **the inner thoughts behind character behaviors**. The paper proposes a unified framework for **cognitive-level persona simulation** through dual-layer thinking and reinforcement learning.

The key insight is distinguishing **characters' first-person thinking** from **LLMs' third-person thinking**, enabling more authentic cognitive simulation. The method constructs reasoning-augmented role-playing data via reverse engineering and builds human-aligned principles and reward models.

## Key Contributions

1. **Dual-Layer Thinking Framework**: Formal distinction between character's internal reasoning and model's simulation perspective
2. **Reasoning-Augmented Data**: Novel data construction via reverse engineering to capture cognitive processes
3. **Human-Aligned Reward Models**: Principles and rewards aligned with human perception of role-playing quality
4. **RL Training Pipeline**: Complete SFT + RL training framework based on Qwen3-32B
5. **Benchmark Results**: 30.26 improvement on CoSER benchmark, 14.97 gain on Minimax Role-Play Bench

## Relevance to OurBrood Course

This paper directly addresses **cognitive simulation** in role-playing—a core challenge for persona fidelity:

- **Beyond Surface Behavior**: Moves from "what would X say?" to "how would X think about this?"
- **Reasoning Transparency**: Provides interpretable reasoning traces for persona decisions
- **Training Methodology**: Demonstrates practical RL pipeline for cognitive-level persona training

**Key Questions for Discussion:**
- How does dual-layer thinking change our evaluation of persona consistency?
- Can the reasoning-augmented approach transfer to non-role-playing domains?
- What cognitive biases emerge when LLMs simulate first-person thinking?
- How do we evaluate "cognitive fidelity" vs. "behavioral fidelity"?

## Technical Approach

1. **Data Construction**: Reverse engineering from observed dialogue to reasoning traces
2. **Principle Design**: Human-aligned criteria for role-playing quality
3. **Reward Modeling**: Training rewards that capture both cognitive and behavioral aspects
4. **Model Architecture**: Based on Qwen3-32B with SFT + RL training

## Benchmark Performance

- **CoSER Benchmark**: +30.26 improvement over baseline
- **Minimax Role-Play Bench**: +14.97 gain
- Resources (datasets, principles, models) to be publicly released

## Future Directions

- Combining cognitive simulation with long-term memory
- Personalizing cognitive patterns beyond character archetypes
- Evaluating cognitive consistency across extended dialogues
- Multi-agent cognitive simulation for complex scenarios