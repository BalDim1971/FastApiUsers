from fastapi import FastAPI
from routers import user

app = FastAPI()

app.include_router(user.router)


@app.get("/")
async def read_root():
    return {"message": "Hello, User Management World!"}

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(
        "main:app",
        log_level="info",
        reload=True)
