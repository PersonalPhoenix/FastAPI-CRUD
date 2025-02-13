from app.animal.dao.base_dao import (
    BaseDAO,
    TestDAO,
)
from app.animal.domain.models import (
    Animals,
)


class AnimalDAO(BaseDAO):
    """DAO для модели Animals."""

    obj = Animals
