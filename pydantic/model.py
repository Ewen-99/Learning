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

#-- Validation --#
# use try except to deal with validation errors
try:
    user_2 = User(
        uid='user_2',
        username=None,
        email=123
    )
except ValidationError as e:
    print(e)


# the default model don't validate rechanged variables (unless otherwise set)
user.bio = 123
print(user.bio)
