import os, urllib, shutil

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

def image_store():
	all_files = os.listdir('.')
	csv_files = [f for f in all_files if '.csv' in f and 'all.csv' not in f]

	if not os.path.exists('images'):
		os.makedirs('images')
	source = os.path.dirname(os.path.abspath(__file__))
	destination = source + '/images'

	for csv in csv_files:
		with open(csv) as f:
			zip = csv.replace('.csv', '')
			for line in f:
				username = line.split(',')[0]
				image_url = line.split(',')[-3]
				file_name = '{0} {1}.png'.format(zip, username)
				urllib.urlretrieve(image_url, file_name)
				shutil.move(file_name, destination)

if __name__ == '__main__':
	# consolidate()
	image_store()