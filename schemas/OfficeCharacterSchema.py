from pydantic import BaseModel
from typing import Optional

class OfficeCharacterSchema(BaseModel):
    id: Optional[int] = None
    name: str
    position: str  
    age: int
    relationship_status: Optional[str] = None 
    office_hobbies: Optional[str] = None 
    quote: Optional[str] = None  

    class Config:
        orm_mode = True

