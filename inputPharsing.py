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


def camuPhrasing():
    data = list()
    rawData = list()
    blockData = list()

    with open('data.txt') as dataFile:
        for block in dataFile.read().split('--|--'):
            rawData.append(block)

        # rawData.append(blocks for blocks in dataFile.read().split('--|--'))

    for blocks in rawData:
        blockData.append(blocks.split('\n'))

    print(blockData)
    '''for i in blockData:
        i.pop(1)'''

    for info in blockData:
        course = info[0][0].split(' - ')[0].strip()




camuPhrasing()
