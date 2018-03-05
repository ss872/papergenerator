queBank = []
que = []
ftest = open("testQue.txt",'w')
for dif in range(3):
    for marks in range(1,6):
        for type in range(2):
            for chap in range(1,11):
                que.append(dif)
                que.append(marks)
                que.append(type)
                que.append(chap)
                # ftest.write(str(que))
                # ftest.write('\n')
                queBank.append(que)
                que = []

# print(len(questiondemo))
# ftest.write(str(questiondemo))
ftest.close()