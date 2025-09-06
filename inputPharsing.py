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
            dataGroup["day"] = daysNTimes[0].strip().capitalize()
            dataGroup["start"] = daysNTimes[1].strip()
            dataGroup["end"] = daysNTimes[2].strip()
            dataGroup["code"] = courseName.strip()
            data.append(dataGroup)

    return data


def dayPhrasing(rawData):
    timings = rawData.split(" - ")
    processedTime = list()
    pairs = list()
    for time in timings:
        if len(time) == 5:
            processedTime.append(time)

        else:
            time1 = time[:5]
            time2 = time[5:]
            if time1 == time2:
                continue
            else:
                processedTime.append(time1)
                processedTime.append(time2)

    for index, time in enumerate(processedTime):
        if index%2 == 0:
            pairs.append([processedTime[index], processedTime[index+1]])

    return pairs


def camuPhrasing():
    data = list()
    rawData = list()
    blockData = list()

    with open('data.txt') as dataFile:
        for block in dataFile.read().split('--|--'):
            rawData.append(block)

        # rawData.append(blocks for blocks in dataFile.read().split('--|--'))

    for blocks in rawData:
        blockData.append(blocks.strip().split('\n'))

    for i in blockData:
        i.pop(1)

    print(blockData)

    for info in blockData:
        course = info[0].split(' - ')[0].strip()
        info.pop(0)
        print(course)

        for rawDay in info:
            day, rawTime =  rawDay.strip().split(': ')
            refinedTime = dayPhrasing(rawTime)
            for timingsPairs in refinedTime:
                dataGroup = dict()
                dataGroup["day"] = day
                dataGroup["start"] = timingsPairs[0]
                dataGroup["end"] = timingsPairs[1]
                dataGroup["code"] = course
                data.append(dataGroup)

    return data







camuPhrasing()
