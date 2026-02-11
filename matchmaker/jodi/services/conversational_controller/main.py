from fastapi import FastAPI, HTTPException
from .models import ConversationState, UpdateStateRequest, AdvanceStateRequest
from .config import settings, AUTO_CONFIDENCE, REVIEW_CONFIDENCE
from typing import Dict
from uuid import uuid4
from datetime import datetime

app = FastAPI(title="Conversational Controller")

# In-memory store (placeholder for DB integration)
_store: Dict[str, ConversationState] = {}

@app.post("/state/update")
def update_state(req: UpdateStateRequest):
    # naive progress computation: percent of keys completed in completion_map
    session_key = req.session_id
    obj = _store.get(session_key)
    if not obj:
        obj = ConversationState(id=uuid4(), user_id=req.user_id, session_id=req.session_id, state_json=req.state_json, confidence_map={"last": req.confidence}, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    else:
        obj.state_json = req.state_json
        obj.confidence_map["last"] = req.confidence
        obj.updated_at = datetime.utcnow()
    # set progress_pct as mean confidence for now
    obj.progress_pct = float(req.confidence * 100)
    _store[session_key] = obj

    # Decide action based on confidence thresholds
    if req.confidence >= AUTO_CONFIDENCE:
        status = "auto"
    elif req.confidence >= REVIEW_CONFIDENCE:
        status = "review"
    else:
        status = "clarify"

    return {"session_id": session_key, "status": status, "progress_pct": obj.progress_pct}

@app.get("/state/{session_id}")
def get_state(session_id: str):
    obj = _store.get(session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@app.post("/state/advance")
def advance_state(req: AdvanceStateRequest):
    obj = _store.get(req.session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    # TODO: integrate extractor to compute next state
    # For now, bump progress
    obj.progress_pct = min(100.0, obj.progress_pct + 10.0)
    obj.updated_at = datetime.utcnow()
    _store[req.session_id] = obj
    return {"session_id": req.session_id, "progress_pct": obj.progress_pct}
