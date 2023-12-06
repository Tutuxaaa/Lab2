from fastapi import FastAPI
from models import *
from wikipedia import *

app = FastAPI()


@app.get("/{name}/{surname}")
def with_path(name: str, surname: str):
    p = Path(name=name, surname=surname)
    return p, wikipedia.search(p)


@app.get("/query")
def with_query(name: str, surname: str):
    q = Query(name=name, surname=surname)
    return q, wikipedia.search(q)


@app.post("/cls")
def with_class(fullname: Fullname):
    b = Birth(fullname=fullname, date=2023-fullname.age)
    return b, wikipedia.search(b)
