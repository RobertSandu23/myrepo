#!/bin/bash

if [ -e "bashcrc" ]; then
    counter=$(grep -o "StrictHostKeyChecking" bashcrc | wc -l)
    echo "counter: $counter"
else
    echo "File not found"
fi

