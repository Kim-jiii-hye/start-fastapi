from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
      "message": "Hello World",
      "version": "1.0.2"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)