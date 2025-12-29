import asyncio
from typing import Dict
from uuid import uuid4

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse

from models.schemas import JobState, RunRequest
from services.wenjx_service import run_job
from templates.index import HTML_TEMPLATE

router = APIRouter()

job_store: Dict[str, JobState] = {}


@router.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse(content=HTML_TEMPLATE, headers={"Cache-Control": "no-store, no-cache, must-revalidate"})


@router.get("/favicon.ico")
async def favicon():
    return JSONResponse(content=None, status_code=204)


@router.post("/run")
async def create_run(req: RunRequest):
    job_id = uuid4().hex
    job_store[job_id] = JobState(status="queued", logs=[], error=None)
    asyncio.create_task(run_job(job_id, req.url, req.times, job_store, req.show_browser))
    return JSONResponse({"job_id": job_id})


@router.get("/status/{job_id}")
async def job_status(job_id: str):
    if job_id not in job_store:
        raise HTTPException(status_code=404, detail="job not found")
    return job_store[job_id]
