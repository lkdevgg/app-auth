from db.database import User
from src.models.PyObjectId import PyObjectId


async def add_user(user_data: dict):
    # db = await database.db_connection()
    user = await User.insert_one(user_data)
    new_user = await User.find_one({"_id": user.inserted_id})
    return to_user(new_user)


# Retrieve a user by id
async def read_user(id: str):
    # db = await database.db_connection()
    user = await User.find_one({"_id": PyObjectId(id)})
    if user:
        return to_user(user)
    return None


# Retrieve a user by id
async def read_users():
    # db = await database.db_connection()
    users = await User.find().to_list(500)
    if users:
        return to_user_list(users)
    return None


# Update a user by id
async def update_user(id: str, user_data: dict):
    if len(user_data) < 1:
        return False
    # db = await database.db_connection()
    user = await User.find_one({"_id": PyObjectId(id)})
    if user:
        user["name"] = user_data.get("name")
        user["price"] = user_data.get("price")
        user["updated_by"] = user_data.get("updated_by")
        updated_user = await User.update_one({"_id": PyObjectId(id)}, {"$set": user})
        return updated_user.acknowledged
    return False


# Delete a user from the database


async def delete_user(id: str):
    # db = await database.db_connection()
    user = await User.find_one({"_id": PyObjectId(id)})
    if user:
        await User.delete_one({"_id": PyObjectId(id)})
        return True
    else:
        return False


def to_user(item) -> dict:
    return {
        "id": str(item.get("_id")),
        "userid": item.get("userid"),
        "password": item.get("password"),
        "company": item.get("company"),
        "permission": item.get("password"),
        "price": item.get("price"),
        "created_at": item.get("created_at"),
        "created_by": item.get("created_by"),
        "updated_at": item.get("updated_at"),
        "updated_by": item.get("updated_by")
    }


def to_user_list(items) -> list:
    return [to_user(item) for item in items]
