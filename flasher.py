import os,time
run_count=[]
def flasher(n):
    for i in range(n):
        os.system("termux-torch on")
        run_count.append(i)
        print(run_count)
        print("Flash is on",i)
        time.sleep(0.2)
        os.system("termux-torch off")
flasher(10)
