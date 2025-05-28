#!/bin/bash
# Update GitHub repository settings

echo "📋 Updating GitHub repository settings..."

# Update repository description and topics
gh repo edit edybass/gcc-emissions-calculator \
  --description "🌍 Professional GHG emissions calculator for UAE & Saudi Arabia. Calculate Scope 1, 2, 3 emissions with region-specific factors." \
  --homepage "https://edybass.github.io/gcc-emissions-calculator/" \
  --topics "ghg-calculator,carbon-emissions,sustainability,uae,saudi-arabia,climate-change,greenhouse-gas,net-zero,scope-1-2-3,ghg-protocol"

# Make repository public
echo "🌍 Making repository public..."
gh repo edit edybass/gcc-emissions-calculator --visibility public

echo "✅ Repository settings updated!"
echo "🔗 Visit: https://github.com/edybass/gcc-emissions-calculator"
