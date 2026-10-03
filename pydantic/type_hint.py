
def create_user(
        first_name: str,
        last_name: str,
        age: int | None = None
) -> dict[str, str | int | None]:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age
    }

print(
create_user(
    first_name="Corey",
    last_name="Schafer",
)
)