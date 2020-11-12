#!/bin/sh
echo ----- CLI-setup Beginning -----

pip3 install -r core/requirements.txt

python3 core/setup.py

echo ----- CLI-setup Complete! -----