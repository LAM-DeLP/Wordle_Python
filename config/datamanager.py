import csv
import random

class datamaneger:
    
    vocabfile = "wordle_python\\config\\vocabList.csv"

    def __init__(self):
        data = []
        self.word = ""
        with open("wordle_python\\config\\downloadList.csv","r",encoding="UTF-8") as f:
            reader = csv.reader(f)
            data = [[row[3]] for row in reader]

        with open(datamaneger.vocabfile,"w",encoding="UTF-8",newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def choiceWord(self):
        with open(datamaneger.vocabfile,"r",encoding="UTF-8") as f:
            lines = f.readlines()
            self.word = lines[(random.randint(0,sum(1 for line in lines)))]
            self.word = self.word.replace('\n', '')

