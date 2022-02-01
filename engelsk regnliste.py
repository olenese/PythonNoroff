week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

rainlist = []
windlist = []
temperaturelist = []

for day in week:
    rain = input('What is the amount of rain today? ')
    rainlist.append(rain)

    wind = input('What is the current windspeed?  ')
    windlist.append(wind)

    temperature = input('What is the temperature? ')
    temperaturelist.append(temperature)

for idx, day in enumerate(week) : 
    if rain[idx] > '1':
        print(f'it is more than 1mm rain on {day} . It was  {rainlist[idx]}')
    if wind[idx] > '10':
        print(f'it is more than 10m/s of wind on {day}. It was  {windlist[idx]} m/s')     
    if temperature[idx] < '5':
        print(f'it was less than 5 degrees on {day}. It was {temperaturelist[idx]} degrees celsius')