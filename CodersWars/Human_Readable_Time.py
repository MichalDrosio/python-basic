# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a
# human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

def check_sec(seconds):
    if len(str(seconds)) == 1:
        return '0'+str(seconds)
    return str(seconds)


def make_readable(seconds):
    if seconds <= 359999:
        h = seconds//3600
        m = (seconds-3600*h)//60
        s = (seconds-3600*h-60*m)
        return f'{check_sec(h)}:{check_sec(m)}:{check_sec(s)}'
    return False


print(make_readable(359999))
