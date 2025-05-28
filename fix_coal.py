import json

# Load existing factors
with open("data/emission_factors/factors.json", "r") as f:
    factors = json.load(f)

# Add coal if missing
if "coal" not in factors["fuels"]:
    factors["fuels"]["coal"] = {
        "co2": 94.6,
        "ch4": 0.001,
        "n2o": 0.0015,
        "heating_value": 0.0246,
        "unit": "GJ/kg",
        "source": "IPCC 2006"
    }

# Save back
with open("data/emission_factors/factors.json", "w") as f:
    json.dump(factors, f, indent=2)

print("✅ Fixed emission factors to include coal")