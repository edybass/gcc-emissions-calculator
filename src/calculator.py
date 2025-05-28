"""
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
    print(f"\nTotal emissions: {totals['total']:.2f} tCO2e")

    # Generate report
    calculator.generate_report()
