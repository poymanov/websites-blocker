import time
from datetime import datetime as dt

hosts_file = '/etc/hosts'
redirect_url = '127.0.0.1'
block_sites = ['facebook.com', 'www.facebook.com']
begin_period = dt(dt.now().year, dt.now().month, dt.now().day, 18)
end_period = dt(dt.now().year, dt.now().month, dt.now().day, 19)

while True:
	if begin_period < dt.now() < end_period:
		print('Working time...')

		with open(hosts_file, 'r+') as file:
			content = file.read()

			for website in block_sites:
				if website in content:
					continue
				else:
					file.write('%s %s \n' % (redirect_url, website))

	else:
		print('Fun time...')

		with open(hosts_file, 'r+') as file:
			content = file.readlines()
			file.seek(0)

			for line in content:
				if not any(website in line for website in block_sites):
					file.write(line)

			file.truncate()					
	time.sleep(5)
