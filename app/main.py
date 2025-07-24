from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.home import router as home_router

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.include_router(home_router)

@app.get("/health", response_class=HTMLResponse)
async def health_check():
    return "OK"
