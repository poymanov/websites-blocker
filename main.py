import time
from datetime import datetime as dt

hosts_file = '/etc/hosts'
redirect_url = '127.0.0.1'
block_sites = ['facebook.com', 'www.facebook.com']
begin_period = dt(dt.now().year, dt.now().month, dt.now().day, 17)
end_period = dt(dt.now().year, dt.now().month, dt.now().day, 18)

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
	time.sleep(5)
