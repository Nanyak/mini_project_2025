from fastapi import FastAPI

from routers.users import router as users_router

app = FastAPI()

# Include users router
app.include_router(users_router)


# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}
