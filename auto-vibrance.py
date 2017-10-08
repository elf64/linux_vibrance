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

def get_vibrance_value():
    x = str(subprocess.check_output(
    ['bash', '-c', 'nvidia-settings -q DigitalVibrance']
    )).split(" ")
    return int(x[5].replace(".\\n", ""))

csgo="csgo_linux64"
csgo_run=False
while 1:
    x=[p.name() for p in psutil.process_iter()]
    if csgo in x and csgo_run == False:
        csgo_run=True
        set_vibrance(1023)
    elif csgo not in x and get_vibrance_value() != 300:
        csgo_run=False
        set_vibrance()
    time.sleep(1)
