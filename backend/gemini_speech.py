import asyncio
import os
import google.generativeai as genai
from dotenv import load_dotenv
from google.genai import types
import numpy as np

# Load your .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from your .env file!")

MODEL = "models/gemini-2.0-flash-live-001"
client = genai.Client(api_key=api_key, http_options={"api_version": "v1beta"})

CONFIG = types.LiveConnectConfig(
    response_modalities=["audio"],
    speech_config=types.SpeechConfig(
        voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Puck")
        )
    ),
    system_instruction=types.Content(
        parts=[
            types.Part.from_text(
                text=(
                    "You are a text-to-speech system. "
                    "ONLY read the input text exactly as it is written. "
                    "Do not translate, do not change the language, do not explain, "
                    "and do not add anything extra. "
                    "Just speak the input text word-for-word aloud, in the language provided."
                    "You should not be speaking in English, but in the language of the input text, which will be either Spanish, French, Norwegian, or Mandarin. "
                )
            )
        ],
        role="user"
    )
)

# ✅ Conversion function (handles float32 → int16)
def convert_float32_to_int16(pcm_bytes):
    float_data = np.frombuffer(pcm_bytes, dtype=np.float32)
    int16_data = np.clip(float_data, -1.0, 1.0)
    int16_data = (int16_data * 32767).astype(np.int16)
    return int16_data.tobytes()

# ✅ Gemini speech generator
async def speak_text(text):
    audio_chunks = []

    async with client.aio.live.connect(model=MODEL, config=CONFIG) as session:
        await session.send(input=text, end_of_turn=True)
        turn = session.receive()

        async for response in turn:
            if data := response.data:
                audio_chunks.append(data)

    combined_audio = b''.join(audio_chunks)
    print(f"[DEBUG] Combined audio length: {len(combined_audio)} bytes")
    print(f"[DEBUG] First 20 bytes: {combined_audio[:20]}")

    # ✅ No conversion needed — Gemini sends int16 PCM!
    return combined_audio

