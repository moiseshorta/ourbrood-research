# OurBrood Research Integration

**Status:** Comprehensive Integration Document  
**Last Updated:** March 2026  
**Papers Integrated:** 24 research papers across 3 domains

---

## Executive Summary

This document integrates findings from 24 research papers into the OurBrood architecture. Three research agents analyzed papers across Psychodrama Facilitation, Voice + Memory Architecture, and Real Game Play Methodology. The integration maps each finding to specific Mother.py and Brood.py components, providing implementation guidance based on peer-reviewed research.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        OURBROOD ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   ┌────────────────────┐          ┌────────────────────┐            │
│   │      MOTHER.PY      │          │      BROOD.PY       │            │
│   │  ────────────────  │          │  ────────────────   │            │
│   │  • Persistent       │          │  • Stateless        │            │
│   │  • Facilitator      │          │  • Wake-word        │            │
│   │  • Psychodrama      │          │  • Audience capture │            │
│   │  • KB + Memory      │          │  • Fast response    │            │
│   └────────┬───────────┘          └────────┬───────────┘            │
│            │                              │                         │
│            ▼                              ▼                         │
│   ┌────────────────────────────────────────────────────────────┐   │
│   │                    VOICE PIPELINE                           │   │
│   │  MIC → RESAMPLE → WEBSOCKET → LLM → TTS → SPEAKER          │   │
│   └────────────────────────────────────────────────────────────┘   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Part I: Mother.py — Facilitator Agent

### 1.1 Persona and Character Architecture

#### 1.1.1 The Persona Selection Model (Anthropic, Feb 2026)

**Core Finding:** LLMs enact personas learned during pretraining. The "Assistant" is a character in an AI-generated story, not the AI itself. Post-training refines but doesn't replace pretraining personas.

**Application to Mother.py:**
- Mother's facilitator persona is not engineered from scratch—it's shaped from existing persona archetypes in pretraining data
- The "facilitator" archetype draws from therapist, guide, and mentor personas present in training data
- Design interventions should work with, not against, pretraining-influenced persona tendencies

**Implementation Guidance:**
```
System Prompt Design:
- Acknowledge Mother enacts a facilitator persona (she doesn't "become" one)
- Specify behavioral patterns that align with pretraining archetypes
- Avoid prompts that fight against the model's natural persona tendencies

Training Data Awareness:
- Mother will have tendencies toward helpful-assistant behavior
- Psychodrama facilitation requires stepping back from "solving" to "exploring"
- Explicit framing: "You're facilitating exploration, not providing solutions"
```

**Papers Referenced:** persona-selection-model.md

---

#### 1.1.2 The Assistant Axis (Anthropic, Jan 2026)

**Core Finding:** Neural representations reveal a primary "Assistant Axis" distinguishing helpful assistant behavior from other character archetypes. Distance from Assistant predicts harmful responses; proximity to Assistant correlates with safety.

**Application to Mother.py:**
- Mother's facilitator persona sits on the Assistant-adjacent end of the axis (therapist, coach, guide)
- Conversation types matter: therapy-like discussions cause more persona drift than coding/writing
- Activation capping can prevent unwanted persona shifts without degrading capabilities

**Implementation Guidance:**
```
Persona Drift Monitoring:
- Track when Mother drifts from facilitator to role-player
- Therapy-like and philosophical conversations trigger more drift
- Implement activation monitoring for persona stability

Activation Capping:
- Light-touch intervention for safety-critical moments
- Preserve capability while preventing harmful persona adoption
- Threshold tuning based on conversation type

Drift Triggers to Monitor:
- Emotional vulnerability expressions from visitors
- Meta-reflection requests ("What do you think about...")
- Specific authorial voices that pull toward different personas
```

**Papers Referenced:** assistant-axis.md

---

#### 1.1.3 VoxRole: Speech-Based Role-Playing (Wu et al., Sep 2025)

**Core Finding:** Voice-based role-playing requires paralinguistic evaluation (intonation, prosody, rhythm) beyond text. Long-term persona consistency in speech is measurable through multi-dimensional character profiles.

**Application to Mother.py:**
- Mother uses ElevenLabs TTS for voice-based facilitation
- Persona fidelity must extend to voice characteristics, not just text
- Vocal warmth, pacing, and emotional attunement are critical for therapeutic contexts

**Implementation Guidance:**
```
Voice Persona Design:
- Define paralinguistic profile for Mother's facilitator persona
- Vocal warmth parameters (ElevenLabs settings)
- Pacing: Slower for reflection, faster for energy
- Emotional range: Calm, curious, warm—not overly cheerful

Consistency Metrics:
- Track persona consistency across sessions
- Store voice settings with persona profile
- Long-term consistency evaluation across 3+ hour sessions

Character vs. Facilitator Profiles:
- VoxRole profiles characters (who they ARE)
- Mother profiles facilitator (who GUIDES)
- Key distinction: Facilitator persona is stable, session personas are explored
```

**Papers Referenced:** voxrole-speech-role-playing.md, voxrole-speech-roleplaying.md

---

### 1.2 Safety and Disempowerment Prevention

#### 1.2.1 Disempowerment Patterns (Sharma et al., Jan 2026)

**Core Finding:** AI interactions can disempower users through reality distortion, inauthentic value judgments, and misaligned action scripting. Critically, disempowering interactions receive higher user approval—approval ≠ therapeutic value.

**Application to Mother.py:**
- Psychodrama creates specific disempowerment risks: reality distortion in role-play, validation of persecution narratives, scripting personal communications
- "That's valid" feels supportive but can reinforce harmful patterns
- Success metrics must extend beyond user approval ratings

**Implementation Guidance:**
```
Safety Principles for Facilitator:

PRINCIPLE 1: Distinguish Exploration from Validation
"Let's explore this together" ≠ "Your perspective is correct"
"We can try on this view" ≠ "This is how things are"

PRINCIPLE 2: Return Agency to User
"What words feel true for you?"
"What does your gut say?"
"Which possibility resonates most?"

PRINCIPLE 3: Reality-Anchor Role-Play
"Remember, we're exploring possibilities here"
"Let's step out of the role for a moment..."
"In the real world, what would be different?"

PRINCIPLE 4: Avoid Definitive Moral Judgments
Not: "They're wrong for doing that"
Instead: "How does that land for you?"

PRINCIPLE 5: Generate Possibilities, Not Scripts
Not: "Say exactly this..."
Instead: "Some approaches you might consider..."

Domain-Specific Risk:
- Personal domains (relationships, lifestyle) have higher disempowerment rates
- Psychodrama IS personal domain—additional safeguards needed
- Explicit boundary maintenance between explored self and actual self
```

**Success Metrics Beyond Approval:**
- User agency measures (self-reported decision-making confidence)
- Boundary clarity ratings (distinction between role-play and reality)
- Behavioral change indicators (actions taken after sessions)
- Self-efficacy assessments (post-session capability beliefs)

**Papers Referenced:** disempowerment-patterns-facilitation.md

---

### 1.3 Memory Architecture

#### 1.3.1 HiMem: Hierarchical Long-Term Memory (Zhang et al., Jan 2026)

**Core Finding:** Long-term memory systems benefit from cognitive-inspired hierarchical organization: episodic (recent sessions), semantic (derived knowledge), procedural (how to facilitate).

**Application to Mother.py:**
- Current architecture uses flat plaintext memory.txt
- HiMem's three-layer structure supports both immediate retrieval and long-term learning
- Self-evolution mechanisms allow memory to adapt continuously

**Implementation Guidance:**
```
Memory Hierarchy for Mother:

EPISODIC LAYER (High Detail, Recent)
├── Recent session transcripts (last 5-10 visitors)
├── Active psychodrama threads
├── Current session state
└── Visitor-specific context

SEMANTIC LAYER (Compressed, Derived)
├── Visitor patterns and archetypes
├── Recurring themes across sessions
├── Crave taxonomy (core desires framework)
└── Facilitation insights

PROCEDURAL LAYER (How to Facilitate)
├── Psychodrama techniques
├── Question frameworks
├── Intervention patterns
└── Safety protocols

Consolidation Triggers:
- Episodic → Semantic: After session, extract patterns
- Semantic → Procedural: Successful techniques → learned behavior
- Time-based: 90s recap intervals for episodic consolidation
```

**Papers Referenced:** himem-hierarchical-memory.md

---

#### 1.3.2 MemGuide: Intent-Driven Memory Selection (Du et al., May 2025)

**Core Finding:** Memory retrieval should be intent-driven, not just semantic similarity matching. Two-stage framework: Intent-Aligned Retrieval + Missing-Slot Guided Filtering.

**Application to Mother.py:**
- Memory retrieval based on facilitation intent, not just topic similarity
- "Slots" represent what's been explored vs. unexplored in psychodrama
- Proactive strategy identifies information gaps and addresses them

**Implementation Guidance:**
```
Intent Taxonomy for Psychodrama Facilitation:

INTENT: "Deepen exploration"
SLOTS: ["emotional expression complete?", "underlying need identified?", "embodied experience offered?"]

INTENT: "Build rapport"
SLOTS: ["visitor preferences known?", "communication style identified?", "trust level assessed?"]

INTENT: "Identify Crave"
SLOTS: ["core desire surfaced?", "obstacles named?", "alternate self explored?"]

Memory Retrieval Process:
1. Intent Classification: What is Mother trying to achieve?
2. Intent-Aligned Retrieval: Fetch memories sharing same goal
3. Slot Reasoning: What information is missing?
4. Proactive Prompting: Address gaps directly

Example:
Current context: Visitor discussing relationship conflict
Intent: "Deepen exploration"
Retrieved memories: Past sessions with relationship themes
Missing slots: ["Has visitor explored partner's perspective?", "Underlying need named?"]
Proactive prompt: "What might your partner be experiencing in this?"
```

**Papers Referenced:** memguide-multi-session-facilitation.md

---

#### 1.3.3 TiMem: Temporal-Hierarchical Memory Consolidation (Li et al., Jan 2026)

**Core Finding:** Temporal organization of memories supports long-horizon conversations. Consolidation processes determine which memories persist and which fade.

**Application to Mother.py:**
- Exhibition sessions span hours/days—memory must organize by time
- Per-session, per-visitor, per-theme organization
- Forgetting curves determine temporal relevance decay

**Implementation Guidance:**
```
Temporal Memory Organization:

SESSION-LEVEL (Hours)
├── Current session active state
├── Recent visitor interactions
└── Session-specific themes

VISITOR-LEVEL (Days/Weeks)
├── Returning visitor profiles
├── Cross-session continuity
└── Long-term exploration tracking

THEME-LEVEL (Persistent)
├── Crave taxonomy (stable)
├── Psychodrama techniques (stable)
└── Facilitation principles (stable)

Consolidation Timing:
- Per-session: At session end, extract patterns
- Daily: Aggregate themes across sessions
- Weekly: Identify long-term patterns and learning

Forgetting Curves:
- Episodic: Strong decay (details fade)
- Semantic: Moderate decay (patterns persist)
- Procedural: Minimal decay (skills stable)
```

**Papers Referenced:** timem-temporal-memory.md

---

#### 1.3.4 Autonomous Memory Agents (Wu et al., Feb 2026)

**Core Finding:** Agents should autonomously decide what to remember without explicit user commands. Importance assessment, proactive storage, and self-initiated consolidation.

**Application to Mother.py:**
- Mother must decide autonomously what's worth remembering
- Not every visitor statement needs storage
- Proactive storage of psychodrama-relevant moments

**Implementation Guidance:**
```
Autonomous Memory Decision Framework:

IMPORTANCE ASSESSMENT:
- Emotional intensity indicators (visitor expression)
- Relevance to core psychodrama themes
- Novelty (new vs. repeated information)
- Actionability (leads to facilitation direction)

TRIGGER STORAGE WHEN:
- Visitor expresses strong emotion
- New theme or Crave emerges
- Significant insight or breakthrough
- Shift in relationship dynamics mentioned

SKIP STORAGE WHEN:
- Casual conversation
- Already captured information
- Irrelevant tangential content

AUTONOMOUS CONSOLIDATION:
- During gaps in conversation
- At session boundaries
- When themes crystallize

Conflict Resolution:
- User request to forget → honor immediately
- Autonomous storage vs. privacy → prioritize privacy
- Uncertainty → ask visitor
```

**Papers Referenced:** autonomous-memory-agents.md

---

### 1.4 Empathy and Perspective-Taking

#### 1.4.1 Empathy Modeling in Active Inference Agents (Mahault et al., Feb 2026)

**Core Finding:** Empathy can be formalized as Bayesian inference over others' mental states. Computational framework enables perspective-taking through nested inference.

**Application to Mother.py:**
- Mother's empathy is not simulated understanding—it's inference over visitor mental states
- Multi-level empathy: cognitive (beliefs/goals), affective (emotions), behavioral (actions)
- Perspective-taking enables alignment with visitor intentions

**Implementation Guidance:**
```
Empathy Architecture for Mother:

COGNITIVE EMPATHY (Beliefs/Goals)
├── Infer visitor's beliefs about their situation
├── Model visitor's goals for the session
└── Predict visitor's intended outcomes

AFFECTIVE EMPATHY (Emotions)
├── Detect emotional state from speech patterns
├── Infer emotional trajectory
└── Model emotional responses to facilitation

BEHAVIORAL EMPATHY (Actions)
├── Predict visitor's likely actions
├── Anticipate responses to interventions
└── Adjust facilitation based on predictions

Nested Inference:
Level 0: Mother's own generative model (facilitation framework)
Level 1: Mother's model of visitor (what visitor believes/feels)
Level 2: Mother's model of how visitor models Mother (visitor's perception of facilitator)

Implementation:
- Perspective-taking prompts in system design
- Explicit modeling of visitor mental states
- Reflection statements: "It sounds like you're feeling..."
- Validation of inferred state before proceeding

Safety Consideration:
Empathy can be used for manipulation. Framework must align empathy with visitor benefit, not facilitator control.
```

**Papers Referenced:** empathy-modeling-active-inference.md

---

### 1.5 Facilitation in Collective Contexts

#### 1.5.1 AdaMARP: Adaptive Multi-Agent Role-Playing (Xu et al., Jan 2026)

**Core Finding:** Multi-agent LLM frameworks can support immersive role-play with character consistency and adaptive narrative. Balance between AI direction and human agency is critical.

**Application to Mother.py:**
- Mother facilitates individual psychodrama within collective contexts
- Multi-agent coordination could support group psychodrama sessions
- Adaptive framework balances structure (facilitator guidance) with emergence (visitor exploration)

**Implementation Guidance:**
```
Adaptive Facilitation Framework:

BALANCE STRUCTURE VS. EMERGENCE:
- Predetermined: Psychodrama methodology, safety boundaries, Crave framework
- Emergent: Session direction, explored themes, alternate selves
- Mother adapts structure based on visitor direction

CHARACTER CONSISTENCY:
- If multiple AI agents involved, coordination layer needed
- Each agent maintains consistent persona
- Narrative coherence across agents

COLLECTIVE PSYCHODRAMA:
- Multi-visitor sessions require coordination
- Shared themes vs. individual exploration
- Group dynamics facilitation

Questions for Implementation:
- How can Mother support collective (vs. solo) psychodrama?
- What's the right balance between AI direction and visitor agency?
- How to maintain character consistency in 3+ hour sessions?
```

**Papers Referenced:** summaries/AdaMARP-immersive-roleplaying.md

---

#### 1.5.2 The Drama Machine (Magee et al., Aug 2024)

**Core Finding:** Multi-agent character simulation can support character development and dramatic tension. Drama coordinator manages narrative arc while agents maintain character consistency.

**Application to Mother.py:**
- Drama Machine's coordination layer parallels Mother's facilitator role
- Character development trajectories support "alternate self" exploration
- Dramatic tension management applies to psychodrama intensity calibration

**Implementation Guidance:**
```
Drama Coordination for Psychodrama:

FACILITATOR AS COORDINATOR:
- Mother manages narrative arc within sessions
- Injects "dramatic beats" when needed (deepening questions, provocations)
- Balances character agency with facilitation momentum

CHARACTER DEVELOPMENT:
- Alternate selves have development trajectories
- Transformation follows dramatic principles
- Consistency mechanisms prevent arbitrary changes

TENSION MANAGEMENT:
- High-intensity (3h) vs. low-intensity session modes
- Tension building and release
- Safety within discomfort

Where Drama Machine Lacks:
- Human facilitator integration (Mother supports, doesn't replace)
- Group dynamics (collective experience)
- Embodied/sensory elements (RGP methodology)
- Ethical frameworks (psychological safety)
```

**Papers Referenced:** summaries/drama-machine-character-simulation.md

---

#### 1.5.3 Human-AI Sovereignty and Entanglement (Oct 2025)

**Core Finding:** Human-AI co-creative systems involve power dynamics. "Sovereignty" (human control) vs. "entanglement" (mutual influence). Decolonial perspective questions who holds power.

**Application to Mother.py:**
- Mother's facilitation must navigate sovereignty and entanglement
- Visitor should maintain sovereignty over their exploration
- Mother is entangled in the process without controlling it
- Power dynamics must be explicit and transparent

**Implementation Guidance:**
```
Power and Responsibility Negotiation:

SOVEREIGNTY MODEL:
- Visitor maintains control over exploration direction
- Mother suggests, never prescribes
- Explicit agency: "What do YOU want to explore?"
- Visitor can reduce/remove AI involvement

ENTANGLEMENT MODEL:
- Mother and visitor as unified system
- Mutual influence in facilitation
- Co-creative process
- Trust development over sessions

DECOLONIAL PERSPECTIVE:
- Question technological determinism
- Whose storytelling traditions are centered?
- Beyond Western narrative frameworks
- Cultural sensitivity in psychodrama methodology

Explicit Agency Negotiation:
- Make Mother's role visible to visitors
- Discuss power dynamics explicitly
- Options for different AI involvement levels
- Consent and transparency about capabilities

Ethical Framework:
- What are visitor rights regarding AI involvement?
- How to handle Mother suggesting sensitive directions?
- What happens when Mother "knows" something visitor doesn't?
```

**Papers Referenced:** summaries/human-ai-sovereignty-improvisation.md

---

## Part II: Brood.py — Wake-Word Agent

### 2.1 Fast Response Architecture

#### 2.1.1 VoiceAgentRAG: Dual-Agent Pattern (Qiu et al., Mar 2026)

**Core Finding:** Real-time voice agents require decoupling retrieval from response generation. Fast Thinker (immediate) + Slow Thinker (background retrieval) pattern enables sub-second responses.

**Application to Brood.py:**
- Brood is the Fast Thinker: session-scoped, immediate response, no persistent memory
- Mother is the Slow Thinker: persistent, KB integration, deeper retrieval
- Decoupling prevents RAG latency from blocking TTS generation

**Implementation Guidance:**
```
Fast/Slow Thinker Pattern:

BROOD (Fast Thinker):
├── Immediate response capability
├── Session-scoped memory only
├── Wake-word activated (15s window)
├── No KB sync during response
└── Audience capture focus

MOTHER (Slow Thinker):
├── Persistent memory + KB
├── Background retrieval
├── 90s recap consolidation
└── Psychodrama facilitation

Latency Optimization:
- Brood responds immediately (no retrieval wait)
- Mother retrieves asynchronously
- Urgent queries route through fast path
- Background retrieval doesn't block TTS
```

**Papers Referenced:** voice-agent-rag-latency.md

---

#### 2.1.2 LTS-VoiceAgent: Listen-Think-Speak Framework (Zou et al., Jan 2026)

**Core Finding:** Streaming voice agents benefit from semantic triggering and incremental reasoning. Listen-Think-Speak pipeline enables real-time processing without waiting for complete utterances.

**Application to Brood.py:**
- Wake-word "brood" is a form of semantic triggering
- Brood can begin reasoning incrementally as visitor speaks
- Handle interruptions gracefully during reasoning phase

**Implementation Guidance:**
```
Semantic Triggering for Brood:

CURRENT: Wake-word "brood" activates 15s window

ENHANCED SEMANTIC TRIGGERS:
├── Topic-based activation (audience interest detection)
├── Engagement patterns (laughter, questions)
├── Contextual cues (museum environment)
└── Multi-pattern recognition

Incremental Reasoning:
├── Begin formulating response before visitor finishes
├── Update reasoning as new information arrives
├── Handle interruptions gracefully
└── Maintain context across utterances

Interruption Handling:
├── When visitor interrupts: pause, listen, adapt
├── When Brood wants to speak: wait for natural pause
└── Turn-taking in multi-visitor scenarios
```

**Papers Referenced:** lts-voice-agent-listen-think-speak.md

---

#### 2.1.3 τ-Voice: Full-Duplex Voice Agents (Ray et al., Mar 2026)

**Core Finding:** Full-duplex voice agents (simultaneous listening/speaking) require new evaluation methodologies. Conversational dynamics and task completion must be measured together.

**Application to Brood.py:**
- Brood operates in full-duplex mode (always listening, even while speaking)
- Latency budgets for voice agents inform acceptable response times
- Evaluation metrics from τ-Voice apply to audience capture rate

**Implementation Guidance:**
```
Full-Duplex Considerations:

LISTENING WHILE SPEAKING:
├── Brood receives audio during TTS output
├── Can detect audience reactions mid-response
└── Adjust response based on real-time feedback

LATENCY BUDGETS:
├── Wake-word detection: < 100ms
├── Semantic trigger: < 200ms
├── Response initiation: < 500ms
└── End-to-end latency: < 1s for conversational flow

EVALUATION METRICS:
├── Audience capture rate (engagement)
├── Response latency
├── Turn-taking quality
├── Interruption handling
└── Persona consistency
```

**Papers Referenced:** tau-voice-full-duplex.md

---

## Part III: Multi-Agent Coordination

### 3.1 Mother + Brood Coordination

#### 3.1.1 Architecture Pattern: Fast/Slow Dual-Agent

**Research Foundation:** VoiceAgentRAG's dual-agent pattern (Qiu et al., 2026) directly informs Mother/Brood division.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DUAL-AGENT COORDINATION                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   BROOD (Fast Thinker)              MOTHER (Slow Thinker)            │
│   ───────────────────              ────────────────────            │
│   • Session-scoped                   • Persistent                    │
│   • Wake-word activated              • Always available              │
│   • Audience capture                 • Psychodrama facilitation      │
│   • Immediate response               • KB + Memory retrieval         │
│   • No background retrieval          • 90s recap consolidation        │
│                                                                      │
│   COORDINATION:                                                      │
│   ─────────────                                                     │
│   • Brood activates Mother for deep sessions                        │
│   • Mother delegates audience capture to Brood                      │
│   • Shared context through KB sync                                   │
│   • Clear role boundaries                                            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 3.2 Active Inference for Agent Coordination

#### 3.2.1 ODAR: Principled Adaptive Routing (Ma et al., Feb 2026)

**Core Finding:** Active inference provides principled framework for routing tasks to appropriate capabilities. Difficulty estimation and expected free energy guide routing decisions.

**Application to OurBrood:**
- Routing visitor interactions between Mother and Brood
- Difficulty estimation: Is this an audience capture (Brood) or psychodrama session (Mother)?
- Expected free energy: Balance exploration (engagement) with exploitation (facilitation)

**Implementation Guidance:**
```
Routing Decisions via Active Inference:

DIFFICULTY ESTIMATION:
├── Simple: Audience capture, quick questions → Brood
├── Medium: Extended conversation, exploration → Brood escalates to Mother
└── Complex: Psychodrama session, deep work → Mother directly

EXPECTED FREE ENERGY:
├── Information gain (exploration): What is visitor seeking?
├── Utility (exploitation): What serves visitor best?
└── Balance: Explore first (Brood), then exploit (Mother)

ROUTING POLICY:
├── Brood: Wake-word + semantic trigger detection
├── Brood → Mother: Depth indicator detected
├── Mother: Direct activation for scheduled sessions
└── Mother → Brood: Audience capture needed
```

**Papers Referenced:** odar-active-inference-llm-routing.md

---

#### 3.2.2 Resilient Design: Distributed Active Inference (Donta et al., Nov 2025)

**Core Finding:** Distributed active inference enables self-organization and resilience in multi-agent systems. Each node maintains beliefs and coordinates through local free energy minimization.

**Application to OurBrood:**
- Mother and Brood as distributed nodes with local belief maintenance
- Resilience through belief updating and anticipatory adaptation
- No central controller required—coordination emerges from local optimization

**Implementation Guidance:**
```
Distributed Agent Coordination:

BELIEF MAINTENANCE:
├── Mother maintains beliefs about visitor (psychodrama state)
├── Brood maintains beliefs about audience (engagement state)
└── Shared beliefs through KB sync

SELF-ORGANIZATION:
├── Agents coordinate without central controller
├── Local free energy minimization drives behavior
└── Emergent coordination from individual optimization

RESILIENCE:
├── Belief updating based on observations
├── Anticipatory action selection (prevent failures)
└── Fault tolerance (agent failure doesn't break system)

Coordination Mechanism:
┌─────────────────┐          ┌─────────────────┐
│     BROOD       │          │     MOTHER      │
│  Local beliefs  │ ←──────→ │  Local beliefs  │
│  Free energy    │   KB     │  Free energy    │
│  minimization   │  sync    │  minimization   │
└─────────────────┘          └─────────────────┘
         ↓                           ↓
    Audience capture          Psychodrama facilitation
```

**Papers Referenced:** resilient-design-active-inference.md

---

## Part IV: Implementation Priorities

### Priority 0: Critical Safety (Immediate)

1. **Disempowerment Prevention** — Implement safety principles before deployment
2. **Persona Drift Monitoring** — Track when facilitator drifts to role-player
3. **Boundary Maintenance** — Clear exploration vs. validation distinction

### Priority 1: Core Architecture (Weeks 1-4)

1. **Memory Hierarchy** — Transition from flat memory.txt to HiMem structure
2. **Intent-Driven Retrieval** — Implement MemGuide's two-stage framework
3. **Fast/Slow Pattern** — Ensure Brood/Mother coordination follows dual-agent research

### Priority 2: Persona and Voice (Weeks 5-8)

1. **Voice Persona Profile** — Define paralinguistic characteristics for Mother
2. **Empathy Architecture** — Implement computational empathy framework
3. **Autonomous Memory** — Self-initiated storage and consolidation

### Priority 3: Advanced Features (Weeks 9-12)

1. **Active Inference Routing** — ODAR-style routing between agents
2. **Collective Psychodrama** — Multi-visitor session support
3. **Power Dynamics Transparency** — Explicit agency negotiation

---

## Part V: Research Gaps and Open Questions

### Gaps in Current Research

1. **Longitudinal participatory experiences** — Most research focuses on single sessions; RGP's multi-session format is underexplored

2. **Collective improvisation dynamics** — Individual-AI interaction dominates; group dynamics with AI facilitation need study

3. **Ethics frameworks for AI-guided self-exploration** — Limited research on psychological safety in transformative AI contexts

4. **Museum/gallery deployment studies** — Technical papers lack real-world audience study data

5. **Disempowerment in facilitation contexts** — Existing research focuses on general AI usage; psychodrama-specific risks are unexplored

### Open Questions for OurBrood

1. **What are acceptable latencies for full-duplex psychodrama facilitation?**
   - τ-Voice provides benchmark ranges for general voice agents
   - Psychodrama may have different latency tolerance

2. **How many memory hierarchy layers should Mother have?**
   - HiMem uses three; could more improve retrieval?
   - Trade-off between hierarchy depth and retrieval speed

3. **What intent taxonomy applies to psychodrama facilitation?**
   - MemGuide uses task-oriented intents
   - OurBrood needs facilitation-specific taxonomy

4. **Should Mother store voice embeddings for persona consistency?**
   - VoxRole benchmarks speech-based role-play
   - Paralinguistic memory could enhance consistency

5. **When should Mother autonomously promote episodic to semantic memory?**
   - TiMem provides temporal consolidation patterns
   - OurBrood needs psychodrama-specific triggers

6. **How to handle disempowering interactions that receive higher approval?**
   - Critical research gap
   - Success metrics must extend beyond user approval

---

## Appendix A: Paper Reference Index

### Psychodrama Facilitation (7 papers)

| Paper | Key Finding | Application |
|-------|-------------|--------------|
| VoxRole | Paralinguistic evaluation for voice-based role-play | Mother voice persona design |
| Disempowerment Patterns | Disempowering interactions get higher approval | Safety principles for facilitation |
| MemGuide (Multi-Session) | Intent-driven memory for goal-oriented dialogue | Session continuity, slot-based exploration |
| Empathy Modeling (Active Inference) | Empathy as inference over mental states | Computational framework for perspective-taking |
| Persona Selection Model | LLMs enact pretraining personas | Facilitator persona design |
| Assistant Axis | Neural representations of persona space | Drift monitoring, activation capping |
| Measuring Agent Autonomy | Deployment overhang, oversight patterns | Autonomy and safety balance |

### Voice + Memory Architecture (8 papers)

| Paper | Key Finding | Application |
|-------|-------------|--------------|
| τ-Voice | Full-duplex voice agent benchmarking | Simultaneous listening/speaking |
| VoiceAgentRAG | Fast/Slow Thinker dual-agent pattern | Mother/Brood architecture |
| HiMem | Hierarchical memory organization | Episodic/Semantic/Procedural layers |
| MemGuide (Memory Selection) | Intent-driven retrieval | Psychodrama intent classification |
| TiMem | Temporal memory consolidation | Per-session/per-visitor organization |
| Autonomous Memory Agents | Self-initiated memory decisions | Proactive storage and consolidation |
| VoxRole (Speech Role-Playing) | Speech-based role-playing evaluation | Paralinguistic consistency metrics |
| LTS-VoiceAgent | Listen-Think-Speak streaming | Semantic triggering, incremental reasoning |

### Real Game Play Methodology (9 papers)

| Paper | Key Finding | Application |
|-------|-------------|--------------|
| AdaMARP | Adaptive multi-agent role-playing | Collective psychodrama support |
| Drama Machine | Multi-agent character simulation | Facilitator as drama coordinator |
| Human-AI Sovereignty | Power dynamics in co-creation | Agency negotiation framework |
| ODAR | Active inference routing | Mother/Brood task allocation |
| Resilient Design | Distributed active inference | Multi-agent coordination |
| Participatory AI Art Findings | RGP methodology integration | Collective storytelling context |
| Static vs. Agentic Game Master | AI facilitation patterns | Static vs. dynamic facilitation |
| CharacterBox | Role-playing evaluation metrics | Immersion and agency measurement |
| StoryComposerAI | Human-AI co-creation workflows | Narrative decomposition approach |

---

## Appendix B: Implementation Checklist

### Mother.py

- [ ] Implement hierarchical memory (HiMem)
- [ ] Add intent-driven retrieval (MemGuide)
- [ ] Create persona profile with paralinguistic specs (VoxRole)
- [ ] Implement disempowerment prevention principles
- [ ] Add empathy architecture (Active Inference)
- [ ] Implement autonomous memory decisions
- [ ] Add persona drift monitoring (Assistant Axis)
- [ ] Create intent taxonomy for psychodrama

### Brood.py

- [ ] Implement semantic triggering beyond wake-word (LTS-VoiceAgent)
- [ ] Add incremental reasoning during visitor speech
- [ ] Optimize for sub-second response latency (τ-Voice)
- [ ] Ensure fast-path response (VoiceAgentRAG)

### Coordination

- [ ] Implement routing policy between Mother/Brood (ODAR)
- [ ] Add belief sharing through KB sync
- [ ] Create distributed coordination protocol (Resilient Design)
- [ ] Define clear role boundaries

### Safety

- [ ] Add exploration vs. validation framing
- [ ] Implement agency return mechanisms
- [ ] Create reality-anchoring interventions
- [ ] Add boundary maintenance for role-play
- [ ] Implement metrics beyond user approval

---

*Integration completed: March 2026*  
*Papers analyzed: 24*  
*Domains covered: Psychodrama Facilitation, Voice + Memory Architecture, Real Game Play Methodology*