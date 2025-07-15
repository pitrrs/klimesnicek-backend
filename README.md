# KLIMEŠNÍČEK - Rychlý backend

## Spuštění:
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8124
```

## Endpointy:
- `GET /health` – kontrola dostupnosti
- `GET /recipes` – seznam receptů
- `GET /meal_plan` – aktuální plán

## Databáze:
Soubor `klimesnicek.db` musí být ve stejné složce jako `main.py`.