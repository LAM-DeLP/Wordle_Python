import csv

class datamaneger:
    
    def __init__(self):
        data = []
        with open("wordle_python\\config\\downloadList.csv","r",encoding="UTF-8") as f:
            reader = csv.reader(f)
            data = [[row[3]] for row in reader]

        with open("wordle_python\\config\\vocabList.csv","w",encoding="UTF-8",newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
    
    

manager = datamaneger()


