from pydantic import BaseModel, Field
import random

class Bad(BaseModel):
    name: str = 'Bad'
    tags: list = [] #passing in [] is a bad habit

print(type(Bad()))
print(Bad())

User1 = Bad() 
print(User1)

User2 = Bad()
print(User2)


class Good(BaseModel):
    name: int = Field(default_factory=lambda: random.randint(1, 1000))
    tags: list = Field(default_factory=list)
    
print(type(Good()))
print(Good())

User1 = Good(tags=['python'])
print(User1)

User2 = Good(tags=['javascript'])
print(User2)
