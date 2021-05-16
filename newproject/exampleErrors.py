from fastapi import FastAPI, HTTPException
import uvicorn

err = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@err.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:

        raise HTTPException(status_code=404, detail="Item not found")

    return {"item": items[item_id]}

if __name__ == "__main__":
    uvicorn.run(err, host="127.0.0.1", port=9400)
