import sys
import subprocess

VAL = 1023
ON = f"nvidia-settings -a \"DigitalVibrance={VAL}\" > /dev/null"
OFF = f"nvidia-settings -a \"DigitalVibrance=0\" > /dev/null"
if sys.argv[1] == "on":
    subprocess.check_output(['bash', '-c', ON])
elif sys.argv[1] == "off":
    subprocess.check_output(['bash', '-c', OFF])
else:
    print("Not a valid argument!\nTry to use \"on\" or \"off\"")

