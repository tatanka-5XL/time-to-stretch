import winsound
import time
from datetime import datetime

low_freq = 440
high_freq = 880
short_duration = 300
long_duration = 600
interruption = 0.3
pause = 3600
time_now = datetime.now().strftime('%H:%M')

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

def print_and_write(message):
    print(message)
    with open ("history.txt", "a") as fh:
        fh.writelines(message)


# morning
print_and_write(f"The script started at {datetime.now()}\n")
for i in range(2):
    time.sleep(pause)
    print(f"{time_now} - Time to stretch!")
    single_beep()
    time.sleep(pause)
    print(f"{time_now} - Time to move!")
    double_beep()

# lunch time
time.sleep(pause)
print(f"{time_now} - Lunch time!")
double_beep()
double_beep()

# afternoon
for i in range(2):
    time.sleep(pause)
    print(f"{time_now} - Time to stretch!")
    single_beep()
    time.sleep(pause)
    print(f"{time_now} - Time to move!")
    double_beep()
print(f"{time_now} - Time to go home!")
final_beep()
print_and_write(f"The script finished at {datetime.now()}\n\n")
