import os

from .utils.models import Models
from .utils.settings import Settings
from .utils.objects import flux_2, Model_sdxl_flash
class Diffusion:
	def __init__(self, Interfice_Tor):
		self.models = Models()
		self.Interfice_Tor = Interfice_Tor

	def create(self, prompt, path='./media/image.jpg', settings=None, model=1, proxy=False):
		os.makedirs(os.path.dirname(path), exist_ok=True)
		if (model == 1 or model == 'flux-2') and settings == None:
			return flux_2(self.Interfice_Tor).create(prompt, path, proxy=proxy)
		else:
			if not settings:
				if model == 2 or model == 'sdxl_flash':
					settings = Settings(model)
		
		if isinstance(settings, Settings):
			return Model_sdxl_flash(prompt, path, settings, self.Interfice_Tor).create(proxy=proxy)