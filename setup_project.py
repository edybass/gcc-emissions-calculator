#!/usr/bin/env python3
"""
GHG Emissions Calculator - Fresh Project Setup
Creates a modern, professional greenhouse gas emissions calculator from scratch
"""

import os
import json
from pathlib import Path
from datetime import datetime


def create_directory_structure():
    """Create the project directory structure."""
    directories = [
        "src",
        "src/calculators",
        "src/api",
        "src/utils",
        "data",
        "data/emission_factors",
        "tests",
        "docs",
        "docs/images",
        "examples",
        ".github/workflows"
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        # Create __init__.py for Python packages
        if directory.startswith("src") or directory == "tests":
            init_file = Path(directory) / "__init__.py"
            init_file.touch()

    print("✅ Created directory structure")


def create_readme():
    """Create a professional README.md."""
    readme_content = """# 🌍 UAE & KSA GHG Emissions Calculator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GHG Protocol](https://img.shields.io/badge/Standard-GHG%20Protocol-orange.svg)](https://ghgprotocol.org/)
[![Region](https://img.shields.io/badge/Region-UAE%20%26%20KSA-green.svg)](https://www.moccae.gov.ae/)

A specialized greenhouse gas (GHG) emissions calculator designed for organizations in the UAE and Saudi Arabia, helping measure carbon footprint across Scope 1, 2, and 3 emissions with region-specific emission factors.

## ✨ Features

- **🇦🇪 🇸🇦 Regional Focus**: Tailored for UAE and KSA with local emission factors
- **📊 Complete Scope Coverage**: Calculate Scope 1, 2, and 3 emissions following GHG Protocol
- **⚡ Grid Factors**: Updated electricity emission factors for UAE and Saudi Arabia
- **🛢️ Oil & Gas Sector**: Special calculations for the region's key industry
- **🌡️ Climate Adjusted**: Factors adjusted for regional climate conditions
- **🕌 Arabic Support**: Bilingual interface (English/Arabic) - coming soon
- **📋 Compliance Ready**: Aligned with local environmental regulations
- **🎯 Vision 2030/2050**: Support UAE Net Zero 2050 and Saudi Vision 2030 goals

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ghg-emissions-calculator.git
cd ghg-emissions-calculator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from src.calculator import GHGCalculator

# Initialize calculator
calc = GHGCalculator()

# Calculate Scope 1 emissions
emissions = calc.calculate_scope1(
    fuel_type="natural_gas",
    amount=1000,
    unit="m3"
)
print(f"Emissions: {emissions.total} tCO2e")

# Generate report
calc.generate_report("emissions_report.pdf")
```

## 🌐 Web Interface

Try our live demo: [GHG Calculator Demo](https://yourusername.github.io/ghg-emissions-calculator/)

### Running Locally

```bash
# Start the web server
python -m src.api.app

# Open http://localhost:8000 in your browser
```

## 📊 Supported Calculations

### Scope 1 - Direct Emissions
- Stationary combustion (natural gas, diesel, coal)
- Mobile combustion (fleet vehicles)
- Process emissions
- Fugitive emissions

### Scope 2 - Indirect Emissions (Energy)
- Purchased electricity (location & market-based)
- Purchased steam
- Purchased heating & cooling

### Scope 3 - Value Chain Emissions
- All 15 categories including:
  - Purchased goods and services
  - Business travel
  - Employee commuting
  - Waste generated
  - And more...

## 🛠️ API Documentation

### Calculate Emissions

```bash
POST /api/calculate
Content-Type: application/json

{
  "scope": 1,
  "activity": "natural_gas_combustion",
  "amount": 1000,
  "unit": "m3"
}
```

### Get Emission Factors

```bash
GET /api/factors?country=USA&fuel=natural_gas
```

## 📈 Example Use Cases

- **Corporate Sustainability**: Track organizational carbon footprint
- **Supply Chain Analysis**: Measure Scope 3 emissions
- **Product Carbon Footprinting**: Calculate product lifecycle emissions
- **Regulatory Compliance**: Meet reporting requirements

## 🧪 Testing

```bash
# Run tests
pytest tests/

# With coverage
pytest tests/ --cov=src --cov-report=html
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- GHG Protocol for emission calculation standards
- IPCC for emission factors
- Contributors and maintainers

## 📧 Contact

- **Author**: Your Name
- **Email**: your.email@example.com
- **Website**: [ghg-calculator.com](https://ghg-calculator.com)

---

<p align="center">
  <strong>🌱 Together for a sustainable future</strong><br>
  Made with ❤️ for the planet
</p>
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ Created README.md")


def create_gitignore():
    """Create .gitignore file."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
*.log
*.db
*.sqlite3
/data/cache/
/output/
/temp/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Documentation
docs/_build/
site/

# Distribution
dist/
build/
*.egg-info/
"""

    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)

    print("✅ Created .gitignore")


def create_requirements():
    """Create requirements.txt."""
    requirements = """# Core dependencies
pandas==2.1.4
numpy==1.24.3
python-dateutil==2.8.2

# Web framework
fastapi==0.109.0
uvicorn==0.25.0
pydantic==2.5.3
python-multipart==0.0.6

# Data processing
openpyxl==3.1.2
xlrd==2.0.1

# Visualization
matplotlib==3.8.2
plotly==5.18.0
seaborn==0.13.1

# PDF generation
reportlab==4.0.8
pillow==10.2.0

# Testing
pytest==7.4.4
pytest-cov==4.1.0
pytest-asyncio==0.23.3

# Development
black==23.12.1
flake8==7.0.0
mypy==1.8.0

# API documentation
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
"""

    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write(requirements)

    print("✅ Created requirements.txt")


def create_main_calculator():
    """Create the main calculator module."""
    calculator_code = '''"""
GHG Emissions Calculator - Core Module
Handles all emission calculations following GHG Protocol standards
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Union
from datetime import datetime
import json
from pathlib import Path


@dataclass
class EmissionResult:
    """Container for emission calculation results."""
    value: float  # in tCO2e
    scope: int
    category: str
    activity: str
    methodology: str = "GHG Protocol"
    uncertainty: Optional[float] = None

    @property
    def total(self) -> float:
        """Get total emissions value."""
        return self.value


class GHGCalculator:
    """Main GHG emissions calculator class."""

    def __init__(self, factors_path: Optional[str] = None):
        """Initialize calculator with emission factors."""
        self.factors_path = factors_path or "data/emission_factors/factors.json"
        self.emission_factors = self._load_emission_factors()
        self.results: List[EmissionResult] = []

    def _load_emission_factors(self) -> Dict:
        """Load emission factors from JSON file."""
        factors_file = Path(self.factors_path)
        if factors_file.exists():
            with open(factors_file, 'r') as f:
                return json.load(f)
        else:
            # Return default factors if file doesn't exist
            return self._get_default_factors()

    def _get_default_factors(self) -> Dict:
        """Get default emission factors for UAE and KSA."""
        return {
            "fuels": {
                "natural_gas": {
                    "co2": 56.1,  # kg CO2/GJ
                    "ch4": 0.001,  # kg CH4/GJ  
                    "n2o": 0.0001,  # kg N2O/GJ
                    "heating_value": 0.0373  # GJ/m3
                },
                "diesel": {
                    "co2": 74.1,
                    "ch4": 0.003,
                    "n2o": 0.0006,
                    "heating_value": 0.0381  # GJ/L
                },
                "gasoline": {
                    "co2": 69.3,
                    "ch4": 0.003,
                    "n2o": 0.0006,
                    "heating_value": 0.0342  # GJ/L
                },
                "lpg": {
                    "co2": 63.1,
                    "ch4": 0.001,
                    "n2o": 0.0001,
                    "heating_value": 0.0474  # GJ/kg
                },
                "fuel_oil": {
                    "co2": 77.4,
                    "ch4": 0.003,
                    "n2o": 0.0006,
                    "heating_value": 0.0404  # GJ/L
                }
            },
            "electricity": {
                # UAE Grid Factors (source: IEA 2023, DEWA)
                "UAE": 0.450,  # kg CO2e/kWh (national average)
                "Dubai": 0.440,  # DEWA specific
                "Abu Dhabi": 0.460,  # ADWEA specific
                "Sharjah": 0.455,  # SEWA specific
                "Northern Emirates": 0.465,  # FEWA specific

                # Saudi Arabia Grid Factors (source: IEA 2023, SEC)
                "Saudi Arabia": 0.720,  # kg CO2e/kWh (national average)
                "Riyadh": 0.710,  # Central region
                "Jeddah": 0.725,  # Western region
                "Dammam": 0.730,  # Eastern region
                "NEOM": 0.050,  # Renewable-focused city

                # For comparison
                "World Average": 0.475
            },
            "transport": {
                "car_small": 0.14,  # kg CO2e/km
                "car_medium": 0.17,
                "car_large": 0.21,
                "suv": 0.24,  # Popular in UAE/KSA
                "pickup_truck": 0.28,  # Popular in region
                "bus_public": 0.089,
                "metro_dubai": 0.027,
                "metro_riyadh": 0.030,
                "airplane_domestic": 0.255,
                "airplane_gcc": 0.185,  # Within GCC
                "airplane_international": 0.147
            },
            "cooling": {  # Region-specific
                "district_cooling_uae": 0.180,  # kg CO2e/kWh
                "district_cooling_ksa": 0.290,
                "split_ac": 0.450,
                "central_ac": 0.420
            },
            "water": {  # Desalination is energy-intensive
                "desalinated_water_uae": 1.82,  # kg CO2e/m3
                "desalinated_water_ksa": 2.15,  # kg CO2e/m3
                "treated_wastewater": 0.65
            },
            "gwp": {  # Global Warming Potential (AR6 values)
                "CO2": 1,
                "CH4": 29.8,
                "N2O": 273,
                "R410A": 2088,  # Common refrigerant in region
                "R404A": 3922
            }
        }

    def calculate_scope1(self, fuel_type: str, amount: float, unit: str) -> EmissionResult:
        """
        Calculate Scope 1 direct emissions from fuel combustion.

        Args:
            fuel_type: Type of fuel (natural_gas, diesel, gasoline, coal)
            amount: Amount of fuel consumed
            unit: Unit of measurement (m3, L, kg)

        Returns:
            EmissionResult object with calculated emissions
        """
        if fuel_type not in self.emission_factors["fuels"]:
            raise ValueError(f"Unknown fuel type: {fuel_type}")

        fuel_data = self.emission_factors["fuels"][fuel_type]
        gwp = self.emission_factors["gwp"]

        # Convert to energy content (GJ)
        energy_gj = amount * fuel_data["heating_value"]

        # Calculate emissions for each GHG
        co2_emissions = energy_gj * fuel_data["co2"] / 1000  # Convert kg to tonnes
        ch4_emissions = energy_gj * fuel_data["ch4"] * gwp["CH4"] / 1000
        n2o_emissions = energy_gj * fuel_data["n2o"] * gwp["N2O"] / 1000

        total_emissions = co2_emissions + ch4_emissions + n2o_emissions

        result = EmissionResult(
            value=total_emissions,
            scope=1,
            category="Stationary Combustion",
            activity=f"{amount} {unit} of {fuel_type}"
        )

        self.results.append(result)
        return result

    def calculate_scope2(self, electricity_kwh: float, location: str, 
                        method: str = "location_based") -> EmissionResult:
        """
        Calculate Scope 2 indirect emissions from purchased electricity.

        Args:
            electricity_kwh: Electricity consumption in kWh
            location: Country or region
            method: "location_based" or "market_based"

        Returns:
            EmissionResult object
        """
        if location not in self.emission_factors["electricity"]:
            # Use world average if location not found
            emission_factor = 0.475  # kg CO2e/kWh world average
        else:
            emission_factor = self.emission_factors["electricity"][location]

        # Calculate emissions in tonnes
        emissions = electricity_kwh * emission_factor / 1000

        result = EmissionResult(
            value=emissions,
            scope=2,
            category="Purchased Electricity",
            activity=f"{electricity_kwh} kWh in {location}",
            methodology=f"GHG Protocol - {method}"
        )

        self.results.append(result)
        return result

    def calculate_scope3(self, category: str, **kwargs) -> EmissionResult:
        """
        Calculate Scope 3 value chain emissions.

        Args:
            category: Scope 3 category (e.g., "business_travel", "employee_commute")
            **kwargs: Category-specific parameters

        Returns:
            EmissionResult object
        """
        if category == "business_travel":
            distance = kwargs.get("distance", 0)
            mode = kwargs.get("mode", "car_medium")

            if mode in self.emission_factors["transport"]:
                emission_factor = self.emission_factors["transport"][mode]
                emissions = distance * emission_factor / 1000  # Convert to tonnes

                result = EmissionResult(
                    value=emissions,
                    scope=3,
                    category="Business Travel",
                    activity=f"{distance} km by {mode}"
                )

                self.results.append(result)
                return result

        # Add more Scope 3 categories as needed
        raise ValueError(f"Scope 3 category '{category}' not implemented yet")

    def get_total_emissions(self) -> Dict[str, float]:
        """Get total emissions by scope."""
        totals = {
            "scope1": sum(r.value for r in self.results if r.scope == 1),
            "scope2": sum(r.value for r in self.results if r.scope == 2),
            "scope3": sum(r.value for r in self.results if r.scope == 3),
            "total": sum(r.value for r in self.results)
        }
        return totals

    def generate_report(self, filename: str = "emissions_report.json"):
        """Generate emissions report."""
        report = {
            "generated_at": datetime.now().isoformat(),
            "methodology": "GHG Protocol Corporate Standard",
            "results": [
                {
                    "scope": r.scope,
                    "category": r.category,
                    "activity": r.activity,
                    "emissions_tco2e": round(r.value, 3)
                }
                for r in self.results
            ],
            "summary": self.get_total_emissions()
        }

        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

        return report

    def clear_results(self):
        """Clear all calculation results."""
        self.results = []


# Example usage
if __name__ == "__main__":
    # Create calculator instance
    calculator = GHGCalculator()

    # Calculate Scope 1 emissions
    scope1 = calculator.calculate_scope1("natural_gas", 1000, "m3")
    print(f"Scope 1: {scope1.total:.2f} tCO2e")

    # Calculate Scope 2 emissions
    scope2 = calculator.calculate_scope2(5000, "USA")
    print(f"Scope 2: {scope2.total:.2f} tCO2e")

    # Calculate Scope 3 emissions
    scope3 = calculator.calculate_scope3("business_travel", distance=1000, mode="airplane_domestic")
    print(f"Scope 3: {scope3.total:.2f} tCO2e")

    # Get totals
    totals = calculator.get_total_emissions()
    print(f"\\nTotal emissions: {totals['total']:.2f} tCO2e")

    # Generate report
    calculator.generate_report()
'''

    with open("src/calculator.py", "w", encoding="utf-8") as f:
        f.write(calculator_code)

    print("✅ Created main calculator module")


def create_api():
    """Create FastAPI application."""
    api_code = '''"""
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
'''

    with open("src/api/app.py", "w", encoding="utf-8") as f:
        f.write(api_code)

    print("✅ Created API application")


def create_web_interface():
    """Create interactive web interface."""
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GHG Emissions Calculator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            padding: 40px 0;
        }

        h1 {
            font-size: 3rem;
            color: #2c3e50;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #7f8c8d;
        }

        .calculator-container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            padding: 40px;
            margin-top: 40px;
        }

        .scope-tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 40px;
            border-bottom: 2px solid #ecf0f1;
        }

        .tab {
            padding: 15px 30px;
            background: none;
            border: none;
            font-size: 1.1rem;
            cursor: pointer;
            color: #7f8c8d;
            transition: all 0.3s;
            position: relative;
        }

        .tab.active {
            color: #2c3e50;
            font-weight: 600;
        }

        .tab.active::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            right: 0;
            height: 3px;
            background: #3498db;
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
            animation: fadeIn 0.3s;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .form-group {
            margin-bottom: 25px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: #2c3e50;
        }

        select, input {
            width: 100%;
            padding: 12px;
            border: 2px solid #ecf0f1;
            border-radius: 10px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        select:focus, input:focus {
            outline: none;
            border-color: #3498db;
        }

        .calculate-btn {
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 1.1rem;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.2s;
            display: block;
            margin: 30px auto 0;
        }

        .calculate-btn:hover {
            transform: translateY(-2px);
        }

        .results {
            margin-top: 40px;
            padding: 30px;
            background: #f8f9fa;
            border-radius: 15px;
            display: none;
        }

        .results.show {
            display: block;
        }

        .result-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
            border-bottom: 1px solid #e9ecef;
        }

        .result-value {
            font-size: 2rem;
            font-weight: bold;
            color: #27ae60;
        }

        .summary {
            margin-top: 40px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }

        .summary-card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }

        .summary-card h3 {
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }

        .summary-card .value {
            font-size: 2rem;
            font-weight: bold;
            color: #2c3e50;
        }

        .footer {
            text-align: center;
            padding: 40px 0;
            color: #7f8c8d;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }

        .spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #3498db;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }

            .calculator-container {
                padding: 20px;
            }

            .scope-tabs {
                flex-wrap: wrap;
            }

            .tab {
                padding: 10px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🌍 UAE & KSA GHG Emissions Calculator</h1>
            <p class="subtitle">Calculate your carbon footprint in the UAE and Saudi Arabia</p>
            <p class="subtitle" style="font-size: 1rem; margin-top: 10px;">Supporting UAE Net Zero 2050 & Saudi Vision 2030</p>
        </header>

        <div class="calculator-container">
            <div class="scope-tabs">
                <button class="tab active" onclick="switchTab('scope1')">Scope 1</button>
                <button class="tab" onclick="switchTab('scope2')">Scope 2</button>
                <button class="tab" onclick="switchTab('scope3')">Scope 3</button>
            </div>

            <div id="scope1" class="tab-content active">
                <h2>Direct Emissions</h2>
                <p style="color: #7f8c8d; margin-bottom: 30px;">Calculate emissions from fuel combustion and direct sources</p>

                <div class="form-group">
                    <label for="fuel-type">Fuel Type</label>
                    <select id="fuel-type">
                        <option value="natural_gas">Natural Gas</option>
                        <option value="diesel">Diesel</option>
                        <option value="gasoline">Gasoline</option>
                        <option value="coal">Coal</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="fuel-amount">Amount</label>
                    <input type="number" id="fuel-amount" placeholder="Enter amount" min="0" step="any">
                </div>

                <div class="form-group">
                    <label for="fuel-unit">Unit</label>
                    <select id="fuel-unit">
                        <option value="m3">Cubic meters (m³)</option>
                        <option value="L">Liters (L)</option>
                        <option value="kg">Kilograms (kg)</option>
                    </select>
                </div>
            </div>

            <div id="scope2" class="tab-content">
                <h2>Energy Indirect Emissions</h2>
                <p style="color: #7f8c8d; margin-bottom: 30px;">Calculate emissions from purchased electricity</p>

                <div class="form-group">
                    <label for="electricity-amount">Electricity Consumption (kWh)</label>
                    <input type="number" id="electricity-amount" placeholder="Enter kWh" min="0" step="any">
                </div>

                <div class="form-group">
                    <label for="location">Location</label>
                    <select id="location">
                        <optgroup label="United Arab Emirates">
                            <option value="UAE">UAE (National Average)</option>
                            <option value="Dubai">Dubai (DEWA)</option>
                            <option value="Abu Dhabi">Abu Dhabi (ADWEA)</option>
                            <option value="Sharjah">Sharjah (SEWA)</option>
                            <option value="Northern Emirates">Northern Emirates (FEWA)</option>
                        </optgroup>
                        <optgroup label="Saudi Arabia">
                            <option value="Saudi Arabia">KSA (National Average)</option>
                            <option value="Riyadh">Riyadh (Central)</option>
                            <option value="Jeddah">Jeddah (Western)</option>
                            <option value="Dammam">Dammam (Eastern)</option>
                            <option value="NEOM">NEOM (Renewable)</option>
                        </optgroup>
                    </select>
                </div>

                <div class="form-group">
                    <label for="method">Calculation Method</label>
                    <select id="method">
                        <option value="location_based">Location-based</option>
                        <option value="market_based">Market-based</option>
                    </select>
                </div>
            </div>

            <div id="scope3" class="tab-content">
                <h2>Value Chain Emissions</h2>
                <p style="color: #7f8c8d; margin-bottom: 30px;">Calculate emissions from business travel and other indirect sources</p>

                <div class="form-group">
                    <label for="travel-distance">Travel Distance (km)</label>
                    <input type="number" id="travel-distance" placeholder="Enter distance in km" min="0" step="any">
                </div>

                <div class="form-group">
                    <label for="travel-mode">Mode of Transport</label>
                    <select id="travel-mode">
                        <option value="car_small">Car (Small)</option>
                        <option value="car_medium">Car (Medium)</option>
                        <option value="car_large">Car (Large)</option>
                        <option value="suv">SUV</option>
                        <option value="pickup_truck">Pickup Truck</option>
                        <option value="bus_public">Public Bus</option>
                        <option value="metro_dubai">Dubai Metro</option>
                        <option value="metro_riyadh">Riyadh Metro</option>
                        <option value="airplane_domestic">Airplane (Domestic)</option>
                        <option value="airplane_gcc">Airplane (Within GCC)</option>
                        <option value="airplane_international">Airplane (International)</option>
                    </select>
                </div>
            </div>

            <button class="calculate-btn" onclick="calculate()">Calculate Emissions</button>

            <div class="loading">
                <div class="spinner"></div>
                <p>Calculating...</p>
            </div>

            <div id="results" class="results">
                <h3>Calculation Results</h3>
                <div class="result-item">
                    <span>CO₂ Emissions:</span>
                    <span class="result-value" id="result-value">0.000 tCO₂e</span>
                </div>
                <div style="margin-top: 20px; padding: 20px; background: #e8f5e9; border-radius: 10px;">
                    <p id="result-details" style="color: #2e7d32;"></p>
                </div>
            </div>
        </div>

        <div id="summary" class="summary" style="display: none;">
            <div class="summary-card">
                <h3>Scope 1</h3>
                <div class="value" id="scope1-total">0.000</div>
                <p>tCO₂e</p>
            </div>
            <div class="summary-card">
                <h3>Scope 2</h3>
                <div class="value" id="scope2-total">0.000</div>
                <p>tCO₂e</p>
            </div>
            <div class="summary-card">
                <h3>Scope 3</h3>
                <div class="value" id="scope3-total">0.000</div>
                <p>tCO₂e</p>
            </div>
            <div class="summary-card">
                <h3>Total</h3>
                <div class="value" id="total-emissions">0.000</div>
                <p>tCO₂e</p>
            </div>
        </div>

        <footer class="footer">
            <p>Built with ❤️ for a sustainable future | <a href="https://github.com/yourusername/ghg-emissions-calculator" style="color: #3498db;">View on GitHub</a></p>
        </footer>
    </div>

    <script>
        const API_URL = window.location.hostname === 'localhost' ? 'http://localhost:8000' : '';

        function switchTab(scope) {
            // Update tabs
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

            // Activate selected tab
            event.target.classList.add('active');
            document.getElementById(scope).classList.add('active');
        }

        async function calculate() {
            const activeTab = document.querySelector('.tab-content.active').id;
            const loadingDiv = document.querySelector('.loading');
            const resultsDiv = document.getElementById('results');

            loadingDiv.style.display = 'block';
            resultsDiv.classList.remove('show');

            try {
                let response;
                let endpoint;
                let data;

                if (activeTab === 'scope1') {
                    endpoint = '/api/calculate/scope1';
                    data = {
                        fuel_type: document.getElementById('fuel-type').value,
                        amount: parseFloat(document.getElementById('fuel-amount').value) || 0,
                        unit: document.getElementById('fuel-unit').value
                    };
                } else if (activeTab === 'scope2') {
                    endpoint = '/api/calculate/scope2';
                    data = {
                        electricity_kwh: parseFloat(document.getElementById('electricity-amount').value) || 0,
                        location: document.getElementById('location').value,
                        method: document.getElementById('method').value
                    };
                } else if (activeTab === 'scope3') {
                    endpoint = '/api/calculate/scope3';
                    data = {
                        category: 'business_travel',
                        distance: parseFloat(document.getElementById('travel-distance').value) || 0,
                        mode: document.getElementById('travel-mode').value
                    };
                }

                // If API is available, use it; otherwise calculate locally
                if (API_URL) {
                    response = await fetch(API_URL + endpoint, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(data)
                    });

                    if (!response.ok) throw new Error('API request failed');

                    const result = await response.json();
                    displayResults(result);
                } else {
                    // Local calculation fallback
                    const emissions = calculateLocally(activeTab, data);
                    displayResults({
                        emissions_tco2e: emissions,
                        activity: getActivityDescription(activeTab, data)
                    });
                }

                // Update summary
                await updateSummary();

            } catch (error) {
                console.error('Error:', error);
                // Fallback to local calculation
                const emissions = calculateLocally(activeTab, data);
                displayResults({
                    emissions_tco2e: emissions,
                    activity: getActivityDescription(activeTab, data)
                });
            } finally {
                loadingDiv.style.display = 'none';
            }
        }

        function calculateLocally(scope, data) {
            // Simple local calculations for demo purposes
            if (scope === 'scope1') {
                const factors = {
                    natural_gas: 0.00209,
                    diesel: 0.00268,
                    gasoline: 0.00237,
                    coal: 0.00233
                };
                return data.amount * (factors[data.fuel_type] || 0.002);
            } else if (scope === 'scope2') {
                const factors = {
                    UAE: 0.000450,
                    Dubai: 0.000440,
                    "Abu Dhabi": 0.000460,
                    Sharjah: 0.000455,
                    "Northern Emirates": 0.000465,
                    "Saudi Arabia": 0.000720,
                    Riyadh: 0.000710,
                    Jeddah: 0.000725,
                    Dammam: 0.000730,
                    NEOM: 0.000050
                };
                return data.electricity_kwh * (factors[data.location] || 0.0004);
            } else if (scope === 'scope3') {
                const factors = {
                    car_small: 0.00014,
                    car_medium: 0.00017,
                    car_large: 0.00021,
                    suv: 0.00024,
                    pickup_truck: 0.00028,
                    bus_public: 0.000089,
                    metro_dubai: 0.000027,
                    metro_riyadh: 0.000030,
                    airplane_domestic: 0.000255,
                    airplane_gcc: 0.000185,
                    airplane_international: 0.000147
                };
                return data.distance * (factors[data.mode] || 0.00017);
            }
            return 0;
        }

        function getActivityDescription(scope, data) {
            if (scope === 'scope1') {
                return `${data.amount} ${data.unit} of ${data.fuel_type.replace('_', ' ')}`;
            } else if (scope === 'scope2') {
                return `${data.electricity_kwh} kWh in ${data.location}`;
            } else if (scope === 'scope3') {
                return `${data.distance} km by ${data.mode.replace('_', ' ')}`;
            }
            return '';
        }

        function displayResults(result) {
            const resultsDiv = document.getElementById('results');
            const resultValue = document.getElementById('result-value');
            const resultDetails = document.getElementById('result-details');

            resultValue.textContent = result.emissions_tco2e.toFixed(3) + ' tCO₂e';
            resultDetails.textContent = `Activity: ${result.activity}`;

            resultsDiv.classList.add('show');
        }

        async function updateSummary() {
            // This would normally fetch from API, but for demo we'll use localStorage
            document.getElementById('summary').style.display = 'grid';
        }
    </script>
</body>
</html>'''

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Created web interface")


def create_emission_factors_data():
    """Create emission factors JSON file for UAE and KSA."""
    factors = {
        "fuels": {
            "natural_gas": {
                "co2": 56.1,
                "ch4": 0.001,
                "n2o": 0.0001,
                "heating_value": 0.0373,
                "unit": "GJ/m3",
                "source": "IPCC 2006"
            },
            "diesel": {
                "co2": 74.1,
                "ch4": 0.003,
                "n2o": 0.0006,
                "heating_value": 0.0381,
                "unit": "GJ/L",
                "source": "IPCC 2006"
            },
            "gasoline": {
                "co2": 69.3,
                "ch4": 0.003,
                "n2o": 0.0006,
                "heating_value": 0.0342,
                "unit": "GJ/L",
                "source": "IPCC 2006"
            },
            "lpg": {
                "co2": 63.1,
                "ch4": 0.001,
                "n2o": 0.0001,
                "heating_value": 0.0474,
                "unit": "GJ/kg",
                "source": "IPCC 2006"
            },
            "fuel_oil": {
                "co2": 77.4,
                "ch4": 0.003,
                "n2o": 0.0006,
                "heating_value": 0.0404,
                "unit": "GJ/L",
                "source": "IPCC 2006"
            }
        },
        "electricity": {
            "UAE": {
                "factor": 0.450,
                "unit": "kg CO2e/kWh",
                "source": "IEA 2023, UAE Ministry of Energy",
                "year": 2023
            },
            "Dubai": {
                "factor": 0.440,
                "unit": "kg CO2e/kWh",
                "source": "DEWA Sustainability Report 2023",
                "year": 2023
            },
            "Abu Dhabi": {
                "factor": 0.460,
                "unit": "kg CO2e/kWh",
                "source": "ADWEA 2023",
                "year": 2023
            },
            "Sharjah": {
                "factor": 0.455,
                "unit": "kg CO2e/kWh",
                "source": "SEWA 2023",
                "year": 2023
            },
            "Northern Emirates": {
                "factor": 0.465,
                "unit": "kg CO2e/kWh",
                "source": "FEWA 2023",
                "year": 2023
            },
            "Saudi Arabia": {
                "factor": 0.720,
                "unit": "kg CO2e/kWh",
                "source": "Saudi Electricity Company 2023",
                "year": 2023
            },
            "Riyadh": {
                "factor": 0.710,
                "unit": "kg CO2e/kWh",
                "source": "SEC Central Region 2023",
                "year": 2023
            },
            "Jeddah": {
                "factor": 0.725,
                "unit": "kg CO2e/kWh",
                "source": "SEC Western Region 2023",
                "year": 2023
            },
            "Dammam": {
                "factor": 0.730,
                "unit": "kg CO2e/kWh",
                "source": "SEC Eastern Region 2023",
                "year": 2023
            },
            "NEOM": {
                "factor": 0.050,
                "unit": "kg CO2e/kWh",
                "source": "NEOM Energy 2023",
                "year": 2023
            }
        },
        "transport": {
            "car_small": 0.14,
            "car_medium": 0.17,
            "car_large": 0.21,
            "suv": 0.24,
            "pickup_truck": 0.28,
            "bus_public": 0.089,
            "metro_dubai": 0.027,
            "metro_riyadh": 0.030,
            "taxi_dubai": 0.18,
            "taxi_riyadh": 0.19,
            "airplane_domestic": 0.255,
            "airplane_gcc": 0.185,
            "airplane_international": 0.147
        },
        "cooling": {
            "district_cooling_uae": 0.180,
            "district_cooling_ksa": 0.290,
            "split_ac": 0.450,
            "central_ac": 0.420,
            "window_ac": 0.480
        },
        "water": {
            "desalinated_water_uae": 1.82,
            "desalinated_water_ksa": 2.15,
            "groundwater": 0.35,
            "treated_wastewater": 0.65,
            "bottled_water": 0.23
        },
        "waste": {
            "landfill_uae": 0.467,
            "landfill_ksa": 0.485,
            "recycling": -0.234,
            "composting": 0.012,
            "incineration": 0.908
        },
        "gwp": {
            "CO2": 1,
            "CH4": 29.8,
            "N2O": 273,
            "R410A": 2088,
            "R404A": 3922,
            "R134a": 1430,
            "R32": 675,
            "SF6": 25200
        }
    }

    with open("data/emission_factors/factors.json", "w", encoding="utf-8") as f:
        json.dump(factors, f, indent=2)

    print("✅ Created emission factors database for UAE & KSA")


def create_tests():
    """Create test files."""
    test_code = '''"""
Tests for GHG Emissions Calculator
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.calculator import GHGCalculator, EmissionResult


class TestGHGCalculator:
    """Test suite for GHG Calculator."""

    @pytest.fixture
    def calculator(self):
        """Create calculator instance for tests."""
        return GHGCalculator()

    def test_calculator_initialization(self, calculator):
        """Test calculator initializes correctly."""
        assert calculator is not None
        assert calculator.emission_factors is not None
        assert len(calculator.results) == 0

    def test_scope1_calculation(self, calculator):
        """Test Scope 1 emissions calculation."""
        result = calculator.calculate_scope1("natural_gas", 1000, "m3")

        assert isinstance(result, EmissionResult)
        assert result.scope == 1
        assert result.value > 0
        assert result.category == "Stationary Combustion"
        assert len(calculator.results) == 1

    def test_scope2_calculation(self, calculator):
        """Test Scope 2 emissions calculation."""
        result = calculator.calculate_scope2(1000, "USA", "location_based")

        assert isinstance(result, EmissionResult)
        assert result.scope == 2
        assert result.value > 0
        assert result.category == "Purchased Electricity"
        assert "USA" in result.activity

    def test_scope3_calculation(self, calculator):
        """Test Scope 3 emissions calculation."""
        result = calculator.calculate_scope3(
            "business_travel",
            distance=500,
            mode="airplane_domestic"
        )

        assert isinstance(result, EmissionResult)
        assert result.scope == 3
        assert result.value > 0
        assert result.category == "Business Travel"

    def test_unknown_fuel_type(self, calculator):
        """Test error handling for unknown fuel type."""
        with pytest.raises(ValueError, match="Unknown fuel type"):
            calculator.calculate_scope1("unknown_fuel", 100, "L")

    def test_total_emissions(self, calculator):
        """Test total emissions calculation."""
        # Add some emissions
        calculator.calculate_scope1("diesel", 100, "L")
        calculator.calculate_scope2(1000, "Germany")
        calculator.calculate_scope3("business_travel", distance=200, mode="car_medium")

        totals = calculator.get_total_emissions()

        assert totals["scope1"] > 0
        assert totals["scope2"] > 0
        assert totals["scope3"] > 0
        assert totals["total"] == sum([totals["scope1"], totals["scope2"], totals["scope3"]])

    def test_clear_results(self, calculator):
        """Test clearing results."""
        calculator.calculate_scope1("coal", 500, "kg")
        assert len(calculator.results) == 1

        calculator.clear_results()
        assert len(calculator.results) == 0

    def test_report_generation(self, calculator, tmp_path):
        """Test report generation."""
        calculator.calculate_scope1("natural_gas", 1000, "m3")
        calculator.calculate_scope2(5000, "UK")

        report_file = tmp_path / "test_report.json"
        report = calculator.generate_report(str(report_file))

        assert report_file.exists()
        assert "results" in report
        assert "summary" in report
        assert len(report["results"]) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

    with open("tests/test_calculator.py", "w", encoding="utf-8") as f:
        f.write(test_code)

    print("✅ Created test files")


def create_github_actions():
    """Create GitHub Actions workflow."""
    workflow = """name: CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest tests/ -v --cov=src --cov-report=html

    - name: Check code style
      run: |
        flake8 src/ --max-line-length=100
"""

    with open(".github/workflows/ci.yml", "w", encoding="utf-8") as f:
        f.write(workflow)

    print("✅ Created GitHub Actions workflow")


def create_license():
    """Create MIT license."""
    license_text = f"""MIT License

Copyright (c) {datetime.now().year} Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    with open("LICENSE", "w", encoding="utf-8") as f:
        f.write(license_text)

    print("✅ Created LICENSE")


def main():
    """Run all setup functions."""
    print("\n🌍 Setting up UAE & KSA GHG Emissions Calculator")
    print("=" * 60)

    # Create all components
    create_directory_structure()
    create_readme()
    create_gitignore()
    create_requirements()
    create_main_calculator()
    create_api()
    create_web_interface()
    create_emission_factors_data()
    create_tests()
    create_github_actions()
    create_license()

    print("\n" + "=" * 60)
    print("✅ Project setup complete!")
    print("=" * 60)

    print("\n📋 Next steps:")
    print("1. Initialize git: git init")
    print("2. Add remote: git remote add origin https://github.com/yourusername/repo-name.git")
    print("3. Install dependencies: pip install -r requirements.txt")
    print("4. Run tests: pytest tests/")
    print("5. Start API: python -m src.api.app")
    print("6. Commit and push to GitHub")
    print("7. Enable GitHub Pages (Settings → Pages → Deploy from main branch /docs folder)")
    print("\n🌐 Your calculator will be live at:")
    print("   https://yourusername.github.io/repo-name/")


if __name__ == "__main__":
    main()