"""
Basic GHG Calculation Example
Calculate emissions for a small office in Dubai
"""

from src.calculator import GHGCalculator

# Initialize calculator
calc = GHGCalculator()

print("=== Small Office in Dubai - Annual Emissions ===\n")

# Scope 1: Natural gas for water heating
print("Scope 1 - Natural Gas:")
scope1 = calc.calculate_scope1("natural_gas", 500, "m3")
print(f"  Emissions: {scope1.total} tCO2e\n")

# Scope 2: Electricity
print("Scope 2 - Electricity:")
scope2 = calc.calculate_scope2(
    electricity_kwh=25000,
    location="Dubai",
    method="location_based"
)
print(f"  Emissions: {scope2.total} tCO2e\n")

# Scope 3: Employee commuting
print("Scope 3 - Employee Commuting:")
scope3 = calc.calculate_scope3(
    category="employee_commute",
    daily_distance=30,  # Average round trip
    mode="car_medium",
    working_days=250,
    employees=10
)
print(f"  Emissions: {scope3.total} tCO2e\n")

# Total
totals = calc.get_total_emissions()
print(f"Total Annual Emissions: {totals['total']} tCO2e")
print(f"  Scope 1: {totals['breakdown']['scope1_pct']}%")
print(f"  Scope 2: {totals['breakdown']['scope2_pct']}%")
print(f"  Scope 3: {totals['breakdown']['scope3_pct']}%")

# Generate report
calc.generate_report("small_office_dubai.json")
print("\nReport saved as small_office_dubai.json")
