from fastapi import (
    FastAPI,
)

from app.animal.endpoints.api_v1.api_v1_router import (
    router as api_v1_router,
)


app = FastAPI()


app.include_router(
    router=api_v1_router,
)
