# Python week 5 lab worksheet
import statistics


def time_calc_sec(): # Code task 1
    total_seconds = int(input("Please inout the total number of seconds: "))
    seconds = str(total_seconds % 60)
    total_minutes = total_seconds // 60
    if total_minutes >= 60:
        minutes = str(total_minutes - 60)
    else:
        minutes = str(total_minutes)
    hours = str(total_minutes // 60)

    print ("hours:" + hours + "minutes: " + minutes + "seconds: " + seconds)


def slices_task(): # Code task 2
    a = list(range(9,-1,-1))

    print (len(a))
    print(sum(a))
    print(min(a))
    print(max(a[::3]))
    b = a.reverse()
    print(b)


def stats_task(): # Code task 3
    a = [9, 3, 5, 4, 10, 4, 3, 2, 4]

    print(statistics.mean(a))
    print(statistics.mode(a))
    print(statistics.median(a))


def string_manipulation(): # Code task 4
    for char in "1bc4":
        if char.isalpha() is False:
            print ("not a letter")
        else:
            print(char.upper())
