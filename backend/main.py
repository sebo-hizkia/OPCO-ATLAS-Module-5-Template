from fastapi import FastAPI
from pydantic import BaseModel, Field
from loguru import logger

from modules.calcul import calcul

app = FastAPI(title="FastIA Template API", version="1.0.0")


class CalculRequest(BaseModel):
    n: int = Field(..., description="Entier à mettre au carré")


class CalculResponse(BaseModel):
    n: int
    carre: int


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
