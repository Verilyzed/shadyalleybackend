import datetime

from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

MAINTENANCE = False
VERSION = "0.1.24"
PRICE_WEED = 10
PRICE_ECSTASY = 15
PRICE_CRACK = 20
PRICE_COCAINE = 25
PRICE_HEROINE = 30
PRICE_LSD = 5


@app.get("/data")
async def data():
    return {
        "maintenance": MAINTENANCE,
        "version": VERSION,
        "prices": {
            "weed": PRICE_WEED,
            "ecstasy": PRICE_ECSTASY,
            "cocaine": PRICE_COCAINE,
            "crack": PRICE_CRACK,
            "heroine": PRICE_HEROINE,
            "lsd": PRICE_LSD
        },
        "datetime": datetime.utcnow().strftime("%d.%m.%Y %H:%M:%S")
    }


@app.get("/time")
async def time():
    return {
        "maintenance": MAINTENANCE,
        "version": VERSION,
        "datetime": datetime.utcnow().strftime("%d.%m.%Y %H:%M:%S")
    }
