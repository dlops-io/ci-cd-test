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
    return {"message": "Welcome to the API Service v 2.0"}
