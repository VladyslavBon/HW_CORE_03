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
            difference = date - current_datetime
            if 0 < difference.days <= 7:
                if date.weekday() in [0, 5, 6]:
                    monday += f" {name},"
                    count_monday += 1
                elif date.weekday() == 1:
                    tuesday += f" {name},"
                    count_tuesday += 1
                elif date.weekday() == 2:
                    wednesday += f" {name},"
                    count_wednesday += 1
                elif date.weekday() == 3:
                    thursday += f" {name},"
                    count_thursday += 1
                elif date.weekday() == 4:
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
    {"Bill": datetime(year=2023, month=5, day=20).date()}, 
    {"Jill": datetime(year=2023, month=5, day=22).date()},
    {"Kim": datetime(year=2023, month=5, day=19).date()},
    {"Jan": datetime(year=2023, month=5, day=23).date()}
    ]

get_birthdays_per_week(users)