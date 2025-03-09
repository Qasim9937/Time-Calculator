# Add Time Function

## Description
The `add_time` function calculates the new time after adding a given duration to a starting time. It also accounts for AM/PM transitions and optionally provides the day of the week and the number of days later.

## Features
- Supports 12-hour AM/PM format.
- Accepts an optional day of the week.
- Calculates the number of days passed.
- Returns the updated time in a human-readable format.

## Parameters
- `start` (str): The starting time in the format `hh:mm AM/PM` (e.g., "3:00 PM").
- `duration` (str): The duration to add in the format `hh:mm` (e.g., "2:30").
- `day` (str, optional): The starting day of the week (e.g., "Monday").

## Return Value
A formatted string representing the new time:
- If the result is on the same day: `"5:30 PM"`
- If the result is the next day: `"12:00 AM (next day)"`
- If multiple days have passed: `"9:15 AM (3 days later)"`
- If a day of the week is provided: `"9:15 AM, Thursday (3 days later)"`

## Example Usage
```python
print(add_time("3:00 PM", "3:10"))
# Output: "6:10 PM"

print(add_time("11:30 AM", "2:32", "Monday"))
# Output: "2:02 PM, Monday"

print(add_time("11:43 PM", "24:20"))
# Output: "12:03 AM (2 days later)"

print(add_time("10:10 PM", "3:30", "Wednesday"))
# Output: "1:40 AM, Thursday"
```

## Edge Cases
- Ensures hours and minutes do not exceed their valid ranges.
- Handles AM/PM transitions correctly.
- Adjusts the day of the week appropriately.
- Returns an error message if the provided day is invalid.

## Notes
- The function assumes the `start` time is always in a valid 12-hour format.
- Days of the week are case-insensitive.
- If no `day` argument is provided, only the time and day count are returned.

This function is useful for scheduling, time calculations, and working with 12-hour time formats.

