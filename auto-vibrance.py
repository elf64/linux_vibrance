import sys
import subprocess
import psutil
import time
# This script turns on/off digital vibrance in nvidia-settings
#   when csgo starts/closes
VAL=1023
csgo="csgo_linux64"
ON=f"nvidia-settings -a \"DigitalVibrance={VAL}\" > /dev/null"
OFF=f"nvidia-settings -a \"DigitalVibrance=0\" > /dev/null"
csgo_run=False
off=True
while 1:
    x=[p.name() for p in psutil.process_iter()]
    if csgo in x and csgo_run==False:
        print("set 1023")
        csgo_run=True
        off=True
        subprocess.check_output(['bash', '-c', ON])
    if csgo not in x:
        if off==True:
            print("Set variables to False and 0 vibrance")
            csgo_run=False
            off=False
            subprocess.check_output(['bash', '-c', OFF])
    time.sleep(1)
