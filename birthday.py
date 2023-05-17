from datetime import datetime

def get_birthdays_per_week(users):
    current_datetime = datetime.now().date()

    monday = f"Monday:"
    count_monday = 0
    tuesday = f"Tuesday:"
    count_tuesday = 0
    wednesday = f"Wednesday:"
    count_wednesday = 0
    thursday = f"Thursday:"
    count_thursday = 0
    friday = f"Friday:"
    count_friday = 0

    for ch in users:
        for name, date in ch.items():
            new_datetime = datetime(year=current_datetime.year, month=date.month, day=date.day).date()
            difference = new_datetime - current_datetime
            if 0 < difference.days <= 7:
                if new_datetime.weekday() in [0, 5, 6]:
                    monday += f" {name},"
                    count_monday += 1
                elif new_datetime.weekday() == 1:
                    tuesday += f" {name},"
                    count_tuesday += 1
                elif new_datetime.weekday() == 2:
                    wednesday += f" {name},"
                    count_wednesday += 1
                elif new_datetime.weekday() == 3:
                    thursday += f" {name},"
                    count_thursday += 1
                elif new_datetime.weekday() == 4:
                    friday += f" {name},"
                    count_friday += 1

    if count_monday > 0:
        print(monday.rstrip(","))
    if count_tuesday > 0:
        print(tuesday.rstrip(","))
    if count_wednesday > 0:
        print(wednesday.rstrip(","))
    if count_thursday > 0:
        print(thursday.rstrip(","))
    if count_friday > 0:
        print(friday.rstrip(","))
    
users = [
    {"Bill": datetime(year=1986, month=5, day=20).date()}, 
    {"Jill": datetime(year=1993, month=5, day=22).date()},
    {"Kim": datetime(year=1975, month=5, day=19).date()},
    {"Jan": datetime(year=1969, month=5, day=23).date()}
    ]

get_birthdays_per_week(users)