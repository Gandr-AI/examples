#!/usr/bin/env python3
"""The lines that break phone agents, read back correctly.

Order IDs, dates, phone numbers, addresses: the exact text shapes a voice agent
has to say out loud and most speech APIs mangle. Renders four of them to WAV.

    pip install gandr
    export GANDR_API_KEY=gnd_...   # free key, 100,000 tokens, no card: https://gandr.ai
    python readback_demo.py
"""
import os
from gandr import Gandr

LINES = [
    "Order number 4-2-7-1 ships on March 3rd and arrives Thursday between 9 and 11 AM.",
    "Your appointment is confirmed for Tuesday, August 18th at 2:30 PM.",
    "The driver will call 415-555-0173 when the delivery reaches 1800 Oak Street, apartment 4B.",
    "Your balance is $1,204.67 and the payment posts on the 15th.",
]

def main():
    g = Gandr(os.environ["GANDR_API_KEY"])
    for i, line in enumerate(LINES, 1):
        path = f"readback_{i}.wav"
        with open(path, "wb") as f:
            f.write(g.say(line))
        print(f"{path}  <-  {line}")

if __name__ == "__main__":
    main()
