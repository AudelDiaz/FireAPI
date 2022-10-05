from codecs import unicode_escape_decode
from pydantic import BaseModel

class User(BaseModel):
    id: str
    first_name: str = None
    last_name: str = None
    email: str = None