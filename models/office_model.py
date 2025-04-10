from core.configs import settings
from sqlalchemy import Column, String, Integer, Float

class OfficeModel(settings.DBBaseModel):
    __tablename__ = "characters"

    id: int = Column(Integer(), primary_key = True, autoincrement = True)
    name: str = Column(String(128), nullable = False)
    team: str = Column(String(16), nullable = False)
    color: str = Column(String(16))
    age: int = Column(Integer())