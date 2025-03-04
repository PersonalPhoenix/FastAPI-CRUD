from fastapi import (
    APIRouter,
)

from app.config import (
    settings,
)
from app.animal.endpoints.api_v1.endpoints import (
    router as animals_router,
)


router = APIRouter(
    tags=[settings.DEFAULT_URL_API_V1_TAG],
    prefix=settings.DEFAULT_URL_PREFIX_API_V1,
)


router.include_router(
    router=animals_router,
)
