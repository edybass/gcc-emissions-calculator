"""
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
