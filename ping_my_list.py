from rich.console import Console
from rich.table import Table
from rich.live import Live
from sys import exit

from pythonping import ping
import time

watchlist = []
f = open("hosts.txt", "r")
for x in f:
	watchlist.append(str. rstrip(x))  



def generate_table() -> Table:
	id=0
	table = Table(show_header=True, header_style='bold #2070b2',title='[bold][#2070b2]P[/#2070b2]ing_m[#f8e020]y[/#f8e020]_list')
	table.add_column('ID', justify='right')
	table.add_column('Hostname')
	table.add_column('IP',justify='center')
	table.add_column('Status', justify='center')
	table.add_column('PING', justify='right')
	for url in watchlist:
		id+=1
		try:
			result = get_ping(url)
		except:
			pass
		table.add_row(str(id), f'{result["hostname"]}', f'[#f8e020]{result["ip"]}', f'[green]{result["status"]}',f'{result["ping"]}')
	return table



def get_ping(hostname,count=1,verbose=False):	
	try:
		resp = ping(hostname,count=1)
		res_ping = str(resp).split(' ')
	except:
		result_status = '[red][blink]DOWN!'
		result_ip = "---"
		result_ms = "---"
		result_hostname	= '[strike][red]'+hostname
	else:		
		if resp.success():
			result_status = '[green]UP'
			result_ip = res_ping[2].replace('\r', '').replace('\n', '').replace(',', '').replace('msRound', '')
			result_ms = res_ping[6].replace('\r', '').replace('\n', '').replace(',', '').replace('msRound', '')+" ms"    
			result_hostname	= '[bold][#2070b2]'+hostname
		else:
			result_status = '[red][blink]DOWN!'
			result_ip = "---"
			result_ms = "---"
			result_hostname	= '[strike][red]'+hostname	
	return {'status': result_status,'ping':result_ms,'ip':result_ip,'hostname':result_hostname}



	
with Live(generate_table(), refresh_per_second=4) as live:
	live.update(generate_table())