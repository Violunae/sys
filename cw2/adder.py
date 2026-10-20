import os, time

filename = "/home/violunae/Desktop/dev/uni/sys/adder_test.txt"

try:
    os.remove(filename)
except:
    pass

open(filename, "a").close()

num = 0
with open(filename, "a") as file:
    while True:
        file.write(f"{str(num)}\n")
        file.flush()
        print(f"Written line: {str(num)}")
        num += 1
        time.sleep(1.0)


