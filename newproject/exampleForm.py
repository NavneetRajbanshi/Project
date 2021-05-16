from fastapi import FastAPI, Form
import uvicorn


frm = FastAPI()


@frm.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


if __name__ == "__main__":
    uvicorn.run(frm, host="127.0.0.1", port=5000)
