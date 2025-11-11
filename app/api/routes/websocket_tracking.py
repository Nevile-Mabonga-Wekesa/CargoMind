# app/api/routes/websocket_tracking.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio, json
import redis.asyncio as aioredis
from app.core.config import settings

router = APIRouter(prefix="/ws", tags=["WebSocket"])

@router.websocket("/track")
async def websocket_track(websocket: WebSocket):
    await websocket.accept()

    redis_conn = await aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        decode_responses=True
    )

    pubsub = redis_conn.pubsub()
    await pubsub.subscribe("vehicle_updates")

    try:
        async for message in pubsub.listen():
            if message["type"] == "message":
                await websocket.send_text(message["data"])
    except WebSocketDisconnect:
        await pubsub.unsubscribe("vehicle_updates")
        await redis_conn.close()
