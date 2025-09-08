from modules import visualize_timetable, phraseBlocks
from inputPharsing import camuPhrasing

data, blockTimings = camuPhrasing()

phraseBlocks(blockTimings)

if input('go/noGo?: ').lower() == 'go':
    visualize_timetable(data)
