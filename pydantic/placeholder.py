from typing import NewType, Literal, Any, TypeVar
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
        first_name=first_name, 
        last_name=last_name,
        gender=gender,
        email=email,
        age=age,
        fav_color=fav_color
    )

# NOTE choice 1: we can use Any
# Mypy basically checks nothing  here
def random_choice(items: list[Any]) -> Any:
    return random.choice(items)

# NOTE choice 2: we can use TypeVar
# we still accept anything as input
# but, TypeVar keeps the input and output type information consistent
T = TypeVar("T")
def random_choice2(items: list[T]) -> T:
    return random.choice(items)

# The TypeVar placeholder can also be used simply this way, even without importing TypeVar lib
def random_choice3[T](items: list[T]) -> T:
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
          "\nIf we use Any in the function for checking"
          "\nMypy will not notice the emails are wrongly feeded into the fucntion"
          "\n---", e)
