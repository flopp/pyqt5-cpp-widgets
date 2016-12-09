#!/bin/bash
# Example (see variable exports below):
#   QMAKE=qmake-qt5 PYTHON=python3 ./build.sh
#
# Note: custom library must be built with same version of Qt.

set -e

# Executable paths
export QMAKE=${QMAKE:-qmake}
export SIP=${SIP:-sip}
export PYTHON=${PYTHON:-python3}

# Project and library paths
export PROJECT_PATH=${PROJECT_PATH:-"$PWD/.."}
export LIBRARY_PATH=${LIBRARY_PATH:-"$PROJECT_PATH/custom"}
export SIP_FILE_PATH=${SIP_FILE_PATH:-"$PROJECT_PATH/python/custom.sip"}
export PYQT_INCLUDE_PATH=${PYQT_INCLUDE_PATH:-""}

# generate files
"$PYTHON" "$PROJECT_PATH/python/configure.py"

# build
"$QMAKE" .
make

# test
PYTHONPATH=$PWD "$PYTHON" "test.py"
