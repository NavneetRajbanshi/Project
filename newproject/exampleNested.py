from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

top = FastAPI()



class Image(BaseModel):

    url: str

    name: str



class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)
    image: Optional[Image] = None


@top.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results  


if __name__ == '__main__':
    uvicorn.run(top, host ="127.0.0.1", port =9000)