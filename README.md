# Zadanie-2-REST-API
# README — Instrukcja uruchomienia mikroserwisów (Product Service & Stock Service)

## 1. Wymagania

* Python 3.10 lub nowszy
* Pip (zazwyczaj instalowany razem z Pythonem)
* System Windows / Linux / macOS

## 2. Struktura plików

Upewnij się, że katalog projektu zawiera:
 - product_service.py
 - stock_service.py
 - requirements.txt


## 3. Utworzenie i aktywacja wirtualnego środowiska

### Windows cmd

--------------------------------------------------------------------------------------------------

python -m venv venv
venv\Scripts\activate
--------------------------------------------------------------------------------------------------


### Linux / macOS


python3 -m venv venv
source venv/bin/activate


## 4. Instalacja zależności

--------------------------------------------------------------------------------------------------

pip install -r requirements.txt


## 5. Uruchomienie serwisów

### Serwis Produktów (port 8001)

--------------------------------------------------------------------------------------------------

uvicorn product_service:app --host 127.0.0.1 --port 8001 --reload

### Serwis Magazynowy (port 8002)

Otwórz **nowe okno terminala**, aktywuj ponownie środowisko, potem:

--------------------------------------------------------------------------------------------------

uvicorn stock_service:app --host 127.0.0.1 --port 8002 --reload

###8.Testowanie 

http://localhost:8001/products/1

http://localhost:8002/stock/999

--------------------------------------------------------------------------------------------------

## 9. Dezaktywacja środowiska

deactivate

