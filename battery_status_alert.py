import subprocess
from playsound import playsound
import time
import tkinter as tk

t = 300


def system_battery_status_check():
    ## call acpi command  to find out the current battery status ##
    p = subprocess.Popen("acpi", stdout=subprocess.PIPE, shell=True)

    ## Talk with acpi command i.e. read data from stdout and stderr. Store this info in tuple ##
    ## Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.  ##
    ## Wait for process to terminate. The optional input argument should be a string to be sent to the child process, ##
    # or None, if no data should be sent to the child.
    (output, err) = p.communicate()

    ## Wait for date to terminate. Get return returncode ##
    p_status = p.wait()

    output = str(output).split(',')
    output = output[1].split('%')
    return int(output[0])


def system_adaptor_status():
    p = subprocess.Popen("acpi -a", stdout=subprocess.PIPE, shell=True)
    (adapt, err) = p.communicate()
    adapt = str(adapt)
    if 'on' in adapt:
        print("adaptor on ")
        return False
    else:
        return True


while(True):
    if system_battery_status_check() < 25 and system_adaptor_status():
        print('battery is low')
        playsound("./alert.wav")
        root = tk.Tk()
        root.geometry('300x200')
        root.title('Battery low !!!!!!')
        btn = tk.Button(root, text='Exit', command=root.destroy)
        btn.pack()
        root.mainloop()
        time.sleep(t)
