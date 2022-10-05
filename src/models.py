from codecs import unicode_escape_decode
from pydantic import BaseModel

class User(BaseModel):
    uid: str
    first_name: str
    last_name: str
    email: str