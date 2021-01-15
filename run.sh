#!/bin/bash
echo '---------------------------------'
python healthy_everyday_docker.py
while [[ $? -eq 1 ]]; do
    python healthy_everyday_docker.py
done
