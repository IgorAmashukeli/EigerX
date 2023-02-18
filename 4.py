def sequencer(first, maxNum, maxCount):
    n = int(input())
    if first:
        maxNum = n
    if n == 0:
        if n == maxNum:
          maxCount += 1
        return maxCount
    if n > maxNum:
        maxNum = n
        maxCount = 1
    elif n == maxNum:
        maxCount += 1
    return sequencer(False, maxNum, maxCount)


print(sequencer(True, 0, 0))