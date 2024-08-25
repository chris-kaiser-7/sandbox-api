from typing import Union, Any, Optional
import openai

a = Union[str, None]
b = Optional[str]
c = str | None
print(openai)

print(type(a))
print(type(b))
print(type(c))