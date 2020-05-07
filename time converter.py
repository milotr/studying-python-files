hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_mins = float(mins+dura)
remainer = (total_mins)%60
total_hours = (hour + int(total_mins/60))% 24

print (int(total_hours),":",int(remainer))
