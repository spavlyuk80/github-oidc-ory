from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root(request: Request):
    print(f"{request.client.host=}")
    print(f"{request.method=}")
    print(f"{request.headers=}")
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9000)