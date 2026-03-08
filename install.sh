#!/usr/bin/env bash

sudo cp spautofy /usr/local/bin/spautofy
chmod +x /usr/local/bin/spautofy
echo $PWD | tee $HOME/spautofylocation.txt
