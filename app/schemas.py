from pydantic import BaseModel

class DestinationBase(BaseModel):
    name: str
    country: str
    description: str

class DestinationCreate(DestinationBase):
    pass

class DestinationOut(DestinationBase):
    id: int

    class Config:
        orm_mode = True
