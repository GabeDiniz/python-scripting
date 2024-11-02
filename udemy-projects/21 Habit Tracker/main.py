import pandas as pd   # pip install pandas
from tabulate import tabulate   # pip install tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit

'''
USAGE
This projects helps you track your habits. Insert the habit you would like to track,
  how long since you have quit the habit, how much that habit costed you, and how much
  time you spent on that habit. 
  
  track_habit("Name", Date that you quit the habit, cost of habit per day, minutes used by that habit per day)
Example:
  track_habit("Coffee", datetime(2023, 11, 27, 8), cost = 1, minutes_used = 5)
    -> Translation: you quit coffee on Nov 27, 2023 @ 8am. That habit cost you $1/day, and 5-minutes/day 

RESULT EXAMPLE
The current habits found below will result in a table that will look something like the table below,
  with the exception that some of the values will be slightly different depending on the current date.
+----+-----------------+--------------+------------------+-----------------+---------------+
|    | name            | time_since   | remaining_days   |   minutes_saved | money_saved   |
|----+-----------------+--------------+------------------+-----------------+---------------|
|  0 | Coffee          | 62.54 days   | Cleared!         |             313 | $219.04       |
|  1 | Procrastinating | 27.54 days   | 32               |            1652 | $1652.2       |
|  2 | Quit Smoking    | 8.54 days    | 51               |            1537 | $939.3        |
+----+-----------------+--------------+------------------+-----------------+---------------+
'''


def main():
  habits: list[Habit] = [
    track_habit("Coffee", datetime(2023, 11, 27), cost = 1, minutes_used = 5),
    track_habit("Procrastinating", datetime(2024, 1, 1), cost = 30, minutes_used = 60),
    track_habit("Quit Smoking", datetime(2024, 1, 20), cost = 20, minutes_used = 60 * 3),
  ]

  df = pd.DataFrame(habits)

  print(tabulate(df, headers="keys", tablefmt="psql"))

if __name__ == "__main__":
  main()