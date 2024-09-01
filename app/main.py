from __future__ import annotations

import logging

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)

from fastapi import FastAPI, Request

from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from .middleware import TokenMiddleware
from .api import (
    endpoint_routes
)

app = FastAPI(
    middleware=[
        # CORS middleware has to go before token middleware
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(TokenMiddleware),
    ],
    title="YourAPI",
    version="1.0.0",
    description="Description",
    contact={
        "name": "Name",
        "email": "contact@domain.com",
        "url": "domain.com",
    },
    termsOfService="domain.com/terms",
    servers=[{"url": "https://api.domain.com/v1/", "description": "Production"}],
)

app.include_router(endpoint_routes)

@app.middleware("http")
async def verify_token(request: Request, call_next):
    # Necessary for CORS
    if request.method == "OPTIONS":
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        return response
    response = await call_next(request)
    return response

