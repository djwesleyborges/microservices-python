import os
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

# DATABASE TO INVENTORY SERVICE
redis = get_redis_connection(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    db=os.getenv("REDIS_DB"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)



class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


class ProductUpdate(HashModel):
    name: Optional[str]
    price: Optional[float]
    quantity: Optional[int]

    class Meta:
        database = redis


@app.get('/products')
def all():
    products = [format(pk) for pk in Product.all_pks()]
    return products


def format(pk: str):
    product = Product.get(pk)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.post('/products')
def create(product: Product):
    return product.save()


@app.get('/product/{pk}')
def get(pk: str):
    return Product.get(pk)


@app.put('/product/{pk}')
def update(pk: str, product: ProductUpdate):
    existing_product = Product.get(pk)

    # atualiza apenas os campos enviados no body
    updated_data = product.dict(exclude_unset=True)
    for field, value in updated_data.items():
        setattr(existing_product, field, value)

    return existing_product.save()


@app.delete('/product/{pk}')
def delete(pk: str):
    return Product.delete(pk)
