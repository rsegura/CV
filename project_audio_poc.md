---
name: audio-poc-nacar
description: nacar.ai — Voice agent PoC for clinical pre-screening (migraine trial demo) with LiveKit + Deepgram + OpenRouter + ElevenLabs
metadata:
  type: project
---

audio_poc (nacar.ai) is a voice agent for clinical pre-screening. Demo scenario: migraine trial qualification.

Stack: LiveKit (WebRTC), Deepgram (STT), OpenRouter (LLM), ElevenLabs (TTS). 1,229 tests, transactional fence pattern, SQLite WAL persistence. 7 development phases completed.

**Why:** This is the most mature PoC in ~/Develop, with substantial test coverage and a clear product direction.

**How to apply:** Treat this as production-grade code, not a throwaway prototype. Changes should maintain test coverage.
