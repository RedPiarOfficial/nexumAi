from .system.diffusion.generator import Diffusion
from .system.completions.chat import Completion
from .utils.webtor import Interfice_Tor

class Client:
	def __init__(self):
		pass

	@property
	def completion(self):
		return Completion(Interfice_Tor)

	@property
	def diffusion(self):
		return Diffusion(Interfice_Tor)