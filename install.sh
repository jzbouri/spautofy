#!/usr/bin/env bash

sudo cp spautofy /usr/local/bin/spautofy
sudo chmod +x /usr/local/bin/spautofy
echo $PWD | tee $HOME/spautofylocation.txt
python3 -m venv .venv
pip install -e .
pip install -r requirements.txt