#!/bin/sh

. ./iot_venv/bin/activate

# avoid to stuck raspberry cpus
export OPENBLAS_NUM_THREADS=1
export OPENBLAS_MAIN_FREE=1

cd master/slave
python3 main.py &

cd ..
python3 main.py &
