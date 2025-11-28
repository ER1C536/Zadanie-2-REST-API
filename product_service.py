# product_service.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Product Service")

class Product(BaseModel):
    id: int
    Nazwa: str
    Cena: float

# "Na sztywno" kilka produktów w pamięci
PRODUCTS: Dict[int, Product] = {
    1: Product(id=1, Nazwa="Laptop", Cena=4500.00),
    2: Product(id=2, Nazwa="Smartfon", Cena=2500.50),
    3: Product(id=3, Nazwa="Klawiatura", Cena=49.99),
    4: Product(id=3, Nazwa="Mysz bezprzewodowa", Cena=59.99),
    5: Product(id=3, Nazwa="Sluchwki", Cena=99.99),
    6: Product(id=3, Nazwa="Mysz ", Cena=69.99),
    
}

@app.get("/products/{id}", response_model=Product)
async def get_product(id: int):
    product = PRODUCTS.get(id)
    if not product:
        # zwracamy standardowe 404 z JSON-em
        raise HTTPException(status_code=404, detail=f"Produkt z id {id} nie znaleziony")
    return product