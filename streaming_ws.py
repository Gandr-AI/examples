"""First audio byte in ~116 ms warm: the WebSocket lane voice agents use.

    pip install websockets
"""

import asyncio
import json
import time

import websockets

KEY = "gnd_..."


async def main():
    async with websockets.connect(
        "wss://tts.gandr.ai/ws", additional_headers={"x-api-key": KEY}
    ) as ws:
        t0 = time.perf_counter()
        await ws.send(json.dumps({
            "text": "Your appointment is confirmed for Tuesday at ten.",
            "lang": "en",
            "voice_id": "gandr-mia",
            "output_sample_rate": 24000,
        }))
        async for msg in ws:
            if isinstance(msg, bytes):
                print(f"first audio byte: {(time.perf_counter() - t0) * 1000:.0f} ms")
                break


asyncio.run(main())
