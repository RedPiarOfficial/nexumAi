from nexum import Client
from nexum.system.completions.utils.models import Models
from nexum.system.diffusion.utils.settings import Settings
from nexum.utils.webtor import Interfice_Tor

# Quick start
print('-'*30 + '\n')
client = Client()

messages = [{'role': 'user', 'content': 'Hello!'}]
print(client.completion.create(messages))

# Change model + Display used model via model_check
print('-'*30 + '\n')
client = Client()

messages = [{'role': 'user', 'content': 'Hello!'}]
print(client.completion.create(messages, model_check=True, model=2))

# View all models
print('-'*30 + '\n')
print(Models().get_models())

print(Models().get_model_by_id(1))  # Search by ID
print(Models().get_model_by_name('Gemini-2.0-F-Thinking'))  # Search by name
print(Models().get_model(1))  # Contains functionality of both get_model_by_id and get_model_by_name, determines the search type automatically

# Image generation
print('-'*30 + '\n')
client = Client()
print(client.diffusion.create('cute anime cat'))

# Image generation + Change model
print('-'*30 + '\n')
client = Client()
print(client.diffusion.create('nude cute anime girl neko', path='./media/girl.png', model=2))

# Settings for model 2 for image generation
print('-'*30 + '\n')
settings = Settings(model=2)
client = Client()
settings.negative_prompt('(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation')
settings.set_seed('random')
settings.set_resolution((1024, 1024))
settings.set_steps(15)
print(client.diffusion.create('cute anime girl neko', path='./media/girl_steps_15.png', model=2, settings=settings))

# Get all image generation models
print('-'*30 + '\n')
from nexum.system.diffusion.utils.models import Models

print(Models().get_models())
print(Models().get_model_by_id(1))  # Search by ID
print(Models().get_model_by_name('sdxl-flash'))  # Search by name
print(Models().get_model(1))  # Contains functionality of both get_model_by_id and get_model_by_name, determines the search type automatically

# Connect Tor proxy to bypass possible restrictions
print('-'*30 + '\n')
# Interfice_Tor.install_tor() - if Tor is not installed
Interfice_Tor.new_ip()
client = Client()

messages = [{'role': 'user', 'content': 'Hello!'}]
print(client.completion.create(messages, model_check=True, model=2, proxy=True))
print(client.diffusion.create('cute anime cat', proxy=True))

