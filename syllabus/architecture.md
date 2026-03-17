# OurBrood AI Agent Architecture

**Commissioned by:** OMSK Social Club  
**Presented at:** ArkDes, Stockholm 2025  
**Created by:** SEMILLA.AI Studio (Moisés Horta)  
**© 2025-2026**

---

## Project Overview

PROJECT OURBR00D is a unique opportunity to explore alternate versions of yourself as part of one of the most extensive roleplays commissioned by a museum. Become a part of the exhibition by playing this full-scale Real Game Play (RGP) — an interactive experience designed by OMSK Social Club, created for Worldglimpsing.

This is an experimental work that positions roleplay as an expanded form of participatory design. A shared space to test how we might live together, raise intelligence (both human and artificial), and negotiate responsibility when faced with ecological and technological transformations.

OUR BR00D is a facilitated roleplay — the complete work can only be experienced with a guide. On select weekends, sign up to play the three hour-long high intensity experience. On Fridays, Saturdays, and Sundays, participate in a shorter, low intensity experience.

---

## OMSK Social Club

A stewarded practice of collective storytelling involving a specific immersive improvised methodology, coined in 2017 as 'Real Game Play', encompassing collective immersion and speculative worlding. From live iterations, they harvest media relics — films, scripts, and large-scale video installations.

---

## Credits

- **Our Brood by:** OMSK Social Club
- **Assistant to OSC:** Mina Kalvøy
- **Spatialisation at ArkDes:** Daryan Knoblauch
- **Voice Actor:** Angela Rafferty
- **Embroidery Production:** Angela Rafferty
- **Furniture/Object:** Natália Sýkorová
- **Frame Production:** Nevo Bar
- **AI Development + Voice Cloning:** SEMILLA STUDIO (Moisés Horta)
- **Photography:** Jonas Schoeneberg
- **Audio Recording + Post:** Alfie Brooks
- **Music Composition:** Yikii
- **AI Consultation:** Cem Dagdelen, Joey Holder, Will Allstetter

Research shaped through the Brood Reading Group (Callie's, Berlin, 2024–2025) and playtesting at Shedhalle, Zürich; Sybil, Berlin; and Nieuwe Instituut, Rotterdam.

---

## Commission

Commissioned by ArkDes and Nieuwe Instituut with support from Shedhalle (Zürich), Callie's (Berlin), and Haus der Kunst (Munich) as part of Art & AI, Kulturstiftung des Bundes. Following Stockholm, journeys to Rotterdam 2026.

---

## File Structure

```
mother.py           1271 lines    main agent
brood.py             693 lines    brood agent
sync_memories_now.py 114 lines    KB sync util
mother_system_prompt.md            system prompt
memories/mother_memory.txt         memory store
conversations/*.txt                transcripts
```

---

## mother.py — Guardian Agent

### Description
Cloud-based ElevenLabs voice agent. Guardian of Brood.py and the Crave. Facilitates psychodrama sessions with human visitors. Persistent long-term memory via plaintext store + KB sync.

### Inputs
- Microphone audio (PCM 44.1 kHz mono)
- `.env`: `API_KEY`, `MOTHER_AGENT_ID`
- Hotkeys: `'a'` active, `'space'` listen
- `mother_audio_config.json`
- Dynamic vars: `{{greeting}}`, `{{memory_context}}`

### Tools
- `save_memory(content: str)` — Persist note to memory.txt
- `recall_memories(query, limit)` — Search in memory.txt

### Outputs
- Speaker audio (stereo, pan/vol)
- Transcript log (console)
- `mother_memory.txt` (recap + saves)
- `mother_sync.json` (KB metadata)

### Dataset
`mother_memory.txt`
```
YYYY-MM-DD HH:MM | tag | content
```
Tags: `recap` (auto 90s), `note`

### Components
```
MIC → RESAMPLE → WEBSOCKET → LLM → PROMPT → TTS → KB → SPEAKER
                      ↓
                    ECHO
                      ↓
               TRANSCRIPT BUFFER
                      ↓
                    RECAP → MEMORY TOOLS → SYNC → CTRL
```

---

## brood.py — Wake-Word Agent

### Description
Always-on ElevenLabs voice agent. Wake-word activated ("brood"). Multi-channel audio output with optional channel duplication. Stateless — no persistent memory between sessions.

### Inputs
- Microphone audio (PCM, auto-detect SR)
- `.env`: `API_KEY`, `BROOD_AGENT_ID`
- Wake word trigger ("brood")
- `brood_audio_config.json`

### Tools
- `save_memory(content: str)` — Persist note to memory.txt
- `recall_memories(query, limit)` — Search in memory.txt

### Outputs
- Speaker(s) audio (multi-ch, pan/vol/dup)
- Transcript log (console)

### Dataset
Remembered words from audience. Stored in `brood_memory.txt`. Captures audience interactions. Persists across sessions.

### Notes
- Wake word "brood" activates 15s window
- Outside window: speech muted + interrupted
- No ACTIVE/LISTENING toggle — always-on
- Supervisor process auto-restarts on crash

### Components
```
MIC → RESAMPLE → WEBSOCKET → LLM → TTS → SPEAKER → ROUTE
                      ↓                        ↓
                   TRANSCRIPT                WAKE
                      ↓                        ↓
                    GATE ← ← ← ← ← ← ← ← ← ← MUTE
                      ↓
                     IDLE → WATCH
```

---

## Key Architecture Concepts

### Two-Agent System
1. **Mother** — Persistent, facilitator, psychodrama guide
2. **Brood** — Ephemeral, audience-capturing, wake-word activated

### Memory Architecture
- **Mother**: Long-term memory via plaintext + KB sync
- **Brood**: Session-scoped only, stateless

### Voice Pipeline
Both use ElevenLabs TTS with:
- WebSocket streaming
- Real-time audio processing
- Multi-channel output

### Wake Word System
Brood listens for "brood" activation:
- 15-second active window
- Auto-mute outside window
- Supervisor process for resilience

---

*Documentation sourced from ourbrood_AIAgent_architecture.pdf (SEMILLA.AI Studio, 2025)*