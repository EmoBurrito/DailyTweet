#!/usr/bin/env bash
working_dir=`dirname "$0"`
python3 -m venv ${working_dir}
source ${working_dir}/bin/activate
pip3 install -r ${working_dir}/requirements.txt
python3 ${working_dir}/main.py
deactivate
