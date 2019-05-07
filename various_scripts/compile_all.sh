#!/bin/bash
# Compile all WUProto files to python.
# TODO: add __init__.py files to all subfolders
set -e

OUT_DIR="output/"

FILES=$(find WUProtos -type f -name "*.proto")

for proto in $FILES; do
    echo $proto;
    protoc --python_out="$OUT_DIR" "$proto";
done