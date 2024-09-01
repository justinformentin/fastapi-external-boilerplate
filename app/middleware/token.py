from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi.responses import JSONResponse
from fastapi.security.utils import get_authorization_scheme_param

class TokenMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            authorization: str = request.headers.get("Authorization")
            scheme, token = get_authorization_scheme_param(authorization)
            # token_service(token)
            response: Response = await call_next(request)
            return response
        except:
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

