import os

with open("/model/run.sh", "w") as f:
    f.write("cd /model\n")
    f.write("pip3 install -e .\n")

os.system("chmod 0777 /model/run.sh")
os.system("/model/run.sh")
