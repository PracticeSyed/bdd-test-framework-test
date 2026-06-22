#!/bin/bash

# 🎭 Playwright BDD Framework Runner
# This script automates the complete framework execution

set -e  # Exit on error

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🎭 Playwright BDD Test Framework${NC}"
echo "=================================="
echo ""

# Step 1: Check prerequisites
echo -e "${YELLOW}[1/5] Checking prerequisites...${NC}"
command -v python3 >/dev/null 2>&1 || { echo -e "${RED}❌ Python3 required${NC}"; exit 1; }
command -v pip >/dev/null 2>&1 || { echo -e "${RED}❌ pip required${NC}"; exit 1; }
echo -e "${GREEN}✓ Prerequisites OK${NC}"
echo ""

# Step 2: Install dependencies
echo -e "${YELLOW}[2/5] Installing dependencies...${NC}"
cd tests/bdd
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -q -r requirements.txt
playwright install chromium --with-deps
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Step 3: Extract DOM
echo -e "${YELLOW}[3/5] Extracting DOM...${NC}"
cd utils
python dom_extractor.py
cd ..
echo -e "${GREEN}✓ DOM extracted${NC}"
echo ""

# Step 4: Generate page objects
echo -e "${YELLOW}[4/5] Generating page objects...${NC}"
python utils/page_object_generator.py
echo -e "${GREEN}✓ Page objects generated${NC}"
echo ""

# Step 5: Run tests
echo -e "${YELLOW}[5/5] Running tests...${NC}"
cd ../..
python run_tests.py

echo ""
echo -e "${GREEN}✅ Framework execution complete!${NC}"
echo -e "📊 Check reports in: tests/bdd/reports/"
