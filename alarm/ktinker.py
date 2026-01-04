import tkinter as tk
from logic import Timer, Stopwatch, Clock
from playsound import playsound
timer = Timer()
stopwatch = Stopwatch()
clock = Clock()

root = tk.Tk()
root.title("Timer/stopwatch")
root.geometry("500x400")


def show_frame(frame):
    frame.tkraise()

pages = []  

for i in range(4): 
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)
    pages.append(frame)

tk.Label(pages[0], text="Main menu", font=("Arial", 20)).pack(pady=20)

tk.Button(pages[0], text="Go to current time", width=25, height = 2, command=lambda: show_frame(pages[1])).pack(pady=15)

tk.Button(pages[0], text="Go to timer", width=25, height = 2, command=lambda: show_frame(pages[2])).pack(pady=15)

tk.Button(pages[0], text="Go to stopwatch", width=25, height = 2, command=lambda: show_frame(pages[3])).pack(pady=15)

time_label = tk.Label(pages[1], text="", font=("Arial", 40))
time_label.pack(pady=20)

def update_clock():
    time_label.config(text=clock.get_time())
    root.after(1000, update_clock)  # update every 1 second

update_clock()  
tk.Button(pages[1], text="Back", command=lambda: show_frame(pages[0])).pack(pady=15)

def play_alarm():
    threading.Thread(target=playsound, args=("alarm.mp3",), daemon=True).start()
    
timer_label = tk.Label(pages[2], text="00:00", font=("Arial", 40))
timer_label.pack(pady=20)
entry_label = tk.Label(pages[2], text="Enter time in seconds:", font=("Arial", 14))
entry_label.pack(pady=5)

time_entry = tk.Entry(pages[2], font=("Arial", 14))
time_entry.pack(pady=10)

def start_timer():
    
    if timer.running:
        return
    
    input_seconds = time_entry.get()  
    
    if input_seconds.isdigit():      
        my_seconds = int(input_seconds)
        timer.start(my_seconds)      
        update_timer()
    else:
        timer_label.config(text="Invalid input")

def reset_timer():
    timer.reset()            
    timer.seconds = 0       
    timer_label.config(text="00:00") 
    time_entry.delete(0, tk.END)
    
    
    

def update_timer():
    
    if not timer.running:
        return
    
    
    if timer.seconds > 0:
        minutes, seconds = divmod(timer.seconds, 60) #get quotient rema3idner 
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        timer.tick()
        root.after(1000, update_timer) #call update after 1s
    else:
        timer.running = False
        timer_label.config(text="Timer done")
        play_alarm()

tk.Button(pages[2], text="Start Timer", width=25, height = 2, command=start_timer).pack(pady=15)
tk.Button(pages[2], text="Reset Timer", width=25, height = 2, command=reset_timer).pack(pady=15)
tk.Button(pages[2], text="Back", width=25, height = 2, command=lambda: show_frame(pages[0])).pack(pady=15)


stopwatch_label = tk.Label(pages[3], text="00:00", font=("Arial", 40))
stopwatch_label.pack(pady=20)

def start_stopwatch():
     if stopwatch.running:
        return
    stopwatch.stop() 
    stopwatch.seconds = 0 
    stopwatch_label.config(text="00:00")
    stopwatch.start()
    update_stopwatch()

def end_stopwatch():
    stopwatch.stop()
    
    update_stopwatch()

def update_stopwatch():
    minutes, seconds = divmod(stopwatch.seconds, 60)
    stopwatch_label.config(text=f"{minutes:02d}:{seconds:02d}")
    stopwatch.tick()
    if stopwatch.running:
        root.after(1000, update_stopwatch)

tk.Button(pages[3], text="Start", width=25, height = 2, command=start_stopwatch).pack(pady=15)
tk.Button(pages[3], text="End",  width=25, height = 2, command=end_stopwatch).pack(pady=15)
tk.Button(pages[3], text="Back",  width=25, height = 2, command=lambda: show_frame(pages[0])).pack(pady=15)

show_frame(pages[0])

root.mainloop()
