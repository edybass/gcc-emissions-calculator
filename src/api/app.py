"""
GHG Calculator API
RESTful API for greenhouse gas emissions calculations
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, Dict
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.calculator import GHGCalculator

# Create FastAPI app
app = FastAPI(
    title="GHG Emissions Calculator API",
    description="Calculate greenhouse gas emissions following GHG Protocol standards",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize calculator
calculator = GHGCalculator()


# Request models
class Scope1Request(BaseModel):
    fuel_type: str
    amount: float
    unit: str


class Scope2Request(BaseModel):
    electricity_kwh: float
    location: str
    method: str = "location_based"


class Scope3Request(BaseModel):
    category: str
    distance: Optional[float] = None
    mode: Optional[str] = None


# API endpoints
@app.get("/")
async def root():
    """Welcome endpoint."""
    return {
        "message": "GHG Emissions Calculator API",
        "documentation": "/docs",
        "endpoints": {
            "/api/calculate/scope1": "Calculate Scope 1 emissions",
            "/api/calculate/scope2": "Calculate Scope 2 emissions",
            "/api/calculate/scope3": "Calculate Scope 3 emissions",
            "/api/factors": "Get emission factors",
            "/api/report": "Get emissions report"
        }
    }


@app.post("/api/calculate/scope1")
async def calculate_scope1(request: Scope1Request):
    """Calculate Scope 1 direct emissions."""
    try:
        result = calculator.calculate_scope1(
            request.fuel_type,
            request.amount,
            request.unit
        )
        return {
            "success": True,
            "emissions_tco2e": round(result.total, 3),
            "scope": result.scope,
            "category": result.category,
            "activity": result.activity
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/calculate/scope2")
async def calculate_scope2(request: Scope2Request):
    """Calculate Scope 2 indirect emissions."""
    try:
        result = calculator.calculate_scope2(
            request.electricity_kwh,
            request.location,
            request.method
        )
        return {
            "success": True,
            "emissions_tco2e": round(result.total, 3),
            "scope": result.scope,
            "category": result.category,
            "activity": result.activity,
            "method": request.method
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/calculate/scope3")
async def calculate_scope3(request: Scope3Request):
    """Calculate Scope 3 value chain emissions."""
    try:
        kwargs = {}
        if request.distance is not None:
            kwargs["distance"] = request.distance
        if request.mode is not None:
            kwargs["mode"] = request.mode

        result = calculator.calculate_scope3(request.category, **kwargs)
        return {
            "success": True,
            "emissions_tco2e": round(result.total, 3),
            "scope": result.scope,
            "category": result.category,
            "activity": result.activity
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/factors")
async def get_emission_factors():
    """Get available emission factors."""
    return calculator.emission_factors


@app.get("/api/report")
async def get_report():
    """Get current emissions report."""
    totals = calculator.get_total_emissions()
    return {
        "summary": {
            "scope1": round(totals["scope1"], 3),
            "scope2": round(totals["scope2"], 3),
            "scope3": round(totals["scope3"], 3),
            "total": round(totals["total"], 3)
        },
        "details": [
            {
                "scope": r.scope,
                "category": r.category,
                "activity": r.activity,
                "emissions_tco2e": round(r.value, 3)
            }
            for r in calculator.results
        ]
    }


@app.delete("/api/clear")
async def clear_results():
    """Clear all calculation results."""
    calculator.clear_results()
    return {"success": True, "message": "Results cleared"}


# Mount static files for web interface
if Path("docs").exists():
    app.mount("/", StaticFiles(directory="docs", html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
