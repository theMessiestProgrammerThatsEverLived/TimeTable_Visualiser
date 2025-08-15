import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime


def parse_time(time_str):
    """Convert 'HH:MM AM/PM' to minutes since midnight."""
    dt = datetime.strptime(time_str, "%I:%M %p")
    return dt.hour * 60 + dt.minute


def visualize_timetable(courseTile, days=None, title="Class Timetable", filename=None):
    """Draws a timetable with days and rectangles centered between grid lines."""

    if days is None:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Convert times to minutes
    for c in courseTile:
        c["start_min"] = parse_time(c["start"])
        c["end_min"] = parse_time(c["end"])

    # Time range: 7:30 AM → 5:30 PM
    start_day_min = parse_time("7:30 AM")
    end_day_min = parse_time("5:30 PM")

    ax = plotSetup(days, start_day_min, end_day_min)

    subjectTiles(courseTile, ax, days, title)

    if filename:
        plt.savefig(filename)
    plt.show()


def subjectTiles(courseList, ax, days, title):
    # Prepare unique colors for each course code
    course_codes = list({c["code"] for c in courseList})  # Unique course codes
    color_map = {code: plt.cm.tab20(i % 20) for i, code in enumerate(course_codes)}

    # Draw rectangles for each course
    for c in courseList:
        day_idx = days.index(c["day"])
        rect = patches.Rectangle(
            (day_idx + 0.02, c["start_min"]),  # Start just inside the column
            0.96,  # Width to fit inside grid lines
            c["end_min"] - c["start_min"],
            linewidth=1,
            edgecolor='black',
            facecolor=color_map[c["code"]],
            alpha=0.7
        )
        ax.add_patch(rect)

        # Course code label
        ax.text(day_idx + 0.5, c["start_min"] + 20, c["code"],
                ha='center', va='top', fontsize=9, weight='bold')

        # Time label
        ax.text(day_idx + 0.5, c["start_min"] + (c["end_min"] - c["start_min"]) / 2,
                f"{c['start']} - {c['end']}", ha='center', va='center', fontsize=8)

    plt.title(title, fontsize=14, pad=20)
    plt.tight_layout()


def plotSetup(days, start_day_min, end_day_min):
    # Setup plot
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, len(days))  # One column per day
    ax.set_ylim(end_day_min, start_day_min)  # Invert y-axis for time
    ax.invert_yaxis()

    # Place xticks in the middle of each column
    ax.set_xticks([i + 0.5 for i in range(len(days))])
    ax.set_xticklabels(days)

    # Draw vertical grid lines at column borders
    ax.set_xticks(range(len(days) + 1), minor=True)

    # Y-axis ticks every 30 mins
    y_ticks = list(range(start_day_min, end_day_min + 1, 30))
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([f"{h // 60}:{h % 60:02d}" for h in y_ticks])

    # Grid: major = time, minor = day columns
    ax.grid(True, which='major', axis='y', linestyle='--', alpha=0.5)
    ax.grid(True, which='minor', axis='x', linestyle='-', alpha=0.7)

    return ax


'''courses = [
    {"day": "Monday", "start": "8:30 AM", "end": "9:30 AM", "code": "CSE101"},
    {"day": "Monday", "start": "12:30 PM", "end": "1:30 PM", "code": "CSE101"},
    {"day": "Wednesday", "start": "1:00 PM", "end": "2:30 PM", "code": "MTH102"},
    {"day": "Saturday", "start": "9:30 AM", "end": "11:00 AM", "code": "PHY103"},
    {"day": "Monday", "start": "10:00 AM", "end": "11:30 AM", "code": "MTH102"},  # Same course as Wednesday
]'''


def inputPhrasing():
    data = list()
    while True:
        courseName = input("Course Name: ")

        if not courseName:
            break

        while True:
            daysNTimes = input("days, startTime, endTime: ").split(',')
            print(daysNTimes)
            if daysNTimes == ['']:
                break

            dataGroup = dict()
            dataGroup["day"] = daysNTimes[0].strip()
            dataGroup["start"] = daysNTimes[1].strip()
            dataGroup["end"] = daysNTimes[2].strip()
            dataGroup["code"] = courseName.strip()
            data.append(dataGroup)

    return data


visualize_timetable(inputPhrasing(), filename="timetable.png")
