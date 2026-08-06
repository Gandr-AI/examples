"""Batch-render an IVR prompt library. pip install gandr"""

from gandr import Gandr

g = Gandr("gnd_...")

PROMPTS = {
    "welcome": "Thank you for calling. Your call matters to us.",
    "menu": "Press 1 for reservations, 2 for takeout, 3 for hours and directions.",
    "hold": "One moment while we connect you.",
    "goodbye": "Thanks for calling. Goodbye.",
}

for name, text in PROMPTS.items():
    audio = g.say(text, voice="gandr-jenny", temperature=0.6, cfg_weight=0.5)
    with open(f"{name}.wav", "wb") as f:
        f.write(audio)
    print(f"{name}.wav — {len(audio)} bytes")
