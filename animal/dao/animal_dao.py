from app.animal.dao.base_dao import (
    BaseDAO,
)
from app.animal.domain.models import (
    Animals,
)


class AnimalDAO(BaseDAO):
    obj = Animals