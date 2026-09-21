from fastapi import FastAPI

app = FastAPI(title="CRM API")

@app.get("/health")
async def health():
    return {"status": "okay"}