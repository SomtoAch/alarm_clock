from playsound import playsound
import time

# ANSI sequences that when printed execute special commands within the terminal
# CLEAR clears the entire terminal
CLEAR = "\033[2J"

# CLEAR_AND_RETURN clears the terminal as well, but after printing is finished returns the cursor to its home position, as if it was going to write over the content that was just printed
CLEAR_AND_RETURN = "\033[H"

# parameter seconds is the time the function will count down from
def alarm_clock(seconds):

    # convert the time parameter to milliseconds
    milliseconds=seconds * 1000
    time_elapsed = 0

    # clear terminal
    print(CLEAR)

    # loop whilst the specified time has not elapsed
    while time_elapsed < milliseconds:

        time.sleep(0.001)
        time_elapsed+=1

        # time_left is the total no. milliseconds left
        time_left = milliseconds - time_elapsed

        # the no. complete minutes remaining out of the no. milliseconds left. 1 minute = 60,000 milliseconds
        minutes_left = time_left // 60000

        # the no. complete seconds that have not elapsed from the no. milliseconds left, but are not enough to make a minute
        seconds_left = time_left % 60000 // 1000

        # the remainder of time left after minutes and seconds have been bundled together
        milliseconds_left = time_left % 1000

        # placing :02d after a variable means the variable must take up at least 2 digits, if it doesnt pad it with 0s
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}:{milliseconds_left:02d}")

    playsound("iphone_alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes*60 + seconds
alarm_clock(total_seconds)