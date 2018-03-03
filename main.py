# requirement = [diff,queAmtOrMarks,queType,chapDist]
# quetype = [type1,marks1,type2,marks2,....typen,marksn]
# chapdist = [chap1,marks1,chap2,marks2....chapn,marksn]

req = [1,70,[[0,5],[1,13]],[5,10,10,5,5,10,5,5,10,5]]
typePattern =  req[2]
chapPattern = req[3]
queBank = []
ftest = open("testQue.txt",'r')
for line in ftest:
    line = line.strip()
    que = [int(line[1]),int(line[4]),int(line[7]),int(line[10])]
    queBank.append(que)
# print(queBank)
for eachtype in typePattern:
    # print(type)
    type = eachtype[0]
    noOfQue = eachtype[1]
    print("type ==>",type,"no of questions ==>",noOfQue)
    nTypeQue = []
    for each in queBank:
        # print(each[2])
        if each[2]==type:
            nTypeQue.append(each)
    print(nTypeQue)
    print(len(nTypeQue))
    nTypeQue=[]