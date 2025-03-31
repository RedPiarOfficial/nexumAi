from stem import Signal
from stem.control import Controller
import requests

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

	@property
	def proxies(self):
		return self._proxies

Interfice_Tor = Tor()