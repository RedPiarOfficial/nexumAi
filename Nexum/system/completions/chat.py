from .utils.models import Models
from .utils.headers import TOKEN_HEADERS, WRITING_HEADERS
from .utils.make import *

class Completion:
	def __init__(self, Tor=None):
		self.models_object = Models()
		self.proxies = None
		self.Tor = Tor

	def create(self, messages, model=1, model_check=False, proxy=False):
		if proxy and self.Tor:
			self.proxies = self.Tor.proxies

		answer = None
		message = ''
		for i in messages:
			message = message + i['role'] + ': ' + i['content'] + '\n'
		else:
			message = message + 'ai: '

		model_to_use = self.models_object.get_model(model)
		cookies = {}
		cookies = set_cookie(cookies, "SessionID", SESSION_ID)
		
		# Подготовка текста
		inp_val = message.strip()
		text = encode_html_entities(inp_val)
		token = generate_xa1py_token()
		
		# 1. Запрос к token.php
		token_payload = {
			"session_id": get_cookie(cookies, "SessionID"),
			"token": token
		}
		
		try:
			token_response = requests.post(TOKEN_URL, data=token_payload, headers=TOKEN_HEADERS, proxies=self.proxies)
			token_response.raise_for_status()
			token_data = token_response.json()
			
			if "token" not in token_data or not token_data["token"]:
				print("Ошибка: Токен не получен от token.php или пустой")
				return None
			
			capcha_token = token_data["token"]
			
			# 2. Запрос к writing.php
			writing_payload = {
				"text": text,
				"capcha": capcha_token,
				"model": model_to_use['callback'],
				"session_id": get_cookie(cookies, "SessionID")
			}
			
			writing_response = requests.post(WRITING_URL, data=writing_payload, headers=WRITING_HEADERS, proxies=self.proxies)
			writing_response.raise_for_status()
			if not model_check:
				lines = [line for line in writing_response.text.split('\n') if not line.strip().startswith('[model:')]
				answer = '\n'.join(lines).strip()

			if answer:
				return answer
			else:
				return writing_response.text
			
		except requests.exceptions.RequestException as e:
			print(f"Ошибка при выполнении запроса: {e}")
			if e.response is not None:
				print("Ответ сервера:", e.response.text)
			return None