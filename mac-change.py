import subprocess

subprocess.call("ifconfig enp0s3 down", sheel=True)
subprocess.call("ifconfig enp0s3  hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig enp0s3 up", shell=True)