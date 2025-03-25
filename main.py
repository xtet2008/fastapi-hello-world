from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World with FastAPI"}

@app.get("/hello/{name}")
async def read_name(name: str):
    return {"message": f"Hello {name}!"}
