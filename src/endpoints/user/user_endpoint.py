from fastapi import APIRouter
from src.models.user.user_model import UserModel, UserUpdateModel, ResponseModel
from src.endpoints.user.user_handler import add_user, read_user, update_user, delete_user, read_users

# APIRouter creates path operations for user module
router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.post("/add", response_description="user data added into the database")
async def add_user_data(user: UserModel):
    user = user.as_dict()
    new_user = await add_user(user)
    return ResponseModel(new_user, 200, "user added successfully.", False)


@router.put("/update")
async def update_user_data(user: UserUpdateModel):
    user = user.as_dict()
    updated_user = await update_user(user.get("id"), user)
    return ResponseModel(updated_user, 200, "user updated successfully.", False)


@router.delete("/{user_id}/delete")
async def delete_user_data(user_id: str):
    deleted_result = await delete_user(user_id)
    return ResponseModel(deleted_result, 200, "user deleted successfully.", False)


@router.get("/{user_id}")
async def read_user_data(user_id: str):
    user = await read_user(user_id)
    return ResponseModel(user, 200, "user retrieved successfully.", False)

@router.get("/")
async def read_users_data():
    users = await read_users()
    return ResponseModel(users, 200, "user retrieved successfully.", False)