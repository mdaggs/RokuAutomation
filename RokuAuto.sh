#!/bin/bash
echo Starting Roku Automation
cd ..
cd bin
which python
python3 --version
source activate
sleep 2
cd ..
pwd
cd notebooks
python3 Roku_Automation2.py
echo Roku Automation Ended
