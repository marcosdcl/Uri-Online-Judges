# Time Conversion

def time_convert(seconds):
    '''Convert seconds to hours and minutes'''
    time = {
        'hour'    : 0,
        'minutes' : 0,
        'seconds' : 0
        }
    while seconds > 0:
        if seconds >= 3600:
            seconds -= 3600
            time['hour'] += 1
        elif seconds >= 60:
            seconds -= 60
            time['minutes'] += 1
        elif seconds >= 1:
            seconds -= 1
            time['seconds'] += 1
    return time

seconds = int(input())
time = time_convert(seconds)

print('{}:{}:{}'.format(time['hour'], time['minutes'], time['seconds']))
