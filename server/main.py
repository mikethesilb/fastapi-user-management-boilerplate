import uvicorn
from fastapi import FastAPI

import users.router as users_router

app = FastAPI()
users_router.include_router(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, log_level="info")
