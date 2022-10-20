from dataclasses import dataclass

from datetime import date, datetime

@dataclass
class User:
    id: int
    name: str
    email: str
    gender: str
    status: str
