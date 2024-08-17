from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middleware import LoggingMiddleware
from routers import user, auth

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
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
