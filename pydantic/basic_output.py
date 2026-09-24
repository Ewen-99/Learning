from datetime import datetime
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    # required field
    uid: int
    username: str
    email: str

    # option field (with default values)
    verified_at: datetime | None = None

    bio: str = ""
    is_active: bool = True
    full_name: str | None = None

# example of a user class
user = User(
    uid=123,
    username="ewen",
    email="ewen@gmail.com,"
)
print(user)

#-- Output --#

# can use dot attribute as a class object
print(user.uid)

# "model_dump" into a dictionary
print(type(user.model_dump()))
print(user.model_dump())

# model_dump_json
print(user.model_dump_json(indent = 2))