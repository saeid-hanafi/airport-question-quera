firstInput = input()
inputList = firstInput.split(" ")
planeCount = int(inputList[0])
lineCount = int(inputList[1])
planeList = {}
for i in range(0, planeCount):
    planeList[input()] = 1

ordersList = []
orderCount = int(input())
for j in range(0, orderCount):
    ordersList.insert(j, input())

res = []
lineStatusObj = {}
global k
k: int = 0


def getStatusPlane(plane):
    if planeList.get(plane):
        return planeList.get(plane)
    else:
        return 4


def lineStatus(line):
    if lineStatusObj.get(int(line)):
        return lineStatusObj.get(int(line))
    else:
        return "FREE"


def getStatus(order, plane):
    global k
    status = getStatusPlane(plane)
    if order == "TAKE-OFF":
        if status == 4:
            res.insert(k, "YOU ARE NOT HERE")
        elif status == 3:
            res.insert(k, "YOU ARE LANDING NOW")
        elif status == 2:
            res.insert(k, "YOU ARE TAKING OFF")
        elif status == 1 and len(lineStatusObj) == lineCount:
            res.insert(k, "NO FREE BOUND")
        elif status == 1 and len(lineStatusObj) < lineCount:
            firstCountBuffer = 1
            while firstCountBuffer < lineCount + 1:
                if not lineStatusObj.get(firstCountBuffer):
                    lineStatusObj[firstCountBuffer] = plane
                    planeList[plane] = 2
                    break
                else:
                    firstCountBuffer += 1
    elif order == "LANDING":
        if status == 4 and len(lineStatusObj) == lineCount:
            res.insert(k, "NO FREE BOUND")
        elif status == 3:
            res.insert(k, "YOU ARE LANDING NOW")
        elif status == 2:
            res.insert(k, "YOU ARE TAKING OFF")
        elif status == 1:
            res.insert(k, "YOU ARE HERE")
        elif status == 4 and len(lineStatusObj) < lineCount:
            lineCountBuffer = lineCount
            while lineCountBuffer > 0:
                if not lineStatusObj.get(lineCountBuffer):
                    lineStatusObj[lineCountBuffer] = plane
                    planeList[plane] = 3
                    break
                else:
                    lineCountBuffer -= 1

    elif order == "PLANE-STATUS":
        res.insert(k, status)
    elif order == "BAND-STATUS":
        res.insert(k, lineStatus(plane))

    k += 1


for item in ordersList:
    splitItem = item.split(" ")
    orderName = splitItem[0]
    plane = splitItem[1]
    getStatus(orderName, plane)


for resItem in res:
    print(resItem)
