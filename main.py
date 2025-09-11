from modules import visualize_timetable, phraseBlocks, checkConflicts
from inputPharsing import camuPhrasing

data, coursePhrased = camuPhrasing()

phraseBlocks(coursePhrased)

for i in coursePhrased:
    # print(coursePhrased[i], coursePhrased)
    finalData = checkConflicts(i, coursePhrased)

# phraseBlocks(blockTimings)

for entries in data:
    if not(entries['code'] in finalData):
        data.remove(entries)


if input('go/noGo?: ').lower() == 'go':
    visualize_timetable(data)
