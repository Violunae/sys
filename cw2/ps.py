import os
import pwd

print(f"{"USER":<8} {"PID":>7} {"COMMAND"}")

for pid in os.listdir("/proc"):
    if not pid.isdigit():
        continue

    proc_path = f"/proc/{pid}"

    try:
        with open(f"{proc_path}/status", "r") as f:
            status = f.readlines()

        uid = None
        for line in status:
            if line.startswith("Uid:"):
                uid = int(line.split()[1])
                break

        if uid is None:
            continue

        try:
            username = pwd.getpwuid(uid).pw_name
        except KeyError:
            username = str(uid)

        with open(f"{proc_path}/comm", "r") as f:
            command = f.read().strip()

        print(f"{username:<8} {pid:>7} {command}")

    except:
        continue