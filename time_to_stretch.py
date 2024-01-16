import winsound
import time
from datetime import datetime

low_freq = 440
high_freq = 880
short_duration = 300
long_duration = 600
interruption = 0.3
pause = 3600

def single_beep():
    winsound.Beep(low_freq, short_duration)

def double_beep():
    single_beep()
    time.sleep(interruption)
    single_beep()

def final_beep():
    for i in range(3):
        winsound.Beep(high_freq, long_duration)
        time.sleep(interruption)

def write(message):
    with open ("history.txt", "a") as fh:
        fh.writelines(message)

def intro():
    intro_message = f"The script started at {datetime.now()}\n"
    print(intro_message)
    write(intro_message)

def outro():
    outro_message = f"The script finished at {datetime.now()}\n\n"
    print(outro_message)
    write(outro_message)


# morning
intro()
for i in range(2):
    time.sleep(pause)
    print(f"{datetime.time.now().strftime('%H:%M')} - Time to stretch!")
    single_beep()
    time.sleep(pause)
    print(f"{datetime.time.now().strftime('%H:%M')} - Time to move!")
    double_beep()

# lunch time
time.sleep(pause)
print(f"{datetime.time.now().strftime('%H:%M')} - Lunch time!")
double_beep()
double_beep()

# afternoon
for i in range(2):
    time.sleep(pause)
    print(f"{datetime.time.now().strftime('%H:%M')} - Time to stretch!")
    single_beep()
    time.sleep(pause)
    print(f"{datetime.time.now().strftime('%H:%M')} - Time to move!")
    double_beep()
print(f"{datetime.time.now().strftime('%H:%M')} - Time to go home!")
final_beep()
outro()
