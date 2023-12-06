from pydantic import BaseModel
from wikipedia import *


class Path(BaseModel):
    name: str
    surname: str


class Query(BaseModel):
    name: str
    surname: str
    result_search_wiki: wikipedia.search(name, surname)


class Fullname(BaseModel):
    name: str
    surname: str
    age: int


class Birth(BaseModel):
    fullname: Fullname
    date: int
    result_search_wiki: wikipedia.search(fullname, date)