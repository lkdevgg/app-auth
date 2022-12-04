from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import datetime
from src.models.PyObjectId import PyObjectId


class UserModel(BaseModel):
    userid: str = Field(..., title="User name", max_length=64, min_length=4,
                        description="UserID must not be blank")
    password: str = Field(..., title="Password", min_length=8, max_length=128,
                          description="Password must not be blank")
    company: Optional[str] = Field(default=None, description="Describe your company")
    role: str = Field(default="guest", title='Role')
    permission: list = Field(default=[], description="list of permission")
    setting: dict = Field(default={"theme": "light", "nav": "left"}, description="Setting")
    created_by: str = Field(None, title="Creater userid")

    def as_dict(self):
        return {"userid": self.userid,
                "password": self.password,
                "company": self.company,
                "role": self.role,
                "permission": self.permission,
                "setting": self.setting,
                "created_by": self.created_by,
                "created_at": datetime.datetime.now()}


class UserUpdateModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    userid: str = Field(..., title="User name", max_length=64, min_length=4,
                        description="UserID must not be blank")
    password: str = Field(..., title="Password", min_length=8, max_length=128,
                          description="Password must not be blank")
    company: Optional[str] = Field(default=None, description="Describe your company")
    role: str = Field(default="guest", title='Role')
    permission: list = Field(default=[], description="list of permission")
    setting: dict = Field(default={"theme": "light", "nav": "left"}, description="Setting")
    updated_by: Optional[str] = Field(
        None, title="Updater Userid"
    )

    def as_dict(self):
        return {"id": self.id,
                "userid": self.userid,
                "password": self.password,
                "company": self.company,
                "role": self.role,
                "permission": self.permission,
                "setting": self.setting,
                "updated_at": datetime.datetime.now(),
                "updated_by": self.updated_by}


def ResponseModel(data, code, message, error):
    return {
        "data": [data],
        "code": code,
        "message": message,
        "error": error
    }
