class Models:
	def __init__(self):
		self.models = self.get_models()

	def get_models(self):
		return {
	"Google": [
		{
			"model_id": 1,
			"model_name": "Gemini-2.0-F-Thinking",
			"description": "текстовая модель нового поколения с глубоким пониманием контекста, способная генерировать осмысленные, точные и логичные ответы.",
			"callback": 'gemini-2.0-flash-thinking'
		},
		{
			"model_id": 2,
			"model_name": "Gemini-2.0-Flash",
			"description": "высокоскоростная модель генерации текста, обеспечивающая мгновенные, точные и лаконичные ответы с отличным пониманием контекста.",
			"callback": "gemini-2.0-flash"
		},
		{
			"model_id": 3,
			"model_name": "Gemini-1.5-Flash",
			"description": "быстрая и эффективная модель генерации текста, предоставляющая краткие, ясные и точные ответы с хорошим пониманием пользовательских запросов.",
			"callback": "gemini-1.5-flash"
		}
	],
	"OpenAI": [
		{
			"model_id": 4,
			"model_name": "GPT-4o",
			"description": "мультимодальная модель от OpenAI, способная обрабатывать и генерировать текст. Она поддерживает более 50 языков, обеспечивает быструю и точную обработку данных, а также улучшенное понимание контекста.",
			"callback": "gpt-4o-latest" 
		},
		{
			"model_id": 5,
			"model_name": "O1-Mini",
			"description": "эффективная модель ИИ от OpenAI, оптимизированная для задач STEM, особенно в математике и программировании. Она обеспечивает высокую производительность при сниженных затратах и времени отклика.",
			"callback": "o1-mini"
		}
	],
	"DeepSeek": [
		{
			"model_id": 6,
			"model_name": "Deepseek-R1-Distill",
			"description": "серия компактных моделей, полученных методом дистилляции из DeepSeek-R1, обеспечивающих высокую производительность в задачах рассуждения и программирования.",
			"callback": "deepseek-r1"
		}
	],
	"Meta": [
		{
			"model_id": 7,
			"model_name": "Llama-3.3",
			"mind": "70B",
			"description": "продвинутая языковая модель от Meta с 70 миллиардами параметров, обеспечивающая высокое качество генерации текста",
			"callback": "Llama-3.3-70B"
		},
		{
			"model_id": 8,
			"model_name": "Llama-3.1",
			"mind": "405B",
			"description": "крупнейшая открытая языковая модель от Meta с 405 миллиардами параметров, превосходящая GPT-4o в нескольких тестах и поддерживающая контекст до 128 тысяч токенов.",
			"callback": "Llama-3.1-405B"
		}
	],
	"Alibaba": [
		{
			"model_id": 9,
			"model_name": "Qwen2.5",
			"mind": "72B",
			"description": "продвинутая языковая модель от Alibaba Cloud с 72,7 миллиардами параметров. Она поддерживает контекст до 128 тысяч токенов, улучшена в области кодирования и математики, а также поддерживает более 29 языков.",
			"callback": "Qwen2.5-72B"
		},
	],
	"xAI": [
		{
			"model_id": 11,
			"model_name": "Grok-2",
			"description": "продвинутая языковая модель от xAI, разработанная по инициативе Илона Маска. Она интегрирована с платформой X (бывший Twitter) и обладает возможностями генерации изображений с помощью технологии FLUX.1 от Black Forest Labs. Grok-2 известна своим чувством юмора и способностью обрабатывать информацию в реальном времени, предоставляя актуальные ответы на запросы пользователей.",
			"callback": "grok-2-1212"
		},
		{
			"model_id": 12,
			"model_name": "Grok-Beta",
			"description": "экспериментальная языковая модель от xAI, запущенная в августе 2024 года. Она улучшает возможности рассуждения, превосходя Grok-2, и поддерживает контекст до 131072 токенов.",
			"callback": "grok-beta"
		}
	],
	"ToolBaz": [
		{
			"model_id": 13,
			"model_name": "ToolBaz-v3.5-Pro",
			"description": "продвинутая языковая модель от ToolBaz, использующая искусственный интеллект для генерации высококачественного текста. Она анализирует вводимые данные и предлагает улучшения стиля, грамматики и словарного запаса, а также генерирует оригинальный контент, включая статьи, сценарии и сообщения в социальных сетях. Модель обеспечивает быстрые и точные результаты, повышая эффективность и продуктивность пользователей.",
			"callback": "toolbaz_v3.5_pro"
		},
		{
			"model_id": 14,
			"model_name": "ToolBaz-v3",
			"description": "языковая модель, интегрированная в инструменты ToolBaz, использующая искусственный интеллект для генерации текста.",
			"callback": "toolbaz_v3"
		}
	],
	"Mixtral": [
		{
			"model_id": 15,
			"model_name": "Mixtral",
			"mind": "141B",
			"description": "мощная языковая модель от Mistral AI, состоящая из 8 экспертов по 22 миллиарда параметров каждый. Благодаря архитектуре Mixture-of-Experts, она эффективно использует 39 миллиардов активных параметров из 141 миллиарда, обеспечивая высокую производительность при сниженных вычислительных затратах.",
			"callback": "mixtral_8x22b"
		}
	],
	"Unfiltered": [
		{
			"model_id": 16,
			"model_name": "L3-Euryale-v2.1",
			"mind": "70B",
			"description": "продвинутая языковая модель, основанная на архитектуре LLaMA-3, с 70,6 миллиардами параметров.",
			"callback": "L3-70B-Euryale-v2.1"
		},
		{
			"model_id": 17,
			"model_name": "Midnight-Rose",
			"description": None,
			"callback": "midnight-rose"
		},
		{
			"model_id": 18,
			"model_name": "Unity",
			"description": None,
			"callback": "unity"
		},
		{
			"model_id": 19,
			"model_name": "Unfiltered_X",
			"mind": "141B",
			"description": None,
			"callback": "unfiltered_x"
		}
	]}	
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