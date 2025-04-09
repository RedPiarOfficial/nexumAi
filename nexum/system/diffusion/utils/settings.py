from .models import Models

class Settings:
	def __init__(self, model=2):
		self.models = Models()
		self.current_model = self.models.get_model(model)
		self._current_setting = self._load_basic_settings()

	def negative_prompt(self, prompt):
		self._current_setting['negative_prompt'] = prompt
		return True

	def set_seed(self, seed):
		self._current_setting['seed'] = seed
		return True

	def set_resolution(self, res=(1024, 1024)):
		self._current_setting['height'] = res[0]
		self._current_setting['width'] = res[1]
		return True

	def set_steps(self, steps):
		self._current_setting['steps'] = steps
		return True

	@property
	def setting(self):
		return self._current_setting

	def _load_basic_settings(self):
		if self.current_model['model_name'] == 'flux-2':
			raise Exception('for this model not settings')
		elif self.current_model['model_name'] == 'sdxl-flash':
			return {
				'model': self.current_model['model_name'],
				'negative_prompt': "(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation",
				'seed': 'random',
				'height': 1024,
				'width': 1024,
				'steps': 15
			}