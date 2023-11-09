import csv
import re

tempList = []
data = []
with open("wordle_python\\config\\downloadList.csv","r",encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        tempList.append(row[3])
    data = [[tempList[i]] for i in range(len(tempList))]

with open("wordle_python\\config\\vocabList.csv","w",encoding="UTF-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

