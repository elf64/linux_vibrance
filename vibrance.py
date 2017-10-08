import sys
import subprocess

x=[i for i in sys.argv]
def set_vibrance(value=300):
    line=f"nvidia-settings -a \"DigitalVibrance={value}\" \
        > /dev/null"
    subprocess.check_output(
            ['bash', '-c', line]
            )
    print(f"nvidia-settings vibrance value was set to {value}.")

if len(x) == 2:
    try:
        set_vibrance(int(x[1]))
    except ValueError:
        if x[1] == "on":
            set_vibrance(1023)
        else:
            set_vibrance()
else:
    print("No arguments or too many arguments.\
            \nSetting default vibrance value!")
    set_vibrance()
