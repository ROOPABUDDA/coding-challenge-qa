from enum import Enum
from typing import Dict

from pydantic import BaseModel


class UserType(str, Enum):
    STUDENT = "student"
    TUTOR = "tutor"
    DEVELOPER = "dev"
    UNKNOWN = "unknown"


class ClientCode(str, Enum):
    MS_TEAMS = "ms_teams"
    ALEXA = "alexa"
    NATIVE = "native"


class User(BaseModel):
    id: str
    type: UserType


class Client(BaseModel):
    code: ClientCode
    details: Dict


class Language(str, Enum):
    EN = "en"
    DE = "de"
