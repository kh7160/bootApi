from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

import openApi


class Item(BaseModel):
    name:str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item:Item):
    print(item.name)
    print(item.description)
    print(item.price)
    print(item.tax)
    return item

@app.get("/")
async def hello_word():
    img = "2.png"
    return FileResponse(img)

@app.get("/openapi")
async def open_api():
    openApi.open_api()
    return FileResponse("2.png")
