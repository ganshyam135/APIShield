from fastapi import FastAPI

app = FastAPI(
    title="APIShield",
    description="Backend-focused API management and observability platform.",
    version="0.1.0",
)

@app.get("/")
async def health_check():
    return {
        "status": "healthy"
    }

