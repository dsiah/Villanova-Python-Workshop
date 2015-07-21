# Get the day of week of a certain date
from datetime import datetime

date_of_birth = "September 3, 1996"
# date_of_birth = raw_input("Enter the date you were born on (e.g., January 1, 1995): ").strip()

day_of_week = datetime.strptime(date_of_birth, '%B %d, %Y').strftime('%A')
print "{dob} was a {dow}".format(dob=date_of_birth, dow=day_of_week)
