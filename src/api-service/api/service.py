import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Setup FastAPI app
app = FastAPI(title="API Server", description="API Server", version="v1")

# Enable CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    print("Startup tasks")


# Routes
@app.get("/")
async def get_index():
    env_list = []
    for name, value in os.environ.items():
        env_list.append(f"{name}: {value}")

    return {
        "message": "Welcome to the API Service",
        "version": "v 2.3",
        "env_list": env_list,
    }
