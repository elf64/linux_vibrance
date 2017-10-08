import sys
import subprocess
import psutil
import time

def set_vibrance(value=300):
    line=f"nvidia-settings -a \"DigitalVibrance={value}\"\
            > /dev/null"
    subprocess.check_output(
            ['bash', '-c', line]
            )
    print(f"nvidia-settings vibrance value was set to {value}")

csgo="csgo_linux64"
csgo_run=False
off=True
while 1:
    x=[p.name() for p in psutil.process_iter()]
    if csgo in x and csgo_run == False:
        csgo_run=True
        off=True
        set_vibrance(1023)
    if csgo not in x and off == True:
            csgo_run=False
            off=False
            set_vibrance()
    time.sleep(1)
