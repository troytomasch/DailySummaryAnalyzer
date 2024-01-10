import csv
import sys
import string
import calendar

## Customizable variables
## List of common words that will be avoided in scoring
avoid = ['', 'to', 'the', 'and', 'went', 'did', 'on', 'a', 'around', 'out', 'from', 'had', 'at', 'in', 'of', 'for', 'got', 'with', 'my', 'up']
## Frequency required of events to include in output of all word analysis
frequency = 4
## Threshold for what is considered a best day. Anything higher is included
bestDayThreshold = 5
## Threshold for what is considered a worst day. Anything lower is included
worstDayThreshold = 2


## First load the data from a CSV into python
entryFile = open('summary.csv', "r")

csvreader = csv.reader(entryFile)
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

entryFile.close()

## Finds the average rating of days with the provided word
def findScore(word):
    total = 0
    score = 0
    average = 0
    for row in rows:
        for punctuation in string.punctuation:
            row[1] = row[1].replace(punctuation, '')
        row[1] = row[1].split(" ")
        for currentWord in row[1]:
            if currentWord.lower() == word:
                score += int(row[2])
                total += 1
                average = score / total
    print("Average daily score of " + word + " is " + str(round(average, 2)))

## Find commonly used words and their associated scores 
def wordScores():
    ## Entries in the scores dictionary are "word: [Average Score, Frequency, Total Score]"
    scores = {}
    csvwriter.writerow(["Word Analysis"])
    csvwriter.writerow(["Word", "Average Score", "Frequency"])
    for row in rows:
        for punctuation in string.punctuation:
            row[1] = row[1].replace(punctuation, '')
        row[1] = row[1].split(" ")
        for currentWord in row[1]:
            current = currentWord.lower()
            if avoid.count(current) > 0:
                continue
            keys = list(scores.keys())
            if keys.count(current) == 1:
                scores[current][2] += int(row[2])
                scores[current][1] += 1
                scores[current][0] = scores[current][2] / scores[current][1]
            else:
                scores[current] = [int(row[2]), 1, int(row[2])]
    keys = scores.keys()
    output = []
    for key in keys:
        if scores[key][1] >= frequency:
            csvwriter.writerow([key, round(scores[key][0], 2), scores[key][1]])
            output.append([key, round(scores[key][0], 2), scores[key][1]])

## Finds average of all days
def grossAverage():
    total = 0
    count = 0
    for row in rows:
        count += 1
        total += int(row[2])
    print("Average of all days is " + str(round(total / count, 2)))

## Finds days rated above the bestDayThreshold
def bestDays():
    csvwriter.writerow(["Best Days"])
    csvwriter.writerow(["Date", "Summary"])
    for row in rows:
        if int(row[2]) >= bestDayThreshold:
            csvwriter.writerow([row[0], row[1]])

## Finds days rated below the worstDayThreshold
def worstDays():
    csvwriter.writerow(["Worst Days"])
    csvwriter.writerow(["Date", "Summary"])
    for row in rows:
        if int(row[2]) <= worstDayThreshold:
            csvwriter.writerow([row[0], row[1]])

## Finds the average by month
def averageByMonth():
    months = {}
    for row in rows:
        date = row[0].split("/")
        month = date[0]
        keys = list(months.keys())
        if keys.count(month) > 0:
            newAv = (months[month][2] + int(row[2])) / (months[month][1] + 1)
            months[month] = [newAv, months[month][1]+1, months[month][2] + int(row[2])]
        else:
            months[month] = [int(row[2]), 1, int(row[2])]
    keys = months.keys()
    csvwriter.writerow(["Average by Month"])
    csvwriter.writerow(["Month", "Average"])
    for month in keys:
        monthString = calendar.month_name[int(month)]
        csvwriter.writerow([monthString, round(months[month][0], 2)])


## Parses input
if len(sys.argv) == 1:
    print("Must pass valid argument")
elif len(sys.argv) == 3 and sys.argv[1] == "word":
    findScore(sys.argv[2])
else:
    filename = "output.csv"
    outputFile = open(filename, "w", newline="")
    csvwriter = csv.writer(outputFile)
    if sys.argv.count('gross') > 0:
        grossAverage()
    
    if sys.argv.count('months') > 0:
        averageByMonth()

    if sys.argv.count('best') > 0:
        bestDays()

    if sys.argv.count('worst') > 0:
        worstDays()
    
    if sys.argv.count('words') > 0:
        wordScores()

    outputFile.close()
