from typing import Optional, Text,List
from fastapi import Body, FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.routing import Host
import uvicorn
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, Form



app = FastAPI()
    
class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None
    tags: List[str]=[]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

items = {"foo": "The Foo Wrestlers"}
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:

        raise HTTPException(status_code=404, detail="Item not found")

    return {"item": items[item_id]}

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


@app.get('/blog')
def index(limit=10, published: bool=True, sort:Optional[str]= None):
    if published:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit}  from the the database'}


@app.get('/blog/unpublished')     
def unpublished():
    return {'data':'all unpublished blogs'}     


@app.get('/blog/{blog_id}')
def about(blog_id: int):
         return {'Data': blog_id}


@app.get('/blog/{blog_id}/comments')
def comments(blog_id, limit=10):
        return limit
        return{'Data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    tags: list = []
    published: Optional[bool]  
         

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"blog is created with title as{blog.title}"}         


if __name__ == "__main__":
    uvicorn.run(app)




        
