#!/usr/bin/env bash
set -e
timestamp=$(date +"%Y%m%d-%H%M%S")
docker compose logs > "logs-${timestamp}.txt"
tar -czf "logs-${timestamp}.tar.gz" "logs-${timestamp}.txt"
rm "logs-${timestamp}.txt"
