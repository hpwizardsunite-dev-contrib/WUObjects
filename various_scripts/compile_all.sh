#!/bin/bash
# Compile all WUProto files to python.
set -e

OUT_DIR="output/"

FILES=$(find WUProtos -type f -name "*.proto")

for proto in $FILES; do
    echo $proto;
    protoc --python_out="$OUT_DIR" "$proto";
done

ROOT="output"
for DIR in $(find $ROOT -type d); do
    touch $DIR/__init__.py
done