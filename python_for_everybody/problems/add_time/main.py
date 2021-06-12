def what_day_of_week(duration_in_days, start_day):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[(days.index(start_day.capitalize()) + duration_in_days) % 7] 

def what_day_is_this(minutes):
    return int(minutes / (24 * 60))

def convert_to_minutes(time, pm=False):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    if pm:
        hours = hours + 12
    return hours * 60 + minutes

def convert_to_time_string(minutes):
    hours = int(minutes / 60) % 24
    suffix = 'AM'
    if hours > 12:
        hours = hours - 12
        suffix = 'PM'
    if hours == 12:
        suffix = 'PM'
    if hours == 0:
        hours = 12
    minutes_of_hour = str(minutes % 60).zfill(2)
    return f'{hours}:{minutes_of_hour} {suffix}'

def add_time(start, duration, day=False):
    start_split_on_space = start.split()
    start_time = convert_to_minutes(start_split_on_space[0], start_split_on_space[1] == 'PM')
    delta = convert_to_minutes(duration)
    end_time = start_time + delta
    end_time_as_string = convert_to_time_string(end_time)
    end_day = what_day_is_this(end_time)
    day_of_week = ''
    if day:
        day_of_week = f', {what_day_of_week(int(end_time / (60 * 24)), day)}'
    days_later = ''
    if end_day > 0:
        if end_day < 2:
            days_later = ' (next day)'
        else:
            days_later = f' ({end_day} days later)'
    new_time = f'{end_time_as_string}{day_of_week}{days_later}'
    return new_time
