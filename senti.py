import csv
import os
from textblob import TextBlob

#infile = 'C:/Users/bhave/Downloads/smmPro/csv_files_pre/the_promise.csv'

directory = os.path.join(os.getcwd(),"csv_files_pre")
for file_name in os.listdir(directory):
	file_path =  os.path.join(directory,file_name)
	print(file_path)
	with open(file_path, 'r', encoding="utf8") as csvfile:
		rows = csv.reader(csvfile)
		polarity = 0
		row_count = 0
		for row in rows:
			row_count+=1
			sentence = row[1]
			blob = TextBlob(sentence)
			polarity = polarity + (blob.sentiment.polarity)
		average_polarity = (polarity/row_count)
		filename, file_extension = os.path.splitext(file_name)
		fields = [filename, average_polarity]
		writer = csv.writer(open("polairity_table.csv", "a"))
		writer.writerow(fields)
		print(average_polarity)
