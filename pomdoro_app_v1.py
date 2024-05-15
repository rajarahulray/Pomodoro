import tkinter as tk
import datetime as dt
import time


def break_popup(parent_window):
    ## Minimizing the parent window
    parent_window.wm_state('iconic')
    parent_window.iconify()

    ## setting popup time to 25 mins.
    t_end = time.time() + 60*25  
    
    while 1:
        if time.time() < t_end:
            pass;
        else:
            break_time = dt.datetime.now() + dt.timedelta(minutes=5)
            root = tk.Tk()
            root.title("Pomodoro Meesage")

            width= root.winfo_screenwidth() 
            height= root.winfo_screenheight()
            #setting tkinter window size
            root.geometry("%dx%d" % (width, height))
            # root.attributes("-fullscreen", True)    
            root.attributes('-alpha', 0.5)
            task = tk.Label(root,bg='red',fg='white', text = f"Break Time !!!\nLook away for 5 mins and come back at {break_time.strftime('%H:%M:%S')}")
            task.config(width=200, font=("Courier", 44))
            task.pack(side=tk.LEFT, expand=True)
            try:
                from ctypes import windll
                windll.shcore.SetProcessDpiAwareness(1)
            finally:
                root.mainloop()

root = tk.Tk()
root.title("Pomodoro Program")
root.geometry('600x400+50+50')
root.attributes('-alpha', 0.5)

button = tk.Button(root, text = "Activate Pomodoro Mode", command = lambda: break_popup(root))
button.pack(fill='x', expand=True, pady=10)

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
