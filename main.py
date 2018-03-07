# requirement = [diff,queAmtOrMarks,queType,chapDist]
# quetype = [type1,marks1,type2,marks2,....typen,marksn]
# chapdist = [chap1,marks1,chap2,marks2....chapn,marksn]
import random

Result = []

req = [1, 70, [[1, 13, 5], [0, 5, 1]], [5, 10, 10, 5, 5, 10, 5, 5, 10, 5]]
typePattern = req[2]
chapPattern = req[3]
queBank = []
que = []
for dif in range(3):
    for marks in range(1, 6):
        for type in range(2):
            for chap in range(1, 11):
                que.append(dif)
                que.append(marks)
                que.append(type)
                que.append(chap)
                que.append(random.randint(1, 100))
                # ftest.write(str(que))
                # ftest.write('\n')
                queBank.append(que)
                que = []
# ftest = open("testQue.txt", 'r')
# for line in ftest:
#     line = line.strip()
#     que = [int(line[1]), int(line[4]), int(line[7]), int(line[10])]
#     queBank.append(que)

print(queBank)
for eachtype in typePattern:
    # print(type)
    type = eachtype[0]
    noOfQue = eachtype[1]
    weightage = eachtype[2]
    print("Weightage ==> ", weightage)
    # print("type ==>",type,"no of questions ==>",noOfQue)
    nTypeQue = []
    for each in queBank:
        # print(each[2])
        if each[2] == type:
            nTypeQue.append(each)
    # print(nTypeQue)
    # print(len(nTypeQue))
    m = max(chapPattern)
    max_index = [i for i, j in enumerate(chapPattern) if j == m]  # find index of maximum weightage chapters
    print(max_index)
    # print(chapPattern)
    noOfChap = len(chapPattern)
    while noOfQue > noOfChap:
        # print("whats up")
        chapPattern[:] = [x - weightage for x in chapPattern]
        # print(chapPattern)
        for chap in range(1, 11):
            candidates = []
            for each in nTypeQue:
                # print("each3  ",each[3]," chap ",chap)
                if each[3] == chap:
                    candidates.append(each)
            winnerWinnerChickenDinner = [0, 0, 0, 0, 0]
            # print("can $$$$ ",candidates)
            for eachCan in candidates:
                if eachCan[4] > winnerWinnerChickenDinner[4]:
                    winnerWinnerChickenDinner = eachCan
            # print("Winner ==>",winnerWinnerChickenDinner)
            Result.append(winnerWinnerChickenDinner)
            noOfQue -= 1
            # break  # Remove break for probabilistic selection
    while noOfQue > len(max_index):
        print("Loop ==>", noOfQue)
        for index in max_index:
            chapPattern[index] -= weightage
            chap = index + 1
            for each in nTypeQue:
                # print("each3  ", each[3], " chap ", chap)
                if each[3] == chap:
                    candidates.append(each)
            winnerWinnerChickenDinner = [0, 0, 0, 0, 0]
            # print("can $$$$ ",candidates)
            for eachCan in candidates:
                if eachCan[4] > winnerWinnerChickenDinner[4]:
                    winnerWinnerChickenDinner = eachCan
            # print("Winner ==>",winnerWinnerChickenDinner)
            Result.append(winnerWinnerChickenDinner)
            noOfQue -= 1
            # break  # Remove break for probabilistic selection
        m = max(chapPattern)
        max_index = [i for i, j in enumerate(chapPattern) if j == m]  # find index of maximum weight-age chapters

    for index in max_index:
        chapPattern[index] -= weightage
        chap = index + 1
        for each in nTypeQue:
            # print("each3  ", each[3], " chap ", chap)
            if each[3] == chap:
                candidates.append(each)
        winnerWinnerChickenDinner = [0, 0, 0, 0, 0]
        # print("can $$$$ ",candidates)
        for eachCan in candidates:
            if eachCan[4] > winnerWinnerChickenDinner[4]:
                winnerWinnerChickenDinner = eachCan
        # print("Winner ==>",winnerWinnerChickenDinner)
        Result.append(winnerWinnerChickenDinner)
        noOfQue -= 1
        if noOfQue == 0:
            break
    print(noOfQue)

print(chapPattern)
print(Result)
print("Final Count!! = ", len(Result))
