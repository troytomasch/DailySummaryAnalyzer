# DailySummaryAnalyzer
This is the repo that contains the Python script to analyze the data recorded in my daily summary.

# Background
During September of 2023, I started tracking what I did and how I felt at the end of each day. I would record a summary of the things I did that day, as well as a rating of my mood and how I felt that day went on a scale of 1 to 5. The intent was to be able to analyze some of this data to see if there was any trends in what made me happy. This script is to help perform that analysis.

# How to use it
The main requirement for being able to run the script is a csv file called summary.csv in the same folder as the python script. The formatting for the csv file is three columns: one with the date, one with the summary, and one with the rating. It should look like this:
![image](https://github.com/troytomasch/DailySummaryAnalyzer/assets/55467325/7041145c-4fcc-46f7-95b7-392c6480c239)

Punctuation doesn't matter and should be removed automatically.

To run the script, make sure that you have downloaded python and then you can run it by using the command 'python analyzer.py'.
The commands that you are able to run are as follows:
- 'word WORD_TO_SEARCH_FOR' = to get the average score of the days containing a given word. ex: 'python analyzer.py word pizza'
- 'gross' = to get the average score of all the days included in the csv
- 'months' = to get an average score for each of the months included in the csv
- 'best' = to get a list of the summaries of the days over the bestDayThreshold
- 'worst' = to get a list of the summaries of the days over the worstDayThreshold
- 'words' = to get a list of all the words used in the days over a given threshold and the average score from each day they are included in

Besides the word command, commands can be stacked.
Examples:
'python analyzer.py best worst'
'python analyzer.py words months'
'python analyzer.py gross months best worst words'

# Output.csv
Some of the commands will output data to a csv file instead of printing it for better readability. If you get a permission error, "PermissionError: [Errno 13] Permission denied: 'output.csv'", try closing output.csv and trying again.

# Customizable variables
There are a few variable that are customizable at the top of the python file.
- avoid = This is the list of words that won't be counted when returning the average for all the words.
- frequency = This is the frequency required of events to include in output of all word analysis. So if the frequency is 3 and pizza is only mentioned 2 times than it will not be included.
- bestDayThreshold = Threshold for what is considered a best day. Anything higher is included.
- worstDayThreshold = Threshold for what is considered a worst day. Anything lower is included.

# Notes
One thing to note is that if a word is mentioned multiple times in an entry than it will be counted multiple times. For example, if an entry says "For breakfast I had pizza. For lunch I had pizza. For dinner I had pizza.", then the frequency of pizza will be three from this one entry and the value of the entry will be more heavily weighted in its average. I did this intentionally as I felt that if something was mentioned more than one time in a given day then this day should be weighted more as this word was a greater part of this day than others.
