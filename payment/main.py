import os
import time

import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.background import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from starlette.requests import Request

# Carrega variáveis do .env
load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

# DATABASE TO PAYMENT SERVICE
redis = get_redis_connection(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    db=os.getenv("REDIS_DB"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)


class Order(HashModel):
    product_id: str
    price: float
    quantity: int
    fee: float
    total: float
    status: str  # pending, completed, refunded

    class Meta:
        database = redis


@app.get("/orders/{pk}")
async def get(pk: str):
    return Order.get(pk)


@app.post("/orders")
async def create(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()
    req = requests.get("http://localhost:8000/product/%s" % body["id"])
    product = req.json()

    order = Order(
        product_id=product["pk"],
        price=product["price"],
        quantity=body["quantity"],
        fee=0.2 * product["price"],
        total=product["price"] * body["quantity"] + 0.2 * product["price"],
        status="pending"
    )
    order.save()
    # Executa a funcao order_completed em background
    background_tasks.add_task(order_completed, order)

    return order


def order_completed(order: Order):
    time.sleep(10)
    order.status = "completed"
    order.save()
    # Envia a ordem para o Redis
    redis.xadd("order_completed", order.dict(), '*')
