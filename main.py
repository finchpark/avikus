from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    
@app.get("/")
async def read_root():
    return "This is root path from MyAPI"

@app.get("/vessels/{id}")
async def read_vessel(id: int, q: Union[str,  None] = None):
    return {"id": id, "q": q}

@app.post("/vessels/")
async def create_vessel(item: Item):
    return item

@app.put("/vessels/{id}")
async def update_vessel(id: int, item: Item):
    result = {"id": id, **item.dict()}

@app.delete("/vessels/{id}")
def delete_vessel(id: int):
    return {"deleted": id}