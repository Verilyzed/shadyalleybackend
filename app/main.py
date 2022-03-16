import datetime

from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

MAINTENANCE = False
PRICE_WEED = 10
PRICE_CRACK = 15
PRICE_ECSTASY = 20
PRICE_HEROINE = 25
PRICE_LSD = 5


@app.get("/data")
async def data():
    return {
        "maintenance": MAINTENANCE,
        "prices": {
            "weed": PRICE_WEED,
            "crack": PRICE_CRACK,
            "ecstasy": PRICE_ECSTASY,
            "heroine": PRICE_HEROINE,
            "lsd": PRICE_LSD
        },
        "datetime": datetime.utcnow().strftime("%d.%m.%Y %H:%M:%S")
    }
