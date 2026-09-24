from fastapi import FastAPI
from crm_api.modules.tasks.router import router as tasksRouter

def registerRouter(app: FastAPI):
    app.include_router(tasksRouter)