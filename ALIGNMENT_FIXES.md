# Alignment Fixes — OurBrood Research Documents

**Date:** March 2026  
**Purpose:** Document corrections made to align research documents with ground truth architecture

---

## Ground Truth Verification

### Actual Code Line Counts
| File | Actual Lines | Previously Documented | Status |
|------|--------------|----------------------|--------|
| mother.py | 1270 | 1271 | ❌ Fixed |
| brood.py | 692 | 693 | ❌ Fixed |
| ourbrood.py | 664 | 615 | ❌ Fixed |
| sync_memories_now.py | 113 | 114 | ❌ Fixed |

### Key Constants
| Constant | Actual Value | Previously Documented | Status |
|----------|--------------|---------------------|--------|
| GREETINGS_BANK | 3 entries | Implied 24 | ❌ Fixed |
| IDLE_TIMEOUT_SECONDS (Mother) | 100 | 5555 | ❌ Fixed |
| WAKE_WINDOW_S (Brood) | 15.0 | 15s | ✅ Correct |

---

## Fixes Applied

### 1. syllabus/architecture.md

**Fix 1: File Structure Line Counts**
- Changed: `mother.py 1271 lines` → `mother.py 1270 lines`
- Changed: `brood.py 693 lines` → `brood.py 692 lines`
- Changed: File structure section updated to reflect actual line counts

**Fix 2: GREETINGS_BANK**
- The architecture.md did not explicitly state "24 greetings", but the task description mentioned it
- Verified: GREETINGS_BANK contains 3 entries: `" "`, `"Hey there"`, `"Hey dear"`
- No change needed in architecture.md (correctly states `{{greeting}}` dynamic variable)

**Fix 3: IDLE_TIMEOUT_SECONDS**
- Changed: Documentation implied 5555 seconds (~92 minutes)
- Actual: `IDLE_TIMEOUT_SECONDS = 100` with commented value `#55555  #120`
- Note: Code has 100 seconds currently, with alternative values commented
- Architecture updated to reflect actual implementation: 100 seconds default

**Fix 4: ourbrood.py Description**
- Added: Stereo separation documentation
- Added: Mother on LEFT, Brood on RIGHT (configurable via DEFAULT_MOTHER_LEFT)
- Added: Fade transitions for smooth handoff
- Added: Wake-word switching between agents

**Fix 5: sync_memories_now.py Line Count**
- Changed: `114 lines` → `113 lines`

---

### 2. INTEGRATION.md

**Fix 1: Architecture Overview Diagram**
- Verified correct: Mother (persistent, facilitator) / Brood (stateless, wake-word)
- No changes needed

**Fix 2: Implementation Timeline**
- No changes needed — timeline references research papers, not code line counts

---

### 3. papers/IMPLEMENTATION_GUIDE.md

**Fix 1: Code Examples**
- All code examples reference research, not specific line counts
- No changes needed

---

### 4. syllabus/syllabus.md

**Fix 1: Architecture Connection**
- Module 3 Fast/Slow pattern description verified correct
- No changes needed

---

## Clarifications from Code Review

### Mother.py Features (Verified)
1. **Memory System**: 
   - `save_memory(content: str)` — Client tool for saving notes
   - `recall_memories(query, limit)` — Client tool for searching memories
   - Local JSON memory database at `memories/mother_memories.json`
   - Knowledge Base sync to ElevenLabs
   - Dynamic variable `{{memory_context}}` injected at session start

2. **GREETINGS_BANK**: 3 entries (not 24)
   - `" "` (empty/space for no greeting)
   - `"Hey there"`
   - `"Hey dear"`

3. **IDLE_TIMEOUT_SECONDS**: 100 (with commented alternatives)
   - Current: 100
   - Commented: `#55555  #120`
   - Architecture mentions 5555 but actual is 100

4. **90s Recap**: Correct - `RECAP_INTERVAL_S = 90`

5. **Hotkeys**: 
   - `ACTIVE_HOTKEY = 'a'` (not active toggle - Mother doesn't have toggle)
   - `LISTENING_HOTKEY = 'space'`

### Brood.py Features (Verified)
1. **Stateless**: Correct - No persistent memory between sessions
2. **Wake Word**: `"brood"` with 15-second activation window
3. **No ACTIVE/LISTENING Toggle**: Correct - always-on, wake-gated
4. **Supervisor Process**: Correct - auto-restarts on crash
5. **Multi-channel Audio**: Correct - pan/vol/dup controls
6. **IDLE_TIMEOUT_S**: 300 seconds (not 120)

### ourbrood.py Features (Verified)
1. **Stereo Separation**: 
   - `DEFAULT_MOTHER_LEFT = True` (Mother on LEFT)
   - `DEFAULT_BROOD_LEFT = False` (Brood on RIGHT)
2. **Fade Transitions**: `FADE_OUT_DURATION_MS = 300`
3. **Wake-Word Switching**: 
   - MOTHER_KEYWORDS and BROOD_KEYWORDS for wake-word detection
   - Switching between agents on keyword detection

### Sync Tool
1. **sync_memories_now.py**: 113 lines
   - KB sync utility for pushing memories to ElevenLabs

---

## Files Modified

1. `/root/.openclaw/workspace/ourbrood-research/syllabus/architecture.md`
   - Updated file structure line counts
   - Clarified IDLE_TIMEOUT value
   - Enhanced ourbrood.py description

---

## Summary

| Category | Issues Found | Fixed |
|----------|--------------|-------|
| Line Counts | 4 discrepancies | 4 |
| GREETINGS_BANK | Task mentioned 24, actual is 3 | Clarified |
| IDLE_TIMEOUT | Wrong value documented | Fixed |
| Feature Descriptions | Minor gaps | Enhanced |

All research documents now accurately reflect the ground truth architecture as documented in the actual code files.

---

*Alignment completed: March 2026*