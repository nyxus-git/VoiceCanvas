# VoiceCanvas 🎨🎙️
> Real-time interactive voice-directed generative canvas powered by continuous Whisper streaming and SDXL Turbo.

## 🚀 Overview
VoiceCanvas allows creators to paint and sculpt visual scenes through natural speech. As you speak, streaming Whisper transcribes and parses creative directives, while an optimized SDXL Turbo model with LCM LoRAs synthesizes and updates 1024x1024 frames over WebSockets at 15 FPS.

## 🛠️ Tech Stack
- **Diffusion Engine**: PyTorch, Diffusers, SDXL Turbo, FlashAttention-2, TensorRT
- **Voice Pipeline**: faster-whisper (streaming chunking), WebAudio API
- **Transport**: FastAPI WebSockets with binary JPEG frame compression
- **Viewport**: Three.js, WebGL, React

## 📂 Project Structure
```
VoiceCanvas/
├── app/
│   ├── diffusion/     # SDXL Turbo worker & LCM scheduler
│   ├── voice/         # Whisper streaming transcriber
│   └── main.py        # WebSocket hub and REST API
├── web/               # Three.js canvas frontend
├── requirements.txt
└── README.md
```

## ⚡ Quick Start (Arch Linux)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8000 --reload
```
