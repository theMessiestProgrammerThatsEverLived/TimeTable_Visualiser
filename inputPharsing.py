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
