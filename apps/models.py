import uuid
from typing import Optional
from pydantic import BaseModel, Field


class ModelTask(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    completed: bool = False

    class Config:
        allow_users_by_name = True
        schema_extra = {
            "example": {
                "id": "001",
                "name": "Urgent Task",
                "completed": False,
            }
        }


class UpdateTaskModel(BaseModel):
    name: Optional[str]
    completed: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "Important Task",
                "completed": True,
            }
        }
