#Custom date & time 
from datetime import date

my_birthday = date(2025, 6, 20)
print("My birthday is on:", my_birthday)

from datetime import date

# Get today's date
today = date.today()

# Define your birthday (example: 25th December 2025)
my_birthday = date(2025, 12, 25)

# Find the difference
days_left = my_birthday - today

print("Days left in birthday:", days_left.days)
