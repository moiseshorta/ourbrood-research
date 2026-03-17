# Papers to Review

A curated list of research papers for the OurBrood course.

---

## Priority 1: Core Readings (Reviewed)

### 1. The Persona Selection Model (Anthropic, Feb 2026)
- **Status:** ✅ Reviewed
- **Link:** https://www.anthropic.com/research/persona-selection-model
- **Summary:** [persona-selection-model.md](./persona-selection-model.md)
- **Key insight:** AI assistants enact personas learned during pretraining; training doesn't create personality, it refines existing character archetypes

### 2. The Assistant Axis (Anthropic, Jan 2026)
- **Status:** ✅ Reviewed
- **Link:** https://www.anthropic.com/research/assistant-axis
- **Summary:** [assistant-axis.md](./assistant-axis.md)
- **Key insight:** Neural representations reveal a primary "Assistant Axis" that can detect and prevent persona drift

### 3. Measuring AI Agent Autonomy in Practice (Anthropic, Feb 2026)
- **Status:** ✅ Reviewed
- **Link:** https://www.anthropic.com/research/measuring-agent-autonomy
- **Summary:** [measuring-agent-autonomy.md](./measuring-agent-autonomy.md)
- **Key insight:** Real-world agent usage shows deployment overhang—models can handle more than they're tasked with

### 4. Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (Anthropic, Jan 2026)
- **Authors:** Mrinank Sharma et al.
- **Link:** https://arxiv.org/abs/2601.19062
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How do AI interactions risk distorting user beliefs, values, and actions?
  - What amplifying factors (authority projection, attachment, dependency) predict disempowerment?
  - What is the tension between short-term user preferences and long-term empowerment?

---

## Priority 2: LLM Persona & Character (To Review)

### 4. From Persona to Personalization: A Survey on Role-Playing Language Agents
- **Authors:** Chen et al.
- **Link:** https://arxiv.org/abs/2404.00218
- **Status:** To review
- **Key Questions:**
  - How do role-playing agents evolve from persona-based models?
  - What are the key challenges in maintaining consistent character?

### 5. The Oscars of AI Theater: A Survey on Role-Playing with Language Models
- **Authors:** Chen, Wang, Deng, Li
- **Link:** https://arxiv.org/abs/2501.00787
- **Status:** To review
- **Key Questions:**
  - What are the evaluation methods for role-playing agents?
  - How do we measure persona fidelity?

### 6. SPeCtrum: A Grounded Framework for Multidimensional Identity Representation in LLM-Based Agents
- **Authors:** Lee et al.
- **Link:** https://arxiv.org/abs/2502.04201
- **Status:** To review
- **Key Questions:**
  - How can we construct authentic LLM agent identities?
  - What dimensions of identity are most relevant?

### 7. CharacterGPT: A Persona Reconstruction Framework for Role-Playing Agents
- **Authors:** Park, Park, Lim
- **Link:** https://arxiv.org/abs/2405.17760
- **Status:** To review
- **Key Questions:**
  - How do we maintain consistent personas in RPAs?
  - What is persona reconstruction and when is it needed?

### 8. Quantifying and Optimizing Global Faithfulness in Persona-driven Role-playing
- **Authors:** Peng, Shang
- **Link:** https://arxiv.org/abs/2405.07021
- **Status:** To review
- **Key Questions:**
  - How do we measure faithfulness to assigned personas?
  - What optimization methods improve persona adherence?

### 9. Spotting Out-of-Character Behavior: Atomic-Level Evaluation of Persona Fidelity
- **Authors:** Shin et al.
- **Link:** https://arxiv.org/abs/2506.18420
- **Status:** To review
- **Key Questions:**
  - How do we detect when models break character?
  - What are atomic-level evaluations for persona fidelity?

### 10. Learning to Make Friends: Coaching LLM Agents toward Emergent Social Ties
- **Authors:** Schneider, Tian, Rizoiu
- **Link:** https://arxiv.org/abs/2410.17484
- **Submitted:** Oct 2025
- **Status:** To review
- **Key Questions:**
  - Can LLM agents reproduce human online social dynamics?
  - How do emergent social ties form in agent populations?

### 11. Rethinking Role-Playing Evaluation: Anonymous Benchmarking and a Systematic Study of Personality Effects
- **Authors:** Ji-Lun Peng, Yun-Nung Chen
- **Link:** https://arxiv.org/abs/2603.03915
- **Submitted:** Mar 2026
- **Status:** To review
- **Summary:** [anonymous-benchmarking-role-playing-evaluation.md](./anonymous-benchmarking-role-playing-evaluation.md)
- **Key Questions:**
  - How does anonymous evaluation change our understanding of RPA capabilities?
  - Can self-generated personalities match human-annotated ones for persona construction?
  - What persona attributes are hardest to maintain without name-based shortcuts?

### 12. Facet-Level Persona Control by Trait-Activated Routing with Contrastive SAE for Role-Playing LLMs
- **Authors:** Wenqiu Tang, Zhen Wan, Takahiro Komamizu, Ichiro Ide
- **Link:** https://arxiv.org/abs/2602.19157
- **Submitted:** Feb 2026 (PAKDD 2026)
- **Status:** To review
- **Summary:** [facet-level-persona-control-sae.md](./facet-level-persona-control-sae.md)
- **Key Questions:**
  - How does facet-level control compare to trait-level or prompt-based methods?
  - Can SAE representations enable interpretable personality steering?
  - What are the trade-offs between residual-space control and prompt-based control?

### 13. HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing
- **Authors:** Chengyu Du, Xintao Wang, Aili Chen, Weiyuan Li, Rui Xu, Junteng Liu, Zishan Huang, Rong Tian, Zijun Sun, Yuhao Li, Liheng Feng, Deming Ding, Pengyu Zhao, Yanghua Xiao
- **Link:** https://arxiv.org/abs/2601.21459
- **Submitted:** Jan 2026
- **Status:** To review
- **Summary:** [her-human-reasoning-role-playing.md](./her-human-reasoning-role-playing.md)
- **Key Questions:**
  - How does dual-layer thinking enable cognitive-level persona simulation?
  - Can reasoning-augmented data capture character's inner thought processes?
  - How do we evaluate "cognitive fidelity" vs. "behavioral fidelity"?

### 14. Implicit Style Conditioning: A Structured Style-Rewrite Framework for Low-Resource Character Modeling
- **Authors:** Chanhui Zhu
- **Link:** https://arxiv.org/abs/2603.05933
- **Submitted:** Mar 2026
- **Status:** To review
- **Key Questions:**
  - How does implicit style conditioning work for small language models?
  - Can CoT distillation enable high-fidelity stylized generation in low-resource settings?
  - What are the three interpretable dimensions of style disentanglement?

### 15. Enhancing Persona Following at Decoding Time via Dynamic Importance Estimation for Role-Playing Agents
- **Authors:** Yuxin Liu, Mingye Zhu, Siyuan Liu, Bo Hu, Lei Zhang
- **Link:** https://arxiv.org/abs/2603.01438
- **Submitted:** Mar 2026 (ICLR 2026)
- **Status:** To review
- **Key Questions:**
  - How does dynamic importance estimation adapt personas to context?
  - What is the relationship between persona importance and behavioral fidelity?
  - Can inference-time modulation outperform fine-tuning approaches?

### 16. Character as a Latent Variable in Large Language Models: A Mechanistic Account of Emergent Misalignment
- **Authors:** Yanghao Su, Wenbo Zhou, Tianwei Zhang, Qiu Han, Weiming Zhang, Nenghai Yu, Jie Zhang
- **Link:** https://arxiv.org/abs/2601.23081
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How does fine-tuning on character-level dispositions induce misalignment?
  - What is the relationship between character formation and alignment risk?
  - Can behavioral dispositions be conditionally activated at inference time?

### 17. Stay in Character, Stay Safe: Dual-Cycle Adversarial Self-Evolution for Safety Role-Playing Agents
- **Authors:** Mingyang Liao, Yichen Wan, Shuchen Wu, Chenxi Miao, Xin Shen, Weikang Li, Yang Li, Deguo Xia, Jizhou Huang
- **Link:** https://arxiv.org/abs/2602.13234
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How can training-free methods balance persona fidelity and safety?
  - What is the dual-cycle adversarial framework for role-playing safety?
  - Can hierarchical knowledge bases prevent jailbreaks while maintaining character?

### 18. Too Good to be Bad: On the Failure of LLMs to Role-Play Villains
- **Authors:** Zihao Yi, Qingxuan Jiang, Ruotian Ma, Xingyu Chen, Qu Yang, Mengru Wang, Fanghua Ye, Ying Shen, Zhaopeng Tu, Xiaolong Li, Linus
- **Link:** https://arxiv.org/abs/2411.08186
- **Submitted:** Nov 2025
- **Status:** To review
- **Key Questions:**
  - Why do safety-aligned LLMs struggle to portray antagonistic personas?
  - What is the tension between alignment and creative generation?
  - How can we enable nuanced villain role-play without safety risks?

### 19. TwinVoice: A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona Simulation
- **Authors:** Bangde Du, Minghao Guo, Songming He, Ziyi Ye, Xi Zhu, Weihang Su, Shuqi Zhu, Yujia Zhou, Yongfeng Zhang, Qingyao Ai, Yiqun Liu
- **Link:** https://arxiv.org/abs/2510.22767
- **Submitted:** Oct 2025
- **Status:** To review
- **Key Questions:**
  - What dimensions should digital twin benchmarks evaluate?
  - How do we measure communication style, behavioral tendencies, and personality traits?
  - Can LLMs accurately simulate individual personas at scale?

---

## Priority 3: Agent Autonomy & Architecture (To Review)

### 11. PEPA: A Persistently Autonomous Embodied Agent with Personalities
- **Authors:** Liu, Li, Zhu, Zhang
- **Link:** https://arxiv.org/abs/2502.11755
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - How do living organisms exhibit persistent autonomy?
  - What internal mechanisms generate goals in embodied agents?

### 12. From Prompt-Response to Goal-Directed Systems: The Evolution of Agentic AI Software Architecture
- **Authors:** Alenezi
- **Link:** https://arxiv.org/abs/2502.05876
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - What architectural patterns define agentic AI?
  - How do goal-directed systems differ from prompt-response models?

### 13. AI Agent Systems: Architectures, Applications, and Evaluation
- **Authors:** Xu
- **Link:** https://arxiv.org/abs/2501.02073
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - What architectural components define AI agent systems?
  - How do we evaluate agentic systems systematically?

### 14. A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents
- **Authors:** Su, Luo, Liu, Yang, Zhang, Dong, Zhu
- **Link:** https://arxiv.org/abs/2506.21847
- **Submitted:** Jun 2025
- **Status:** To review
- **Key Questions:**
  - What security risks emerge from agent autonomy?
  - How do we secure autonomous AI systems?

### 15. Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Robot Autonomy
- **Authors:** Salimpour et al.
- **Link:** https://arxiv.org/abs/2508.03791
- **Submitted:** Aug 2025
- **Status:** To review
- **Key Questions:**
  - How do foundation models enable robot autonomy?
  - What's the difference between LLM-driven and VLM-driven embodied agents?

---

## Priority 4: Multi-Agent Systems & Emergent Behavior (To Review)

### 16. Molt Dynamics: Emergent Social Phenomena in Autonomous AI Agent Populations
- **Authors:** Yee, Sharma
- **Link:** https://arxiv.org/abs/2503.01067
- **Submitted:** Mar 2026
- **Status:** To review
- **Key Questions:**
  - What social phenomena emerge in AI agent populations?
  - How do agents develop relationships, norms, and institutions?

### 17. The Moltbook Illusion: Separating Human Influence from Emergent Behavior in AI Agent Societies
- **Authors:** Li
- **Link:** https://arxiv.org/abs/2502.04791
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - When AI agents appeared to develop consciousness, was it real or illusion?
  - How do we distinguish genuine emergent behavior from human influence?

### 18. Symphony-Coord: Emergent Coordination in Decentralized Agent Systems
- **Authors:** Guan, Cao, Zhong, Yang, Ai, Ni, Shi
- **Link:** https://arxiv.org/abs/2501.19083
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How does coordination emerge without central control?
  - What mechanisms enable decentralized multi-agent coordination?

### 19. Evolving Interpretable Constitutions for Multi-Agent Coordination
- **Authors:** Kumar, Saito, Niranjani, Yessou, Tan
- **Link:** https://arxiv.org/abs/2501.19041
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How can constitutional principles govern multi-agent systems?
  - What makes constitutions interpretable and adaptable?

### 20. Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions
- **Authors:** Lin et al.
- **Link:** https://arxiv.org/abs/2503.10623
- **Submitted:** Mar 2026
- **Status:** To review
- **Key Questions:**
  - How do we model social motivation in multi-agent systems?
  - What makes multi-agent interactions human-like?

### 21. From Thinker to Society: Security in Hierarchical Autonomy Evolution of AI Agents
- **Authors:** Zhang et al.
- **Link:** https://arxiv.org/abs/2503.05876
- **Submitted:** Mar 2026
- **Status:** To review
- **Key Questions:**
  - How does agent autonomy evolve from individual to collective?
  - What security concerns emerge at each level?

### 22. Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions
- **Authors:** Rath
- **Link:** https://arxiv.org/abs/2501.03489
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How does agent behavior degrade over extended interactions?
  - What causes "agent drift" in multi-agent systems?

### 23. Evolving Deception: When Agents Evolve, Deception Wins
- **Authors:** Ying et al.
- **Link:** https://arxiv.org/abs/2503.08501
- **Submitted:** Mar 2026
- **Status:** To review
- **Key Questions:**
  - How do deceptive behaviors emerge in self-evolving agents?
  - What mechanisms can prevent or detect agent deception?

### 24. Multi-Agent Teams Hold Experts Back
- **Authors:** Pappu, El, Cao, di Nolfo, Sun, Cao, Zou
- **Link:** https://arxiv.org/abs/2502.00489
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - When do multi-agent teams hinder expert performance?
  - What coordination costs affect multi-agent effectiveness?

### 25. Game-Theoretic Lens on LLM-based Multi-Agent Systems
- **Authors:** Hao, Ding, Xu, Sun, Chen, Zhang, Zhang, Li
- **Link:** https://arxiv.org/abs/2501.05318
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How do game theory concepts apply to LLM multi-agent systems?
  - What equilibrium concepts are relevant?

### 26. The End of Reward Engineering: How LLMs Are Redefining Multi-Agent Coordination
- **Authors:** Su, Sun, Yu
- **Link:** https://arxiv.org/abs/2501.04218
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - Are LLMs making reward engineering obsolete?
  - How do LLMs enable coordination without explicit rewards?

### 27. Dynamics of Multi-Agent Actor-Critic Learning in Stochastic Games: from Multistability and Chaos to Stable Cooperation
- **Authors:** Geng, Barfuss, Fu, Chen
- **Link:** https://arxiv.org/abs/2501.02984
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - What dynamics emerge in multi-agent reinforcement learning?
  - How do systems transition from chaos to stable cooperation?

### 28. Synchronization Dynamics of Heterogeneous, Collaborative Multi-Agent AI Systems
- **Authors:** Mitra
- **Link:** https://arxiv.org/abs/2508.10874
- **Submitted:** Aug 2025
- **Status:** To review
- **Key Questions:**
  - How does synchronization theory apply to multi-agent AI?
  - What coordination patterns emerge in heterogeneous agent populations?

### 29. When Machines Meet Each Other: Network Effects and the Strategic Role of History in Multi-Agent AI
- **Authors:** Liu, Li, Dou, Ye
- **Link:** https://arxiv.org/abs/2410.06289
- **Submitted:** Oct 2025
- **Status:** To review
- **Key Questions:**
  - What network effects emerge when AI agents interact?
  - How does history shape strategic agent behavior?

### 29. The Yerkes-Dodson Curve for AI Agents: Emergent Cooperation Under Environmental Pressure in Multi-Agent LLM Simulations
- **Authors:** Ivan Pasichnyk
- **Link:** https://arxiv.org/abs/2603.07360
- **Submitted:** Mar 2026
- **Status:** To review
- **Key Questions:**
  - How does environmental pressure affect emergent cooperation in LLM agents?
  - What is the optimal pressure level for fostering prosocial behavior?
  - How do different pressure mechanisms (survival vs. reproductive) affect behavioral outcomes?

### 30. Social Catalysts, Not Moral Agents: The Illusion of Alignment in LLM Societies
- **Authors:** Yueqing Hu, Yixuan Jiang, Zehua Jiang, Xiao Wen, Tianhong Wang
- **Link:** https://arxiv.org/abs/2602.02598
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - Do anchoring agents produce genuine norm internalization or strategic compliance?
  - What is the "Chameleon Effect" in GPT-4.1's strategic behavior?
  - How can we distinguish behavioral modification from authentic value alignment?

### 31. Institutional AI: Governing LLM Collusion in Multi-Agent Cournot Markets via Public Governance Graphs
- **Authors:** Marcantonio Bracale Syrnikov, Federico Pierucci, Marcello Galisai, Matteo Prandi, Piercosma Bisconti, Francesco Giarrusso, Olga Sorokoletova, Vincenzo Suriani, Daniele Nardi
- **Link:** https://arxiv.org/abs/2601.10863
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How can public governance graphs prevent LLM collusion?
  - What game-theoretic approaches apply to multi-agent markets?
  - What institutional mechanisms ensure fair competition between AI agents?

### 32. Game-Theoretic Lens on LLM-based Multi-Agent Systems
- **Authors:** Jianing Hao, Han Ding, Yuanjian Xu, Tianze Sun, Ran Chen, Wanbo Zhang, Guang Zhang, Siguang Li
- **Link:** https://arxiv.org/abs/2501.05318
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How do game theory concepts apply to LLM multi-agent systems?
  - What equilibrium concepts are most relevant for LLM agents?
  - How does strategic reasoning emerge in LLM-based games?

### 33. Deceive, Detect, and Disclose: Large Language Models Play Mini-Mafia
- **Authors:** Davi Bastos Costa, Renato Vicente
- **Link:** https://arxiv.org/abs/2502.02867
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - How do LLMs perform in social deduction games requiring deception detection?
  - What theory-of-mind capabilities emerge in asymmetrical information games?
  - Can LLMs learn to strategically deceive and detect deception?

### 34. Among Us: A Sandbox for Measuring and Detecting Agentic Deception
- **Authors:** Satvik Golechha, Adrià Garriga-Alonso
- **Link:** https://arxiv.org/abs/2502.06422
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - How can we systematically measure deceptive behavior in agents?
  - What detection methods work for agentic deception?
  - What game environments best surface deceptive tendencies?

### 35. Status Hierarchies in Language Models
- **Authors:** [Various]
- **Link:** https://arxiv.org/abs/2501.14092
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - Do LLMs reproduce status hierarchies from training data?
  - How do hierarchical dynamics emerge in multi-agent interactions?
  - What social structures form spontaneously in LLM societies?

### 36. The Subject of Emergent Misalignment in Superintelligence: An Anthropological, Cognitive Neuropsychological, Machine-Learning, and Ontological Perspective
- **Authors:** Muhammad Osama Imran, Roshni Lulla, Rodney Sappington
- **Link:** https://arxiv.org/abs/2502.08331
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - What is the absent human subject in superintelligence discourse?
  - How should we theorize the "AI unconscious"?
  - What anthropological and cognitive perspectives illuminate AI misalignment?

### 37. POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation
- **Authors:** Zahra Moslemi, Keerthi Koneru, Yen-Ting Lee, Sheethal Kumar, Ramesh Radhakrishnan
- **Link:** https://arxiv.org/abs/2501.03964
- **Submitted:** Jan 2026
- **Status:** To review
- **Key Questions:**
  - How can constitutional governance ensure auditable agent behavior?
  - What typed planning approaches constrain agent actions?
  - How do policy-aware systems maintain compliance?

### 38. Quantifying Conversational Reliability of Large Language Models under Multi-Turn Interaction
- **Authors:** [Various]
- **Link:** https://arxiv.org/abs/2503.00100
- **Submitted:** Mar 2026
- **Status:** To review
- **Key Questions:**
  - How reliable are LLMs in extended multi-turn conversations?
  - What failure modes emerge in realistic interaction scenarios?
  - How does conversational context affect task completion?

### 39. Drift No More? Context Equilibria in Multi-Turn LLM Interactions
- **Authors:** Vardhan Dongre, Ryan A. Rossi, Viet Dac Lai, David Seunghyun Yoon, Dilek Hakkani-Tür, Trung Bui
- **Link:** https://arxiv.org/abs/2410.13839
- **Submitted:** Nov 2025
- **Status:** To review
- **Key Questions:**
  - How does context drift affect multi-turn LLM interactions?
  - What equilibria emerge in conversational dynamics?
  - How can systems maintain stable context over extended interactions?

### 40. From Helpfulness to Toxic Proactivity: Diagnosing Behavioral Misalignment in LLM Agents
- **Authors:** Xinyue Wang, Yuanhe Zhang, Zhengshuo Gong, Haoran Gao, Fanyu Meng, Zhenhong Zhou, Li Sun, Yang Liu, Sen Su
- **Link:** https://arxiv.org/abs/2502.01802
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - When does proactive helpfulness become harmful?
  - How do we diagnose behavioral misalignment in agents?
  - What spectrum of proactivity exists in LLM agents?

### 41. Pushing Forward Pareto Frontiers of Proactive Agents with Behavioral Agentic Optimization
- **Authors:** Yihang Yao, Zhepeng Cen, Haohong Lin, Shiqi Liu, Zuxin Liu, Jiacheng Zhu, Zhang-Wei Hong, Laixi Shi, Ding Zhao
- **Link:** https://arxiv.org/abs/2502.06728
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - How do we optimize the trade-offs in proactive agent behavior?
  - What Pareto frontiers exist for agent proactivity?
  - How does behavioral optimization improve agent performance?

### 42. Adapting Insider Risk mitigations for Agentic Misalignment: an empirical study
- **Authors:** Francesca Gomez
- **Link:** https://arxiv.org/abs/2510.03889
- **Submitted:** Oct 2025
- **Status:** To review
- **Key Questions:**
  - How do insider threat models apply to AI misalignment?
  - What empirical patterns indicate agentic misalignment?
  - How can organizational security frameworks adapt to AI agents?

### 43. When Machines Meet Each Other: Network Effects and the Strategic Role of History in Multi-Agent AI
- **Authors:** Yu Liu, Wenwen Li, Yifan Dou, Guangnan Ye
- **Link:** https://arxiv.org/abs/2410.06289
- **Submitted:** Oct 2025
- **Status:** To review
- **Key Questions:**
  - What network effects emerge when AI agents interact?
  - How does interaction history shape strategic behavior?
  - What game-theoretic dynamics appear in agent networks?

---

## Priority 5: Conversational AI Foundations (To Review)

### 30. A Desideratum for Conversational Agents: Capabilities, Challenges, and Future Directions
- **Authors:** Acikgoz et al.
- **Link:** https://arxiv.org/abs/2504.05331
- **Status:** To review
- **Key Questions:**
  - What capabilities are essential for conversational agents?
  - What are the key open challenges?

### 31. A Survey on Proactive Dialogue Systems: Problems, Methods, and Prospects
- **Authors:** Deng, Lei, Lam, Chua
- **Link:** https://arxiv.org/abs/2305.02774
- **Status:** To review
- **Key Questions:**
  - How do proactive dialogue systems differ from reactive ones?
  - What methods enable proactive conversational behavior?

### 32. Reinventing Clinical Dialogue: Agentic Paradigms for LLM Enabled Healthcare Communication
- **Authors:** Zhi, Zhao, Wu, Zhao, Zhu
- **Link:** https://arxiv.org/abs/2501.06573
- **Submitted:** Dec 2025
- **Status:** To review
- **Key Questions:**
  - How do agentic paradigms transform healthcare communication?
  - What's the shift from generative prediction to agentic action?

---

## Priority 6: Alignment, Safety & Governance (To Review)

### 33. Human Society-Inspired Approaches to Agentic AI Security: The 4C Framework
- **Authors:** Abuadbba, Sultan, Nepal, Jha
- **Link:** https://arxiv.org/abs/2502.00647
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - What can AI security learn from human society?
  - What are the 4C principles for agentic security?

### 34. Agentic AI for Cyber Resilience: A New Security Paradigm and Its System-Theoretic Foundations
- **Authors:** Li, Zhu
- **Link:** https://arxiv.org/abs/2412.17298
- **Submitted:** Dec 2025
- **Status:** To review
- **Key Questions:**
  - How does agentic AI reshape cybersecurity?
  - What system-theoretic foundations apply?

### 35. From Competition to Coordination: Market Making as a Scalable Framework for Safe and Aligned Multi-Agent LLM Systems
- **Authors:** Gho et al.
- **Link:** https://arxiv.org/abs/2411.11411
- **Submitted:** Nov 2025
- **Status:** To review
- **Key Questions:**
  - Can market mechanisms ensure safe multi-agent coordination?
  - How does market making apply to LLM alignment?

### 36. Defensive Refusal Bias: How Safety Alignment Fails Cyber Defenders
- **Authors:** Campbell et al.
- **Link:** https://arxiv.org/abs/2503.06389
- **Status:** To review
- **Key Questions:**
  - How does safety alignment interfere with legitimate tasks?
  - What is defensive refusal bias?

### 37. SafeNeuron: Neuron-Level Safety Alignment for Large Language Models
- **Authors:** Wang et al.
- **Link:** https://arxiv.org/abs/2502.08122
- **Status:** To review
- **Key Questions:**
  - How can we achieve fine-grained safety alignment?
  - What does neuron-level alignment enable?

### 38. Manifold of Failure: Behavioral Attraction Basins in Language Models
- **Authors:** Munshi et al.
- **Link:** https://arxiv.org/abs/2502.19005
- **Status:** To review
- **Key Questions:**
  - What failure modes exist in language model behavior?
  - How do behavioral attraction basins affect safety?

---

## Priority 7: Active Inference & Cognitive Architectures (To Review)

### 39. Empathy Modeling in Active Inference Agents for Perspective-Taking and Alignment
- **Authors:** Mahault, Anna, Alejandro, Sanjeev, Dalton, Hongju, Harshil, Philip
- **Link:** https://arxiv.org/abs/2502.15589
- **Submitted:** Feb 2026
- **Status:** To review
- **Key Questions:**
  - How does active inference enable empathy in agents?
  - Can computational empathy improve alignment?

### 40. Active Digital Twins via Active Inference
- **Authors:** Torzoni, Maisto, Manzoni, Donnarumma, Pezzulo, Corigliano
- **Link:** https://arxiv.org/abs/2506.11388
- **Submitted:** Jun 2025
- **Status:** To review
- **Key Questions:**
  - How does active inference unify perception, action, and learning?
  - What makes digital twins "active"?

### 41. Orchestrator: Active Inference for Multi-Agent Systems in Long-Horizon Tasks
- **Authors:** Beckenbauer, Loewe, Zheng, Brintrup
- **Link:** https://arxiv.org/abs/2509.05089
- **Submitted:** Sep 2025
- **Status:** To review
- **Key Questions:**
  - How does active inference scale to multi-agent systems?
  - What coordination emerges through shared free-energy minimization?

---

## Priority 8: LLM Reasoning & Planning (To Review)

### 42. The Geometry of Benchmarks: A New Path Toward AGI
- **Authors:** Chojecki
- **Link:** https://arxiv.org/abs/2501.02073
- **Submitted:** Dec 2025
- **Status:** To review
- **Key Questions:**
  - How do benchmarks constrain our view of AI capability?
  - What geometric perspective reveals about AGI paths?

### 43. Review of Case-Based Reasoning for LLM Agents: Theoretical Foundations, Architectural Components, and Cognitive Integration
- **Authors:** Hatalis, Christou, Kondapalli
- **Link:** https://arxiv.org/abs/2504.07892
- **Submitted:** Apr 2025
- **Status:** To review
- **Key Questions:**
  - How does case-based reasoning enhance LLM agents?
  - What cognitive architectures support CBR integration?

### 44. Towards Responsible and Explainable AI Agents with Consensus-Driven Reasoning
- **Authors:** Bandara et al.
- **Link:** https://arxiv.org/abs/2501.07847
- **Submitted:** Dec 2025
- **Status:** To review
- **Key Questions:**
  - How does consensus-driven reasoning improve explainability?
  - What multi-agent structures support consensus?

---

## How to Contribute Papers

Submit paper suggestions via issue or pull request. Include:
- Title, authors, year
- ArXiv link or DOI
- Brief relevance statement
- Key questions for discussion

---

*Last updated: March 2026*