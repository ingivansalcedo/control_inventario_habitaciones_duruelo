from fastapi import FastAPI
from mangum import Mangum
import time

app = FastAPI(title="inventory-control-api")

@app.get("/health")
def health():
    return {"status":"ok", "ts": int(time.time())}

# handler expuesto para AWS Lambda (Mangum convierte ASGI -> Lambda)
handler = Mangum(app)
