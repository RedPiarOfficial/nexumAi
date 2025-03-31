class Models:
	def __init__(self):
		self.models = self.get_models()

	def get_models(self):
		return {
	"Diffusion": [{
		'model_id': 1,
		'model_name': 'flux-2',
		'basic_style': 'Realistic and Anime',
		'NSFW': False,
		'loras': None,
		'styles': None
	},
	{
		'model_id': 2,
		'model_name': 'sdxl-flash',
		'basic_style': 'Realistic and Anime',
		'NSFW': True,
		'loras': None,
		'styles': None
	}]}

	def get_model_by_id(self, model_id):
		"""Получить модель по её ID"""
		for company in self.models.values():
			for model in company:
				if model['model_id'] == model_id:
					return model
		return None

	def get_model_by_name(self, model_name):
		"""Получить модель по её названию"""
		for company in self.models.values():
			for model in company:
				if model['model_name'].lower() == model_name.lower():
					return model
		return None

	def get_model(self, identifier):
		"""Получить модель по ID (если число) или названию (если строка)"""
		if isinstance(identifier, int):
			return self.get_model_by_id(identifier)
		elif isinstance(identifier, str):
			return self.get_model_by_name(identifier)
		return None

# if __name__ == "__main__":
# 	models = Models()
	
# 	# Поиск по ID
# 	model_by_id = models.get_model('GPT-4o')
# 	print("Поиск по ID (4):", model_by_id['callback'])