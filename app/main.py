from fastapi import (
    FastAPI,
)

from app.config import (
    settings,
)
from app.animal.endpoints.endpoints import (
    router as animal_routers,
)


app = FastAPI()

app.include_router(
    router=animal_routers,
    prefix=settings.DEFAULT_URL_PREFIX,
)
