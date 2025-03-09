def add_time(start, duration, day=''):
    duration = duration.split(':')
    starting = start.split()
    start = starting[0].split(':')

    time = starting[1]

    strt = []
    dur = []
    
    weekdays = 'Sunday Monday Tuesday Wednesday Thurday Friday Saturday'.split()

    for i in range(2):
        strt.append(int(start[i]))
        dur.append(int(duration[i]))    

    for i in range(2):
        strt[i] += dur[i]
    
    if strt[1] >= 60:
        strt[0] += strt[1] // 60
        strt[1] = strt[1] % 60
        
    
    days = (strt[0] - int(start[0])) // 24
    
    strt[0] %= 24
    
#     if days >= 1:
#         strt[0] = strt[0] % 24

    print(strt)

    

    if strt[0] / 24 < 1:
        if time == 'AM':
            if strt[0] >= 12:
                time = 'PM'
                if strt[0] > 12:
                    strt[0] -= 12
    
        elif time == 'PM':
            strt[0] += 12
            if strt[0] >= 24:
                days += 1
                time = 'AM'
                if strt[0] == 24:
                    strt[0] -= 12
                else:
                    strt[0] -= 24
            else:
                strt[0] -= 12
                
            
    if day == '':        
        if days > 1:
            return '{}:{:02d} {} ({} days later)'.format(strt[0],strt[1],time,days)
        elif days == 1:
            return '{}:{:02d} {} (next day)'.format(strt[0],strt[1],time)
        else:
            return '{}:{:02d} {}'.format(strt[0], strt[1], time)
    
    else:
        try:
            day_index = weekdays.index(day.capitalize())
            new_day = weekdays[(day_index + (days % 7)) % 7]
            
            if days == 0:
                return '{}:{:02d} {}, {}'.format(strt[0], strt[1], time, day)
            elif days == 1:
                return f'{strt[0]}:{strt[1]:02d} {time}, {new_day} (next day)'
            else:
                return '{}:{:02d} {}, {} ({} days later)'.format(strt[0], strt[1], time, new_day, days)
        except ValueError:
            return 'enter a valid day'