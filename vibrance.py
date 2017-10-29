import sys
import subprocess

x = [i for i in sys.argv]

def set_vibrance(value=300):
    line=f"nvidia-settings -a \"DigitalVibrance={value}\" \
        > /dev/null"
    subprocess.check_output(
            ['bash', '-c', line]
            )
    print(f"nvidia-settings vibrance value was set to {value}.")

if __name__ == "__main__":
    try: set_vibrance(int(x[1]))
    except (ValueError, IndexError) as e:
        set_vibrance()

