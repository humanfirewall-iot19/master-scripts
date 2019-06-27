#!/usr/bin/env python3

import os

curpath = os.path.dirname(os.path.abspath(__file__))

os.system("sudo apt install git python3 python3-dev python3-pip python3-venv")
os.system("sudo apt install libzbar-dev")
os.system("""sudo apt-get install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-numpy \
    zip""")

os.system("python3 -m venv %s/master_venv" % curpath)

with open("%s/master_init.sh" % curpath, "w") as f:
    f.write("""#!/bin/sh

. %s/bin/activate

# avoid to stuck raspberry cpus
export OPENBLAS_NUM_THREADS=1
export OPENBLAS_MAIN_FREE=1

cd %s/master
python3 main.py &

cd %s/master/slave
python3 main.py &
""" % (curpath, curpath, curpath))

os.system("chmod +x %s/master_init.sh" % curpath)

if os.uname()[4][:3] == "arm":
    os.system("python3 -m pip install https://github.com/humanfirewall-iot19/dlib-builds/raw/master/dlib-19.17.99-cp35-cp35m-linux_armv7l.whl")
    os.system("python3 -m pip install gpiozero")
    os.system("python3 -m pip install picamera")
    os.system("python3 -m pip install rpi.gpio")
    
    with open(os.expanduser("~/.profile"), "a") as f:
        f.write("\n%s/master_init.sh\n" % curpath)
else:
    os.system("python3 -m pip install https://github.com/humanfirewall-iot19/dlib-builds/raw/master/dlib-19.17.99-cp36-cp36m-linux_x86_64.whl")
    os.system("python3 -m pip install opencv-python")

os.system("python3 -m pip install -r requirements.txt")

os.system("cd %s && git clone --recursive https://github.com/humanfirewall-iot19/master && cd master && git submodule update --remote" % curpath)
