days = int(input("Days :"))
needed_hours = float(input("Hours :"))
workers = int(input("Workers :"))
calc = days-days*0.1
effort = calc*workers*10

if effort >=needed_hours:
    print(f"Project will complete in time and remaining hours are {effort-needed_hours}")
else:
    print(f"Need more man days to finish {needed_hours-effort} hours of work")
