import csv
from collections import Counter

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))


with open("data.csv",newline="") as f:
 reader = csv.reader(f)
 data = list(reader)
data.pop(0)

newData = []

for i in range(len(data)):
    num = data[i][1]
    newData.append(float(num))

n = len(newData)
newData.sort()

if n%2 == 0:
    m1 = float(newData[n//2])
    m2 = float(newData[n//2-1])
    median = (m1 + m2) / 2
else:
    median = newData[n//2]
    print(n)
print(f"The Median is ->{str(median)}")


with open("data.csv",newline="") as f:
 reader = csv.reader(f)
 data = list(reader)
data.pop(0)

newData = []

for i in range(len(data)):
    num = data[i][1]
    newData.append(float(num))

data1 = Counter(newData)
mode={
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height,occurence in data1.items():
    if(50<float(height)<60):
        mode["50-60"] +=occurence
    elif(60<float(height)<70):
        mode["60-70"] +=occurence
    elif(70<float(height)<80):
        mode["70-80"] +=occurence 

moderange,modeoccurence = 0,0

for range,occurence in mode.items():
    if(occurence>modeoccurence):
        moderange,modeoccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode1 = float((moderange[0] + moderange[1])/2)
print(f"The Mode Of the Following Data is ->{mode}")