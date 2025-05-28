#!/usr/bin/env python3
"""
Enhanced GHG Calculator for GCC Region
Improved version with better functionality and error handling
Author: Edy Bassil
Email: bassileddy@gmail.com
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union, Tuple
from datetime import datetime
from enum import Enum
import json
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class EmissionScope(Enum):
    """Enumeration for emission scopes."""
    SCOPE_1 = 1
    SCOPE_2 = 2
    SCOPE_3 = 3


class CalculationMethod(Enum):
    """Enumeration for calculation methods."""
    LOCATION_BASED = "location_based"
    MARKET_BASED = "market_based"


@dataclass
class EmissionResult:
    """Enhanced container for emission calculation results."""
    value: float  # in tCO2e
    scope: EmissionScope
    category: str
    activity: str
    methodology: str = "GHG Protocol"
    uncertainty: Optional[float] = None
    calculation_date: datetime = field(default_factory=datetime.now)
    metadata: Dict = field(default_factory=dict)
    
    @property
    def total(self) -> float:
        """Get total emissions value."""
        return round(self.value, 3)
    
    @property
    def value_with_uncertainty(self) -> Tuple[float, float]:
        """Get value with uncertainty range."""
        if self.uncertainty:
            lower = self.value * (1 - self.uncertainty)
            upper = self.value * (1 + self.uncertainty)
            return (round(lower, 3), round(upper, 3))
        return (self.total, self.total)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "value_tco2e": self.total,
            "scope": self.scope.value,
            "category": self.category,
            "activity": self.activity,
            "methodology": self.methodology,
            "uncertainty": self.uncertainty,
            "calculation_date": self.calculation_date.isoformat(),
            "metadata": self.metadata
        }


class GHGCalculator:
    """Enhanced GHG emissions calculator for GCC region."""
    
    # Class constants for better maintainability
    DEFAULT_UNCERTAINTY = 0.05  # 5% default uncertainty
    GWP_VALUES = {  # AR6 values
        "CO2": 1,
        "CH4": 29.8,
        "N2O": 273,
        "R410A": 2088,
        "R404A": 3922,
        "R134a": 1430,
        "R32": 675,
        "SF6": 25200
    }
    
    def __init__(self, factors_path: Optional[str] = None, region: str = "GCC"):
        """
        Initialize calculator with emission factors.
        
        Args:
            factors_path: Path to emission factors JSON file
            region: Region for calculations (default: GCC)
        """
        self.factors_path = factors_path or "data/emission_factors/factors.json"
        self.region = region
        self.emission_factors = self._load_emission_factors()
        self.results: List[EmissionResult] = []
        self._validate_factors()
        logger.info(f"GHG Calculator initialized for region: {region}")
    
    def _load_emission_factors(self) -> Dict:
        """Load emission factors from JSON file with error handling."""
        factors_file = Path(self.factors_path)
        
        if factors_file.exists():
            try:
                with open(factors_file, 'r', encoding='utf-8') as f:
                    factors = json.load(f)
                logger.info(f"Loaded emission factors from {self.factors_path}")
                return factors
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing emission factors: {e}")
                return self._get_default_factors()
        else:
            logger.warning(f"Emission factors file not found: {self.factors_path}")
            return self._get_default_factors()
    
    def _validate_factors(self):
        """Validate loaded emission factors."""
        required_keys = ["fuels", "electricity", "transport", "gwp"]
        missing_keys = [key for key in required_keys if key not in self.emission_factors]
        
        if missing_keys:
            logger.warning(f"Missing emission factor categories: {missing_keys}")
            # Fill in missing categories with defaults
            default_factors = self._get_default_factors()
            for key in missing_keys:
                self.emission_factors[key] = default_factors.get(key, {})
    
    def _get_default_factors(self) -> Dict:
        """Get comprehensive default emission factors for GCC region."""
        return {
            "fuels": {
                "natural_gas": {
                    "co2": 56.1,
                    "ch4": 0.001,
                    "n2o": 0.0001,
                    "heating_value": 0.0373,
                    "unit": "GJ/m3",
                    "uncertainty": 0.02
                },
                "diesel": {
                    "co2": 74.1,
                    "ch4": 0.003,
                    "n2o": 0.0006,
                    "heating_value": 0.0381,
                    "unit": "GJ/L",
                    "uncertainty": 0.03
                },
                "gasoline": {
                    "co2": 69.3,
                    "ch4": 0.003,
                    "n2o": 0.0006,
                    "heating_value": 0.0342,
                    "unit": "GJ/L",
                    "uncertainty": 0.03
                },
                "lpg": {
                    "co2": 63.1,
                    "ch4": 0.001,
                    "n2o": 0.0001,
                    "heating_value": 0.0474,
                    "unit": "GJ/kg",
                    "uncertainty": 0.02
                },
                "fuel_oil": {
                    "co2": 77.4,
                    "ch4": 0.003,
                    "n2o": 0.0006,
                    "heating_value": 0.0404,
                    "unit": "GJ/L",
                    "uncertainty": 0.03
                },
                "coal": {
                    "co2": 94.6,
                    "ch4": 0.001,
                    "n2o": 0.0015,
                    "heating_value": 0.0246,
                    "unit": "GJ/kg",
                    "uncertainty": 0.05
                },
                "kerosene": {
                    "co2": 71.9,
                    "ch4": 0.003,
                    "n2o": 0.0006,
                    "heating_value": 0.0367,
                    "unit": "GJ/L",
                    "uncertainty": 0.03
                }
            },
            "electricity": {
                # UAE Factors
                "UAE": {"factor": 0.450, "uncertainty": 0.05, "renewable_share": 0.05},
                "Dubai": {"factor": 0.440, "uncertainty": 0.04, "renewable_share": 0.07},
                "Abu Dhabi": {"factor": 0.460, "uncertainty": 0.05, "renewable_share": 0.04},
                "Sharjah": {"factor": 0.455, "uncertainty": 0.05, "renewable_share": 0.03},
                "Northern Emirates": {"factor": 0.465, "uncertainty": 0.06, "renewable_share": 0.02},
                
                # Saudi Arabia Factors
                "Saudi Arabia": {"factor": 0.720, "uncertainty": 0.06, "renewable_share": 0.01},
                "Riyadh": {"factor": 0.710, "uncertainty": 0.05, "renewable_share": 0.02},
                "Jeddah": {"factor": 0.725, "uncertainty": 0.06, "renewable_share": 0.01},
                "Dammam": {"factor": 0.730, "uncertainty": 0.06, "renewable_share": 0.01},
                "NEOM": {"factor": 0.050, "uncertainty": 0.10, "renewable_share": 0.95},
                
                # Other GCC
                "Kuwait": {"factor": 0.750, "uncertainty": 0.07, "renewable_share": 0.01},
                "Qatar": {"factor": 0.490, "uncertainty": 0.05, "renewable_share": 0.01},
                "Bahrain": {"factor": 0.700, "uncertainty": 0.06, "renewable_share": 0.01},
                "Oman": {"factor": 0.680, "uncertainty": 0.06, "renewable_share": 0.01}
            },
            "transport": {
                "car_small": {"factor": 0.14, "unit": "kg CO2e/km", "occupancy": 1.5},
                "car_medium": {"factor": 0.17, "unit": "kg CO2e/km", "occupancy": 1.5},
                "car_large": {"factor": 0.21, "unit": "kg CO2e/km", "occupancy": 1.5},
                "suv": {"factor": 0.24, "unit": "kg CO2e/km", "occupancy": 2.0},
                "pickup_truck": {"factor": 0.28, "unit": "kg CO2e/km", "occupancy": 2.0},
                "bus_public": {"factor": 0.089, "unit": "kg CO2e/passenger-km", "occupancy": 40},
                "metro_dubai": {"factor": 0.027, "unit": "kg CO2e/passenger-km", "occupancy": 150},
                "metro_riyadh": {"factor": 0.030, "unit": "kg CO2e/passenger-km", "occupancy": 150},
                "taxi_dubai": {"factor": 0.18, "unit": "kg CO2e/km", "occupancy": 2},
                "taxi_riyadh": {"factor": 0.19, "unit": "kg CO2e/km", "occupancy": 2},
                "airplane_domestic": {"factor": 0.255, "unit": "kg CO2e/passenger-km"},
                "airplane_gcc": {"factor": 0.185, "unit": "kg CO2e/passenger-km"},
                "airplane_international": {"factor": 0.147, "unit": "kg CO2e/passenger-km"}
            },
            "cooling": {
                "district_cooling_uae": {"factor": 0.180, "unit": "kg CO2e/kWh"},
                "district_cooling_ksa": {"factor": 0.290, "unit": "kg CO2e/kWh"},
                "split_ac": {"factor": 0.450, "unit": "kg CO2e/kWh", "efficiency": "SEER 13"},
                "central_ac": {"factor": 0.420, "unit": "kg CO2e/kWh", "efficiency": "SEER 14"},
                "window_ac": {"factor": 0.480, "unit": "kg CO2e/kWh", "efficiency": "SEER 10"},
                "vrf_system": {"factor": 0.380, "unit": "kg CO2e/kWh", "efficiency": "SEER 18"}
            },
            "water": {
                "desalinated_water_uae": {"factor": 1.82, "unit": "kg CO2e/m3", "process": "MSF/RO"},
                "desalinated_water_ksa": {"factor": 2.15, "unit": "kg CO2e/m3", "process": "MSF"},
                "groundwater": {"factor": 0.35, "unit": "kg CO2e/m3"},
                "treated_wastewater": {"factor": 0.65, "unit": "kg CO2e/m3"},
                "bottled_water": {"factor": 0.23, "unit": "kg CO2e/L"}
            },
            "waste": {
                "landfill_uae": {"factor": 0.467, "unit": "kg CO2e/kg"},
                "landfill_ksa": {"factor": 0.485, "unit": "kg CO2e/kg"},
                "recycling": {"factor": -0.234, "unit": "kg CO2e/kg"},
                "composting": {"factor": 0.012, "unit": "kg CO2e/kg"},
                "incineration": {"factor": 0.908, "unit": "kg CO2e/kg"},
                "anaerobic_digestion": {"factor": -0.180, "unit": "kg CO2e/kg"}
            },
            "gwp": self.GWP_VALUES
        }
    
    def calculate_scope1(self, fuel_type: str, amount: float, unit: str,
                        custom_factor: Optional[float] = None) -> EmissionResult:
        """
        Calculate Scope 1 direct emissions from fuel combustion.
        
        Args:
            fuel_type: Type of fuel
            amount: Amount of fuel consumed
            unit: Unit of measurement
            custom_factor: Optional custom emission factor
            
        Returns:
            EmissionResult object with calculated emissions
        """
        if fuel_type not in self.emission_factors["fuels"] and not custom_factor:
            available_fuels = list(self.emission_factors["fuels"].keys())
            raise ValueError(
                f"Unknown fuel type: {fuel_type}. "
                f"Available fuels: {', '.join(available_fuels)}"
            )
        
        if custom_factor:
            # Use custom factor
            emissions = amount * custom_factor / 1000
            uncertainty = self.DEFAULT_UNCERTAINTY
            logger.info(f"Using custom emission factor: {custom_factor}")
        else:
            fuel_data = self.emission_factors["fuels"][fuel_type]
            gwp = self.emission_factors.get("gwp", self.GWP_VALUES)
            
            # Convert to energy content (GJ)
            energy_gj = amount * fuel_data["heating_value"]
            
            # Calculate emissions for each GHG
            co2_emissions = energy_gj * fuel_data["co2"] / 1000
            ch4_emissions = energy_gj * fuel_data["ch4"] * gwp.get("CH4", 29.8) / 1000
            n2o_emissions = energy_gj * fuel_data["n2o"] * gwp.get("N2O", 273) / 1000
            
            emissions = co2_emissions + ch4_emissions + n2o_emissions
            uncertainty = fuel_data.get("uncertainty", self.DEFAULT_UNCERTAINTY)
        
        result = EmissionResult(
            value=emissions,
            scope=EmissionScope.SCOPE_1,
            category="Stationary Combustion",
            activity=f"{amount} {unit} of {fuel_type}",
            uncertainty=uncertainty,
            metadata={
                "fuel_type": fuel_type,
                "amount": amount,
                "unit": unit,
                "energy_gj": energy_gj if not custom_factor else None
            }
        )
        
        self.results.append(result)
        logger.info(f"Scope 1 calculated: {result.total} tCO2e from {fuel_type}")
        return result
    
    def calculate_scope2(self, electricity_kwh: float, location: str,
                        method: CalculationMethod = CalculationMethod.LOCATION_BASED,
                        renewable_percentage: Optional[float] = None,
                        include_td_losses: bool = True) -> EmissionResult:
        """
        Calculate Scope 2 indirect emissions from purchased electricity.
        
        Args:
            electricity_kwh: Electricity consumption in kWh
            location: Location/grid
            method: Calculation method
            renewable_percentage: Override renewable percentage
            include_td_losses: Include transmission & distribution losses
            
        Returns:
            EmissionResult object
        """
        if location not in self.emission_factors["electricity"]:
            # Try to find a default for the country
            country = location.split(",")[0].strip()
            if country not in self.emission_factors["electricity"]:
                logger.warning(f"Unknown location: {location}. Using GCC average.")
                emission_data = {"factor": 0.600, "uncertainty": 0.10, "renewable_share": 0.02}
            else:
                emission_data = self.emission_factors["electricity"][country]
        else:
            emission_data = self.emission_factors["electricity"][location]
        
        # Get emission factor
        if isinstance(emission_data, dict):
            emission_factor = emission_data["factor"]
            uncertainty = emission_data.get("uncertainty", self.DEFAULT_UNCERTAINTY)
            default_renewable = emission_data.get("renewable_share", 0) * 100
        else:
            # Backwards compatibility
            emission_factor = emission_data
            uncertainty = self.DEFAULT_UNCERTAINTY
            default_renewable = 0
        
        # Apply method-specific adjustments
        if method == CalculationMethod.MARKET_BASED:
            renewable_pct = renewable_percentage if renewable_percentage is not None else default_renewable
            emission_factor *= (1 - renewable_pct / 100)
            logger.info(f"Market-based method: {renewable_pct}% renewable energy")
        
        # Include T&D losses (typically 5-8% in GCC)
        if include_td_losses:
            td_loss_factor = 1.06  # 6% average T&D losses
            electricity_kwh *= td_loss_factor
        
        # Calculate emissions
        emissions = electricity_kwh * emission_factor / 1000
        
        result = EmissionResult(
            value=emissions,
            scope=EmissionScope.SCOPE_2,
            category="Purchased Electricity",
            activity=f"{electricity_kwh:.0f} kWh in {location}",
            methodology=f"GHG Protocol - {method.value}",
            uncertainty=uncertainty,
            metadata={
                "location": location,
                "method": method.value,
                "renewable_percentage": renewable_pct if method == CalculationMethod.MARKET_BASED else None,
                "td_losses_included": include_td_losses,
                "emission_factor": emission_factor
            }
        )
        
        self.results.append(result)
        logger.info(f"Scope 2 calculated: {result.total} tCO2e from electricity in {location}")
        return result
    
    def calculate_scope3(self, category: str, **kwargs) -> EmissionResult:
        """
        Calculate Scope 3 value chain emissions.
        
        Args:
            category: Scope 3 category
            **kwargs: Category-specific parameters
            
        Returns:
            EmissionResult object
        """
        scope3_calculators = {
            "business_travel": self._calculate_business_travel,
            "employee_commute": self._calculate_employee_commute,
            "water_consumption": self._calculate_water_consumption,
            "waste_disposal": self._calculate_waste_disposal,
            "cooling": self._calculate_cooling
        }
        
        if category not in scope3_calculators:
            available = list(scope3_calculators.keys())
            raise ValueError(
                f"Unknown Scope 3 category: {category}. "
                f"Available categories: {', '.join(available)}"
            )
        
        return scope3_calculators[category](**kwargs)
    
    def _calculate_business_travel(self, distance: float, mode: str,
                                 return_trip: bool = False,
                                 passengers: int = 1) -> EmissionResult:
        """Calculate emissions from business travel."""
        if mode not in self.emission_factors["transport"]:
            raise ValueError(f"Unknown transport mode: {mode}")
        
        transport_data = self.emission_factors["transport"][mode]
        
        # Get emission factor
        if isinstance(transport_data, dict):
            emission_factor = transport_data["factor"]
            # For vehicles with occupancy, adjust by passengers
            if "occupancy" in transport_data and "passenger" not in transport_data["unit"]:
                emission_factor = emission_factor / transport_data["occupancy"] * passengers
        else:
            emission_factor = transport_data
        
        # Calculate total distance
        total_distance = distance * (2 if return_trip else 1)
        
        # Calculate emissions
        emissions = total_distance * emission_factor / 1000
        
        result = EmissionResult(
            value=emissions,
            scope=EmissionScope.SCOPE_3,
            category="Business Travel",
            activity=f"{total_distance} km by {mode.replace('_', ' ')}",
            uncertainty=0.10,  # Higher uncertainty for Scope 3
            metadata={
                "distance": distance,
                "mode": mode,
                "return_trip": return_trip,
                "passengers": passengers
            }
        )
        
        self.results.append(result)
        return result
    
    def _calculate_employee_commute(self, daily_distance: float, mode: str,
                                  working_days: int = 250,
                                  employees: int = 1) -> EmissionResult:
        """Calculate annual emissions from employee commuting."""
        # Use business travel calculator for the base calculation
        annual_distance = daily_distance * working_days * employees
        
        result = self._calculate_business_travel(
            distance=annual_distance,
            mode=mode,
            return_trip=True,
            passengers=1
        )
        
        # Update category
        result.category = "Employee Commuting"
        result.activity = f"{employees} employees, {daily_distance} km daily by {mode.replace('_', ' ')}"
        
        return result
    
    def _calculate_water_consumption(self, water_m3: float,
                                   water_type: str = "desalinated_water_uae") -> EmissionResult:
        """Calculate emissions from water consumption."""
        if water_type not in self.emission_factors["water"]:
            raise ValueError(f"Unknown water type: {water_type}")
        
        water_data = self.emission_factors["water"][water_type]
        emission_factor = water_data["factor"]
        
        emissions = water_m3 * emission_factor / 1000
        
        result = EmissionResult(
            value=emissions,
            scope=EmissionScope.SCOPE_3,
            category="Water Consumption",
            activity=f"{water_m3} m³ of {water_type.replace('_', ' ')}",
            uncertainty=0.15,
            metadata={
                "water_type": water_type,
                "volume_m3": water_m3,
                "process": water_data.get("process", "Unknown")
            }
        )
        
        self.results.append(result)
        return result
    
    def _calculate_waste_disposal(self, waste_kg: float,
                                disposal_method: str = "landfill_uae") -> EmissionResult:
        """Calculate emissions from waste disposal."""
        if disposal_method not in self.emission_factors["waste"]:
            raise ValueError(f"Unknown disposal method: {disposal_method}")
        
        waste_data = self.emission_factors["waste"][disposal_method]
        emission_factor = waste_data["factor"]
        
        emissions = waste_kg * emission_factor / 1000
        
        result = EmissionResult(
            value=emissions,
            scope=EmissionScope.SCOPE_3,
            category="Waste Disposal",
            activity=f"{waste_kg} kg via {disposal_method.replace('_', ' ')}",
            uncertainty=0.20,  # High uncertainty for waste
            metadata={
                "disposal_method": disposal_method,
                "waste_kg": waste_kg
            }
        )
        
        self.results.append(result)
        return result
    
    def _calculate_cooling(self, cooling_kwh: float,
                         cooling_type: str = "split_ac") -> EmissionResult:
        """Calculate emissions from cooling systems."""
        if cooling_type not in self.emission_factors["cooling"]:
            raise ValueError(f"Unknown cooling type: {cooling_type}")
        
        cooling_data = self.emission_factors["cooling"][cooling_type]
        emission_factor = cooling_data["factor"]
        
        emissions = cooling_kwh * emission_factor / 1000
        
        result = EmissionResult(
            value=emissions,
            scope=EmissionScope.SCOPE_3,
            category="Cooling Systems",
            activity=f"{cooling_kwh} kWh from {cooling_type.replace('_', ' ')}",
            uncertainty=0.10,
            metadata={
                "cooling_type": cooling_type,
                "consumption_kwh": cooling_kwh,
                "efficiency": cooling_data.get("efficiency", "Unknown")
            }
        )
        
        self.results.append(result)
        return result
    
    def get_total_emissions(self) -> Dict[str, Union[float, Dict]]:
        """Get total emissions by scope with statistics."""
        scope_totals = {
            "scope1": sum(r.value for r in self.results if r.scope == EmissionScope.SCOPE_1),
            "scope2": sum(r.value for r in self.results if r.scope == EmissionScope.SCOPE_2),
            "scope3": sum(r.value for r in self.results if r.scope == EmissionScope.SCOPE_3),
        }
        
        total = sum(scope_totals.values())
        
        # Calculate uncertainty (simplified - should use proper error propagation)
        if self.results:
            avg_uncertainty = sum(r.uncertainty or 0.05 for r in self.results) / len(self.results)
        else:
            avg_uncertainty = 0.05
        
        return {
            "totals": scope_totals,
            "total": round(total, 3),
            "uncertainty": round(avg_uncertainty, 3),
            "calculation_count": len(self.results),
            "breakdown": {
                "scope1_pct": round(scope_totals["scope1"] / total * 100, 1) if total > 0 else 0,
                "scope2_pct": round(scope_totals["scope2"] / total * 100, 1) if total > 0 else 0,
                "scope3_pct": round(scope_totals["scope3"] / total * 100, 1) if total > 0 else 0
            }
        }
    
    def generate_report(self, filename: str = "emissions_report.json",
                       format: str = "json", include_recommendations: bool = True):
        """
        Generate comprehensive emissions report.
        
        Args:
            filename: Output filename
            format: Output format (json, csv, html)
            include_recommendations: Include reduction recommendations
        """
        summary = self.get_total_emissions()
        
        report = {
            "report_metadata": {
                "generated_at": datetime.now().isoformat(),
                "generated_by": "GCC GHG Emissions Calculator",
                "author": "Edy Bassil",
                "email": "bassileddy@gmail.com",
                "methodology": "GHG Protocol Corporate Standard",
                "region": self.region
            },
            "executive_summary": {
                "total_emissions_tco2e": summary["total"],
                "uncertainty": f"±{summary['uncertainty']*100:.1f}%",
                "scope_breakdown": summary["breakdown"],
                "calculation_count": summary["calculation_count"]
            },
            "detailed_results": [r.to_dict() for r in self.results],
            "emissions_by_scope": summary["totals"]
        }
        
        if include_recommendations:
            report["recommendations"] = self._generate_recommendations(summary)
        
        # Save report
        if format == "json":
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Report generated: {filename}")
        return report
    
    def _generate_recommendations(self, summary: Dict) -> List[Dict]:
        """Generate emission reduction recommendations."""
        recommendations = []
        
        # Scope 1 recommendations
        if summary["totals"]["scope1"] > 0:
            recommendations.append({
                "scope": 1,
                "category": "Fuel Switching",
                "recommendation": "Consider switching to cleaner fuels like natural gas or renewable energy",
                "potential_reduction": "10-30%",
                "priority": "High" if summary["breakdown"]["scope1_pct"] > 40 else "Medium"
            })
        
        # Scope 2 recommendations
        if summary["totals"]["scope2"] > 0:
            recommendations.append({
                "scope": 2,
                "category": "Renewable Energy",
                "recommendation": "Install solar panels or purchase renewable energy certificates",
                "potential_reduction": "50-100%",
                "priority": "High" if summary["breakdown"]["scope2_pct"] > 30 else "Medium"
            })
            recommendations.append({
                "scope": 2,
                "category": "Energy Efficiency",
                "recommendation": "Upgrade to efficient cooling systems and LED lighting",
                "potential_reduction": "15-25%",
                "priority": "Medium"
            })
        
        # Scope 3 recommendations
        if summary["totals"]["scope3"] > 0:
            recommendations.append({
                "scope": 3,
                "category": "Transportation",
                "recommendation": "Promote electric vehicles and public transportation",
                "potential_reduction": "20-40%",
                "priority": "Medium"
            })
        
        return recommendations
    
    def clear_results(self):
        """Clear all calculation results."""
        self.results = []
        logger.info("Calculation results cleared")
    
    def get_emission_factor_info(self, category: str, subcategory: str) -> Dict:
        """Get detailed information about a specific emission factor."""
        if category not in self.emission_factors:
            raise ValueError(f"Unknown category: {category}")
        
        if subcategory not in self.emission_factors[category]:
            raise ValueError(f"Unknown subcategory: {subcategory} in {category}")
        
        return self.emission_factors[category][subcategory]


# Utility functions for common calculations
def calculate_annual_emissions(calculator: GHGCalculator,
                             facility_data: Dict) -> Dict:
    """
    Calculate annual emissions for a facility.
    
    Args:
        calculator: GHGCalculator instance
        facility_data: Dictionary with facility consumption data
        
    Returns:
        Summary of annual emissions
    """
    # Clear previous results
    calculator.clear_results()
    
    # Scope 1 - Fuels
    if "fuels" in facility_data:
        for fuel in facility_data["fuels"]:
            calculator.calculate_scope1(
                fuel_type=fuel["type"],
                amount=fuel["annual_amount"],
                unit=fuel["unit"]
            )
    
    # Scope 2 - Electricity
    if "electricity" in facility_data:
        elec = facility_data["electricity"]
        calculator.calculate_scope2(
            electricity_kwh=elec["annual_kwh"],
            location=elec["location"],
            method=CalculationMethod[elec.get("method", "LOCATION_BASED").upper()],
            renewable_percentage=elec.get("renewable_percentage")
        )
    
    # Scope 3 - Various
    if "transport" in facility_data:
        for transport in facility_data["transport"]:
            calculator.calculate_scope3(
                category="business_travel",
                distance=transport["annual_distance"],
                mode=transport["mode"]
            )
    
    if "water" in facility_data:
        calculator.calculate_scope3(
            category="water_consumption",
            water_m3=facility_data["water"]["annual_m3"],
            water_type=facility_data["water"].get("type", "desalinated_water_uae")
        )
    
    return calculator.get_total_emissions()


# Example usage
if __name__ == "__main__":
    # Create calculator instance
    calc = GHGCalculator()
    
    # Example facility data
    facility = {
        "name": "Dubai Manufacturing Facility",
        "fuels": [
            {"type": "natural_gas", "annual_amount": 50000, "unit": "m3"},
            {"type": "diesel", "annual_amount": 10000, "unit": "L"}
        ],
        "electricity": {
            "annual_kwh": 1000000,
            "location": "Dubai",
            "method": "market_based",
            "renewable_percentage": 10
        },
        "transport": [
            {"mode": "car_medium", "annual_distance": 50000},
            {"mode": "airplane_gcc", "annual_distance": 10000}
        ],
        "water": {
            "annual_m3": 5000,
            "type": "desalinated_water_uae"
        }
    }
    
    # Calculate annual emissions
    results = calculate_annual_emissions(calc, facility)
    
    # Generate report
    report = calc.generate_report("dubai_facility_emissions.json")
    
    print(f"\n{'='*50}")
    print(f"Total Annual Emissions: {results['total']} tCO2e")
    print(f"Uncertainty: ±{results['uncertainty']*100:.1f}%")
    print(f"{'='*50}")
    print(f"Scope 1: {results['totals']['scope1']:.2f} tCO2e ({results['breakdown']['scope1_pct']}%)")
    print(f"Scope 2: {results['totals']['scope2']:.2f} tCO2e ({results['breakdown']['scope2_pct']}%)")
    print(f"Scope 3: {results['totals']['scope3']:.2f} tCO2e ({results['breakdown']['scope3_pct']}%)")
    print(f"{'='*50}")