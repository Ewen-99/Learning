from datetime import datetime, UTC
from pydantic import BaseModel, ValidationError, Field
from typing import Literal

class BlogPost(BaseModel):
    title: str
    content: str
    view_count: int = 0
    is_publish: bool = False

    # Field
    tags: list[str] = Field(default_factory=list)   # can use [], but this is not a good habit, should use default_factory 

    create_at: datetime = Field(default_factory=lambda: datetime.now(UTC))  # or Field(default_factory=partial(datetime.now, tz=UTC))

    # Union
    author_id: str | int

    # Literal
    status: Literal['draft', 'published', 'archieved'] = 'draft'


post = BlogPost(
    title='Getting Started with Python',
    content="Here's how to begin",
    author_id="12345",
)
print(post)