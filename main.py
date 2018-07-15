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
	else:
		print('Fun time...')
	time.sleep(5)
