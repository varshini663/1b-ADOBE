#!/bin/bash

# Persona-Driven Document Intelligence System - Test Runner
# This script runs all test cases and validates the system functionality

echo "=========================================="
echo "Persona-Driven Document Intelligence System"
echo "Test Suite Runner"
echo "=========================================="

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed or not in PATH"
    exit 1
fi

# Check if required packages are installed
echo "Checking dependencies..."
python -c "import PyPDF2, sentence_transformers, numpy, sklearn, pandas" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Create output directory if it doesn't exist
mkdir -p sample_output

echo ""
echo "Running test cases..."
echo "=========================================="

# Run the test cases
python test_cases.py

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "All tests completed successfully!"
    echo "Check the generated JSON files for results."
    echo "=========================================="
else
    echo ""
    echo "=========================================="
    echo "Some tests failed. Check the error messages above."
    echo "=========================================="
    exit 1
fi

# Display summary of generated files
echo ""
echo "Generated output files:"
ls -la test_output_*.json 2>/dev/null || echo "No test output files found"

echo ""
echo "Sample output file:"
ls -la sample_output/challenge1b_output.json 2>/dev/null || echo "Sample output file not found"

echo ""
echo "Test run completed!" 