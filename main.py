from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.models import StrategyInput, Influencer
from app.data_service import analyze_strategy_and_match

app = FastAPI(title="Influencer Marketing Strateji Uygulaması")

# Enable CORS for frontend accessibility (though we serve static from same origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Endpoints
@app.post("/api/analyze", response_model=List[Influencer])
async def analyze_strategy(strategy: StrategyInput):
    """
    Analyzes the input strategy and returns a list of recommended influencers.
    """
    try:
        results = analyze_strategy_and_match(strategy)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

# Serve static files (Frontend)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
