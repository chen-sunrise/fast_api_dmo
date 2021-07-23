import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.applications.controller.test import router as api_router
from src.applications.config.customer_server import ALLOWED_HOSTS, API_PREFIX


def create_app():
    fast_app = FastAPI(debug=True)

    # 配置中间件
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    return fast_app


app = create_app()
app.include_router(api_router, prefix=API_PREFIX)


if __name__ == '__main__':
    uvicorn.run("manage:app", host="0.0.0.0", port=8081, debug=True, reload=True, lifespan="on")