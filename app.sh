#!/bin/bash
echo "=== Running CI Tests ==="

# Check if index.html exists
if [ -f "index.html" ]; then
    echo "✓ Success: index.html exists."
else
    echo "✗ Error: index.html is missing!"
    exit 1
fi

# Check if the HTML contains a valid heading status
if grep -q "Status:" index.html; then
    echo "✓ Success: Application status header found."
    exit 0
else
    echo "✗ Error: Critical application status text is missing!"
    exit 1
fi
