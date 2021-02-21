#!/usr/bin/env bash

# Install pyenv
## https://github.com/pyenv/pyenv/wiki#suggested-build-environment
apt-get update; apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc

# Install
## https://github.com/pyenv/pyenv

# Install dependencies the specified python version, and use that version in shell
pyenv install 3.8.5
pyenv shell 3.8.5

# upgrade pip and install pipenv
python -m pip install --upgrade pip
pip install pipenv==2020.11.15

# Create virual environment and install dev_dependencies
pipenv install

# Execute from the current directory to start virtual dev environment: $pipenv shell
