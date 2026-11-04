#!/usr/bin/env bash

# Exit immediately if any command exits with a non-zero status
set -e

# Default configurations
DEFAULT_PORT="/dev/ttyUSB0"
PROFILE_DIR="profiles"
OUTPUT_DIR="output"

print_status() {
    echo -e "\033[1;34m[*] $1\033[0m"
}

print_success() {
    echo -e "\033[1;32m[+] $1\033[0m"
}

print_error() {
    echo -e "\033[1;31m[-] $1\033[0m"
}

# Ensure arguments are provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <operator_name> [serial_port]"
    echo "Available Operators: liquefaction, holonomy_vortex, hallucination_curvature, spectral_cascade, symbolic_drift, collapse_surface, conceptual_fusion, potential_field, dream_diagnostic"
    exit 1
fi

OPERATOR=$1
PORT=${2:-$DEFAULT_PORT}
PROFILE_PATH="${PROFILE_DIR}/dream_${OPERATOR}.json"
GCODE_PATH="${OUTPUT_DIR}/${OPERATOR}_plot.gcode"

# 1. Environment Verification
if [ ! -d "venv" ]; then
    print_status "Local environment missing. Bootstrapping workspace..."
    make env
fi

# Activate virtual environment
source venv/bin/activate

# 2. Match profile file strings cleanly
# Handle prefix naming variations dynamically
if [ "$OPERATOR" == "liquefaction" ]; then PROFILE_PATH="profiles/dream_04_liquefaction.json"; fi
if [ "$OPERATOR" == "holonomy_vortex" ]; then PROFILE_PATH="profiles/dream_07_vortex.json"; fi
if [ "$OPERATOR" == "hallucination_curvature" ]; then PROFILE_PATH="profiles/dream_01_curvature.json"; fi
if [ "$OPERATOR" == "spectral_cascade" ]; then PROFILE_PATH="profiles/dream_06_cascade.json"; fi
if [ "$OPERATOR" == "symbolic_drift" ]; then PROFILE_PATH="profiles/dream_05_drift.json"; fi
if [ "$OPERATOR" == "collapse_surface" ]; then PROFILE_PATH="profiles/dream_08_collapse.json"; fi
if [ "$OPERATOR" == "dream_diagnostic" ]; then PROFILE_PATH="profiles/dream_09_diagnostic.json"; fi

if [ ! -f "$PROFILE_PATH" ]; then
    print_error "Target dream profile matrix configuration not found: $PROFILE_PATH"
    exit 1
fi

# 3. Geometric Verification Suite Execution
print_status "Executing geometric safety assertions..."
pytest tests/test_geometry.py -q

# 4. Pipeline Compilation Loop
print_status "Compiling high-dimensional manifold space via operator: '${OPERATOR}'..."
python3 src/ndh_surrealism/core.py --input "$PROFILE_PATH" --output "$GCODE_PATH"
print_success "Upgraded G-code generated successfully at: $GCODE_PATH"

# 5. Serial Streaming Push
read -p "Connect to hardware rig and stream G-code to $PORT? (y/N): " confirm
if [[ $confirm =~ ^[Yy]$ ]]; then
    print_status "Streaming instructions to painting robot..."
    python3 -m ndh_surrealism.hardware.streamer --file "$GCODE_PATH"
    print_success "Canvas plot execution complete."
else
    print_status "Streaming bypassed. G-code file retained for offline visualization."
fi
