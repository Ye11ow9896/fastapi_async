from components.users.routers import router
from components.product.routers import product_router
from components.stats.routers import stat_router
import uvicorn
from fastapi import FastAPI


app = FastAPI(title="test async")
app.include_router(router)
app.include_router(product_router)
app.include_router(stat_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)
