from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json

app = FastAPI(title="VoiceCanvas API", version="1.0.0")

@app.get("/")
def index():
    return {"service": "VoiceCanvas Real-time Diffusion Server", "fps": 15}

@app.websocket("/ws/stream")
async def websocket_diffusion_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)
            prompt = payload.get("prompt", "")
            await websocket.send_json({
                "status": "rendering",
                "prompt": prompt,
                "step": 4,
                "fps": 15.2
            })
    except WebSocketDisconnect:
        print("Client disconnected from VoiceCanvas stream")
