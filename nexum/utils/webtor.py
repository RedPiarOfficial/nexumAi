from stem import Signal
from stem.control import Controller
import requests
import os
import tarfile
import subprocess

class Tor:
	def __init__(self):
		self._proxies = {
			"http": "socks5://127.0.0.1:9050",
			"https": "socks5://127.0.0.1:9050"
		}

	def new_ip(self):
		with Controller.from_port(port=9051) as controller:
			controller.authenticate()
			controller.signal(Signal.NEWNYM)

	def check_ip(self):
		response = requests.get("http://httpbin.org/ip", proxies=self._proxies)
		response.raise_for_status()
		return response.json()

	def install_tor(self, path='./TOR', repair=False):
		path = os.path.abspath(path)
		tor_exe_path = os.path.join(path, 'tor', 'tor.exe')
		torrc_path = os.path.join(path, 'tor', 'torrc')
		archive_url = 'https://archive.torproject.org/tor-package-archive/torbrowser/14.0.7/tor-expert-bundle-windows-x86_64-14.0.7.tar.gz'
		archive_path = os.path.join(path, 'experttor.tar.gz')

		if not os.path.exists(path) or repair:
			os.makedirs(path, exist_ok=True)

			print('[*] Downloading TOR archive...')
			resp = requests.get(archive_url)
			with open(archive_path, 'wb') as file:
				file.write(resp.content)

			print('[*] Extracting archive...')
			with tarfile.open(archive_path, 'r:gz') as tar:
				tar.extractall(path=path)

			os.remove(archive_path)

			print('[*] Creating torrc configuration...')
			with open(torrc_path, 'w', encoding='utf-8') as torrc:
				torrc.write('SocksPort 9050\nControlPort 9051')

		if os.path.exists(tor_exe_path):
			print('[*] Launching Tor...')
			# Double quotes are used to ensure correct behavior with start/cmd
			cmd = f'start cmd /k ""{tor_exe_path}" -f "{torrc_path}""'
			subprocess.Popen(cmd, shell=True)
		else:
			print('[!] Failed to find tor.exe after installation.')



	@property
	def proxies(self):
		return self._proxies

Interfice_Tor = Tor()