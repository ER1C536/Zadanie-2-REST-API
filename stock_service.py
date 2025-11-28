# stock_service.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from typing import Dict

app = FastAPI(title="Stock Service")

class Stock(BaseModel):
    productId: int
    quantity: int

# "Na sztywno" stany magazynowe
STOCKS: Dict[int, Stock] = {
    1: Stock(productId=1, quantity=15),
    2: Stock(productId=2, quantity=0),
    3: Stock(productId=3, quantity=42),
}

# adres Serwisu Produktów (użyj localhost:8001 dla lokalnego uruchomienia)
PRODUCT_SERVICE_BASE = "http://localhost:8001"

@app.get("/stock/{productId}", response_model=Stock)
async def get_stock(productId: int):
    product_url = f"{PRODUCT_SERVICE_BASE}/products/{productId}"
    # zapytanie do Serwisu Produktów
    timeout = httpx.Timeout(5.0, connect=3.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(product_url)
        except httpx.RequestError:
            # Serwis Produktów niedostępny
            raise HTTPException(status_code=503, detail="Produkt niedostepny")
    if resp.status_code == 404:
        # Produkt nie istnieje — propagujemy 404
        raise HTTPException(status_code=404, detail=f"Tego produktu o ID {productId} nie ma")
    if resp.status_code != 200:
        # Inny błąd z serwisu produktów
        raise HTTPException(status_code=502, detail="Wystąpil blad")

    # Produkt istnieje -> zwracamy stan magazynowy
    stock = STOCKS.get(productId)
    if not stock:
        # Możemy traktować brak wpisu jako 0 lub 404 - tu zwracam 200 z quantity 0
        return Stock(productId=productId, quantity=0)
    return stock