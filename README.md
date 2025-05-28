# 🌍 GCC Emissions Calculator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GHG Protocol](https://img.shields.io/badge/Standard-GHG%20Protocol-orange.svg)](https://ghgprotocol.org/)
[![Region](https://img.shields.io/badge/Region-UAE%20%26%20KSA-green.svg)](https://www.moccae.gov.ae/)

> Professional greenhouse gas emissions calculator designed specifically for organizations in the UAE and Saudi Arabia. Calculate your carbon footprint across Scope 1, 2, and 3 emissions with region-specific emission factors.

## ✨ Key Features

### 🎯 Region-Specific Design
- **UAE Grid Factors**: Emirate-specific factors (DEWA, ADWEA, SEWA, FEWA)
- **Saudi Grid Factors**: Region-specific factors including NEOM renewable city
- **GCC Coverage**: Includes Kuwait, Qatar, Bahrain, and Oman
- **Climate Adapted**: Accounts for cooling needs and desalination

### 📊 Comprehensive Calculations
- **Scope 1**: Direct emissions from fuel combustion
- **Scope 2**: Indirect emissions from purchased electricity
- **Scope 3**: Value chain emissions including:
  - Business travel & employee commuting
  - Water consumption (desalination)
  - Waste disposal
  - Cooling systems

### 🛠️ Technical Features
- **Standards Compliant**: GHG Protocol & ISO 14064
- **RESTful API**: Easy integration with existing systems
- **Offline Capable**: Works without internet connection
- **Mobile Responsive**: Calculate on any device
- **Data Privacy**: All calculations performed locally

## 🚀 Live Demo

**Try it now: [https://edybass.github.io/gcc-emissions-calculator/](https://edybass.github.io/gcc-emissions-calculator/)**

## 📦 Installation

### For Web Use
Simply visit the [live calculator](https://edybass.github.io/gcc-emissions-calculator/) - no installation required!

### For Development

```bash
# Clone the repository
git clone https://github.com/edybass/gcc-emissions-calculator.git
cd gcc-emissions-calculator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Start API server (optional)
python -m src.api.app
```

## 💻 Usage Examples

### Basic Calculation (Python)

```python
from src.calculator import GHGCalculator

# Initialize calculator
calc = GHGCalculator()

# Calculate Scope 1 emissions
result = calc.calculate_scope1(
    fuel_type="natural_gas",
    amount=10000,
    unit="m3"
)
print(f"Emissions: {result.total} tCO2e")

# Calculate Scope 2 emissions
result = calc.calculate_scope2(
    electricity_kwh=50000,
    location="Dubai",
    method="market_based",
    renewable_percentage=10
)
print(f"Emissions: {result.total} tCO2e")
```

### API Usage

```bash
# Calculate Scope 1 emissions
curl -X POST http://localhost:8000/api/calculate/scope1 \
  -H "Content-Type: application/json" \
  -d '{
    "fuel_type": "diesel",
    "amount": 1000,
    "unit": "L"
  }'

# Get emission factors
curl http://localhost:8000/api/factors
```

### Comprehensive Facility Assessment

```python
# Annual facility assessment
facility_data = {
    "name": "Dubai Manufacturing Plant",
    "fuels": [
        {"type": "natural_gas", "annual_amount": 50000, "unit": "m3"},
        {"type": "diesel", "annual_amount": 10000, "unit": "L"}
    ],
    "electricity": {
        "annual_kwh": 1000000,
        "location": "Dubai",
        "method": "market_based",
        "renewable_percentage": 15
    },
    "transport": [
        {"mode": "car_medium", "annual_distance": 50000},
        {"mode": "airplane_gcc", "annual_distance": 20000}
    ],
    "water": {
        "annual_m3": 5000,
        "type": "desalinated_water_uae"
    }
}

results = calculate_annual_emissions(calc, facility_data)
print(f"Total Annual Emissions: {results['total']} tCO2e")
```

## 📊 Emission Factors

### Electricity Grid Factors (kg CO2e/kWh)

| Location | Factor | Source |
|----------|--------|--------|
| UAE (National) | 0.450 | IEA 2023 |
| Dubai (DEWA) | 0.440 | DEWA Sustainability Report |
| Abu Dhabi (ADWEA) | 0.460 | ADWEA 2023 |
| Saudi Arabia | 0.720 | SEC 2023 |
| NEOM | 0.050 | NEOM Energy |

### Fuel Emission Factors

All fuel factors follow IPCC 2006 guidelines with regional adjustments for fuel quality.

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test
pytest tests/test_calculator.py::TestGHGCalculator::test_scope2_calculation
```

## 📈 Roadmap

- [ ] Arabic language support
- [ ] Integration with UAE and KSA environmental reporting systems
- [ ] Scope 3 expansion (all 15 categories)
- [ ] Mobile app development
- [ ] Blockchain verification for carbon credits
- [ ] AI-powered reduction recommendations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Edy Bassil**
- Email: [bassileddy@gmail.com](mailto:bassileddy@gmail.com)
- GitHub: [@edybass](https://github.com/edybass)
- LinkedIn: [Edy Bassil](https://www.linkedin.com/in/edy-bassil/)

## 🙏 Acknowledgments

- **GHG Protocol** for comprehensive accounting standards
- **IPCC** for emission factor methodologies
- **UAE Ministry of Climate Change** for regional guidance
- **Saudi Green Initiative** for sustainability framework
- All contributors and users of this calculator

## 📚 References

1. GHG Protocol Corporate Standard (2015)
2. IPCC Guidelines for National GHG Inventories (2006)
3. UAE State of Energy Report (2023)
4. Saudi Electricity Company Annual Report (2023)
5. ISO 14064-1:2018 Specification with guidance

## 🌱 Supporting Sustainability Goals

This calculator supports:
- 🇦🇪 **UAE Net Zero 2050** Strategic Initiative
- 🇸🇦 **Saudi Vision 2030** & Saudi Green Initiative
- 🌍 **UN Sustainable Development Goals** (SDG 13: Climate Action)

---

<p align="center">
  <strong>Together for a sustainable GCC</strong><br>
  Made with ❤️ in the UAE
</p>
