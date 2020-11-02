import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1

proc = subprocess.run(["ping", "127.0.0.1"], capture_output=True, text=True)
print(proc.stdout)