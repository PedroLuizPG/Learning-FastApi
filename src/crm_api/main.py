from fastapi import FastAPI
from crm_api.modules.tasks.router import router as tasks_router

app = FastAPI(title="CRM API")

@app.get("/health")
async def health():
    return {"status": "okay"}

app.include_router(tasks_router)