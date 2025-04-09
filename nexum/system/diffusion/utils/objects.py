import websocket
import json
import requests
import os
import string
import threading
import random
from bs4 import BeautifulSoup
import base64
from urllib.parse import quote

class Model_sdxl_flash:
	def __init__(self, prompt, path, settings, Tor=None):
		self.proxies = None
		self.Tor = Tor
		self._settings = settings.setting
		self.path = path
		self.urls = {
			'join': 'https://kingnish-sdxl-flash.hf.space/queue/join',
			'generate': 'https://kingnish-sdxl-flash.hf.space/queue/data'
		}

		self.session_hash = "".join(random.choices(string.ascii_letters + string.digits, k=16))
		seed = self._settings['seed']
		if self._settings['seed'] == 'random':
			seed = random.randint(1, 999999)
		self.payload = {
		  "data": [
			prompt,
			self._settings['negative_prompt'],
			True,
			seed,
			self._settings['height'],
			self._settings['width'],
			3,
			self._settings['steps'],
			True
		  ],
		  "event_data": None,
		  "fn_index": 2,
		  "trigger_id": 5,
		  "session_hash": self.session_hash
		}

	def create(self, proxy):
		if proxy and self.Tor:
			self.proxies = self.Tor.proxies

		resp = requests.post('https://kingnish-sdxl-flash.hf.space/queue/join', json=self.payload, proxies=self.proxies)

		answer = requests.get('https://kingnish-sdxl-flash.hf.space/queue/data?session_hash='+self.session_hash, stream=True, proxies=self.proxies)

		if answer.status_code == 200:
			for line in answer.iter_lines():
				if line:
					decoded_line = line.decode('utf-8')
					
					# Если строка начинается с "data: "
					if decoded_line.startswith("data: "):
						# Убираем префикс "data: "
						json_str = decoded_line[6:]
						
						try:
							# Парсим JSON
							data = json.loads(json_str)
							# Получаем msg
							msg = data["msg"]
							
							# Останавливаемся при закрытии потока
							if msg == "process_completed":
								if data['output']:
									resp = requests.get(data['output']['data'][0][0]['image']['url'])
									with open(self.path, 'wb') as file:
										file.write(resp.content)
									return True
								break
								
						except json.JSONDecodeError:
							# Пропускаем некорректный JSON
							continue

class flux_2:
	def __init__(self, Tor=None):
		self.proxies = None
		self.Tor = Tor

	def create(self, prompt, path, proxy=False):
			if proxy and self.Tor:
				self.proxies = self.Tor.proxies
			prompt = quote(prompt)
			resp = requests.get('https://lusion.regem.in/access/flux-2.php',
						params={
							'prompt': prompt
						},
						headers={
							'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
							'referer': 'https://lusion.regem.in/',
						},
						proxies=self.proxies)

			soup = BeautifulSoup(resp.text, 'html.parser')

			if resp.text == 'Error! Try Again Later':
				Exception('Error! Try Again Later')

			img = soup.find('img', class_='img-fluid rounded')
			src = img['src']
			base64_string = src.split(',')[1]
				
			img_bytes = base64.b64decode(base64_string)

			with open(path, 'wb') as file:
				file.write(img_bytes)

			return True
# Model_deepfake('nude hatsune miku', './test1.jpg').create_socket_connect()
# if __name__ == "__main__":
#     # Example initialization with 5 simultaneous requests
#     threads = []
#     prompts = [
#         "nude hatsune miku",
#         "hatsune miku in swimsuit",
#         "hatsune miku dancing",
#         "hatsune miku singing",
#         "hatsune miku with guitar"
#     ]
	
#     # Create 5 threads for simultaneous processing
#     for i in range(5):
#         output_path = f'./test{i+1}.jpg'
#         thread = threading.Thread(target=run_instance, args=(prompts[i], output_path, {"set_log": True}))
#         threads.append(thread)
#         thread.start()
	
#     # Wait for all threads to complete
#     for thread in threads:
#         thread.join()
	
#     print("All 5 requests completed")