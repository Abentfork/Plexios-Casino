from datetime import datetime
from typing import Optional
from pydantic import BaseModel

#API Schemas of User Class

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    last_login: Optional[datetime] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    credits: float
    created_at: datetime
    
    class Config():
        orm_mode = True