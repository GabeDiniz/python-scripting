from datetime import datetime
from dataclasses import dataclass

@dataclass
class Habit:
  name: str
  time_since: str
  remaining_days: str
  minutes_saved: float
  money_saved: str