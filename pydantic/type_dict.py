from typing import NewType, TypedDict, Literal

# NOTE create type alias
RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

# NOTE create typeddict
class User(TypedDict):
    first_name: str
    last_name: str
    gender: Literal["male", "female"]
    email: str
    age: int | None
    fav_color: RGB | None   # NOTE use type alias here

# type User = dict[str, str | int | None | RGB]

def create_user(
        first_name: str,
        last_name: str,
        gender: Literal["male", "female"],
        age: int | None = None,
        fav_color: RGB | None = None
) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "email": email,
        "age": age,
        "fav_color":fav_color
    }

user = create_user(
    first_name="Corey",
    last_name="Schafer",
    gender="male",
    age=38,
    fav_color=(109, 123, 134)
)

print(user)
print(type(user))