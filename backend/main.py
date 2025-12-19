from fastapi import FastAPI
from pydantic import BaseModel, Field
from loguru import logger
from prometheus_client import Counter, generate_latest
from starlette.responses import Response

from modules.calcul import calcul

app = FastAPI(title="FastIA Template API", version="1.0.0")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests"
)

class CalculRequest(BaseModel):
    n: int = Field(..., description="Entier à mettre au carré")


class CalculResponse(BaseModel):
    n: int
    carre: int

@app.middleware("http")
async def count_requests(request, call_next):
    REQUEST_COUNT.inc()
    return await call_next(request)

@app.get("/")
def root():
    logger.info("Route / appelée")
    return {"message": "API OK"}


@app.get("/health")
def health():
    logger.info("Route /health appelée")
    return {"status": "OK"}


@app.post("/calcul", response_model=CalculResponse)
def do_calcul(payload: CalculRequest):
    logger.info(f"Route /calcul appelée avec n={payload.n}")
    return {"n": payload.n, "carre": calcul(payload.n)}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
