import sys
import subprocess
import psutil
import time

min_value = 300
max_value = 1023

def set_vibrance(value=min_value):
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

def is_csgo():
    x=[p.name() for p in psutil.process_iter()]
    if "csgo_linux64" in x:
        return True
    else: return False

while 1:
    try:
        if is_csgo() and get_vibrance_value() != max_value:
            set_vibrance(max_value)
        elif is_csgo() == False and get_vibrance_value() != min_value:
            set_vibrance()
        time.sleep(1)
    except:
        pass
