from core.configs import settings
from sqlalchemy import Column, String, Integer

class OfficeModel(settings.DBBaseModel):
    __tablename__ = "characters"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(128), nullable=False)
    position: str = Column(String(64), nullable=False)
    age: int = Column(Integer, nullable=False)
    relationship_status: str = Column(String(64), nullable=True)
    office_hobbies: str = Column(String(256), nullable=True)
    quote: str = Column(String(256), nullable=True)

