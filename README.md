# 🌍 UAE & KSA GHG Emissions Calculator

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
source venv/bin/activate  # On Windows: venv\Scripts\activate

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
