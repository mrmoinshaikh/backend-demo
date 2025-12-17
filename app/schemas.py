from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    subject: str
    marks: int

class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True
