# requirement = [diff,queAmtOrMarks,queType,chapDist]
# quetype = [type1,marks1,type2,marks2,....typen,marksn]
# chapdist = [chap1,marks1,chap2,marks2....chapn,marksn]

req = [1,70,[0,5,1,65],[1,5,2,10,3,10,4,5,5,5,6,10,7,5,8,5,9,10,10,5]]
queBank = []
ftest = open("testQue.txt",'r')
for line in ftest:
    line = line.strip()
    que = [line[1],line[4],line[7],line[10]]
    queBank.append(que)
print(queBank)

# hi bhav