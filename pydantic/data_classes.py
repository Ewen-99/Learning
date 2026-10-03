from typing import NewType, Literal
from dataclasses import dataclass
import random

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

# use dataclass to give default values, add methods, ...
@dataclass
class User:
    first_name: str
    last_name: str
    gender: Literal["male", "female"]
    email: str
    age: int | None = None
    fav_color: RGB | None = None

# type User = dict[str, str | int | None | RGB]

def create_user(
        first_name: str,
        last_name: str,
        gender: Literal["male", "female"],
        age: int | None = None,
        fav_color: RGB | None = None
) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

# return a dataclass of User (rather than a dict)
    return User(
        first_name=first_name,  # NOTE notice the syntax is now class, not dict 
        last_name=last_name,
        gender=gender,
        email=email,
        age=age,
        fav_color=fav_color
    )

user = create_user(
    first_name="Corey",
    last_name="Schafer",
    gender="male",
    age=38,
    fav_color=(109, 123, 134)
)
print(user)
print(type(user))

# a simple example of applying dataclass into checking
def random_choice(items: list[User]) -> User:
    return random.choice(items)

# random_choice should be applied to dataclass User only
# but it does not stop running when getting inputs of emails
users = [create_user(first_name='john', last_name='abc', gender="male"), create_user(first_name='ben', last_name='def', gender="male")]
user = random_choice(users)
print(user)
print(user.gender)

emails = ['john@gmailcom', 'ben@gamil.com', 'lisa@gmail.com']
email = random_choice(emails)
print(email)
try:
    print(email.gender)
except AttributeError as e:
    print("--- Error Message: Logic"
          "\ndataclass doesn't stop the script running"
          "\nbut it notices the emails are applied with the wrong function"
          "\ngiven the defined dataclass User and type hints in random_choice function\n"
          "---", e)
