## Typehints (without pydantic)

# type_hint
basic usage of hints, e.g. | , ->, dict[ , ]

# type_dict, type alias
use type alias for convenience (NewType)
inherit TypedDict, use dict to define data structure

TypedDict is an example of alias, but it only supports:
1) dict
2) can't use methods like dataclass 
3) hint, not validation

# data_classes
# placeholder
use class syntax to represent data structure
compare generic placeholder Any vs. TypeVar
TypeVar keeps the input and output type information consistent

# third-party lib example: request
mypy may/maynot check the data type of third party packages
(in the latest udpate, it seems requests package can be checked)
in that case, may need to install sub for type check of specific package 
