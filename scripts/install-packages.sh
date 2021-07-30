#!/bin/bash
set -euo pipefail

# No interaction
export DEBIAN_FRONTEND=noninteractive

# Update and install
apt-get update
apt-get -y upgrade
apt-get -y install --no-install-recommends curl build-essential
echo "Can we haz cache naow??/ Trust the process."

# Cleanup
apt-get clean
rm -rf /var/lib/apt/lists/*
