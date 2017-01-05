import os

def consolidate():
	all_files = os.listdir('.')
	csv_files = [f for f in all_files if '.csv' in f and 'all.csv' not in f]
	output = open('all.csv', 'w+')
	data = ''

	output.write('zip,username,url,age,profile_image,match,enemy\n')
	for csv in csv_files:
		zip = csv.replace('.csv', '') + ','
		with open(csv) as f:
			for line in f:
				output.write(zip + line)
		output.write('\n')
		
	output.close()

if __name__ == '__main__':
	consolidate()