from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator, metrics

app = FastAPI()

instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
    should_group_untemplated=True,
)

# Optional: Add custom metrics like latency, request sizes, etc.
instrumentator.add(metrics.latency())
instrumentator.add(metrics.requests())
instrumentator.add(metrics.response_size())
instrumentator.add(metrics.request_size())

instrumentator.instrument(app).expose(app, include_in_schema=False)

@app.get("/")
async def home():
    return {"message": "Hello from SECURESNAP"}

@app.get("/health")
async def health():
    return {"status": "OK"}
