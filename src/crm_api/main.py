from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from .routes import registerRouter
from .shared.Errors.errors import AppError

app = FastAPI(title="CRM API")

@app.exception_handler(AppError)
async def app_error_handler(req: Request, excp: AppError):
    return JSONResponse(
        status_code=excp.statusCode, 
        content={"message": excp.message}
        )
    
@app.exception_handler(RequestValidationError)
async def validation_error_handler(req: Request, excp: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"message": "Validation error", "issues": excp.errors()},
    )

@app.get("/health")
async def health():
    return {"status": "okay"}

registerRouter(app)