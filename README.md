# Nexum Framework Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Client](#client)
5. [Text Generation API](#text-generation-api)
   - [Available Models](#available-text-models)
   - [Usage Examples](#text-usage-examples)
6. [Image Generation API](#image-generation-api)
   - [Available Models](#available-image-models)
   - [Image Generation Settings](#image-generation-settings)
   - [Usage Examples](#image-usage-examples)
7. [Tor Integration](#tor-integration)
8. [Advanced Usage](#advanced-usage)
9. [Troubleshooting](#troubleshooting)
10. [API Reference](#api-reference)

## Introduction

Nexum is a Python framework providing access to multiple AI services through a unified API. It includes:

- **Text Generation API**: Create text using various AI models, including Gemini, GPT-4, Llama, and others
- **Image Generation API**: Create images from text prompts using various diffusion models
- **Tor Integration**: Optional proxy support for enhanced privacy

Nexum is designed for ease of use while providing access to powerful artificial intelligence capabilities.

## Installation

```python
# Installation information will be added after package publication
# Likely via pip:
# pip install nexum
```

### Requirements

- Python 3.9 or higher
- For Tor integration: running Tor service on your machine

## Getting Started

Start by importing the Client class and creating a client instance:

```python
from nexum import Client

# Initialize client
client = Client()
```

## Client

The `Client` class is the main entry point for interacting with the Nexum API. It provides access to two main services:

- `completion`: For text generation
- `diffusion`: For image generation

### Basic Usage

```python
from nexum import Client

client = Client()

# Access text generation
completion = client.completion

# Access image generation
diffusion = client.diffusion
```

## Text Generation API

The text generation API allows you to create text responses using various AI models.

### Creating Text Responses

```python
from nexum import Client

client = Client()

# Create a simple response
messages = [
    {"role": "user", "content": "Hello!"}
]

# Using the default model (Gemini-2.0-F-Thinking)
response = client.completion.create(messages)
print(response)

# Using a specific model by ID
response = client.completion.create(messages, model=4)  # Uses GPT-4o
print(response)

# Using a specific model by name
response = client.completion.create(messages, model="Llama-3.3")
print(response)

# Check which model is being used
response = client.completion.create(messages, model_check=True)
print(response)

# Using Tor proxy for enhanced privacy
response = client.completion.create(messages, proxy=True)
print(response)
```

### Available Text Models

Nexum provides access to a variety of text generation models from different providers:

#### Google Models
- **Gemini-2.0-F-Thinking** (ID: 1): Deep context understanding, generating meaningful responses
- **Gemini-2.0-Flash** (ID: 2): High-speed text generation with excellent context understanding
- **Gemini-1.5-Flash** (ID: 3): Fast and efficient text generation with good understanding of user queries

#### OpenAI Models
- **GPT-4o** (ID: 4): Multimodal model supporting more than 50 languages with improved context understanding
- **O1-Mini** (ID: 5): Optimized for STEM tasks, especially mathematics and programming

#### DeepSeek Models
- **Deepseek-R1-Distill** (ID: 6): Compact models for reasoning and programming tasks

#### Meta Models
- **Llama-3.3** (ID: 7): Advanced language model with 70 billion parameters
- **Llama-3.1** (ID: 8): Large language model with 405 billion parameters and context up to 128k tokens

#### Alibaba Models
- **Qwen2.5** (ID: 9): Model with 72.7 billion parameters and context up to 128k tokens, improved for coding and mathematics

#### xAI Models
- **Grok-2** (ID: 11): Advanced language model with image generation capabilities
- **Grok-Beta** (ID: 12): Experimental model with improved reasoning

#### ToolBaz Models
- **ToolBaz-v3.5-Pro** (ID: 13): Advanced text generation model
- **ToolBaz-v3** (ID: 14): Basic text generation model

#### Mixtral Models
- **Mixtral** (ID: 15): Powerful model with 141 billion parameters using Mixture-of-Experts architecture

#### Unfiltered Models
- **L3-Euryale-v2.1** (ID: 16): Model with 70 billion parameters based on LLaMA-3 architecture
- **Midnight-Rose** (ID: 17): Unfiltered language model
- **Unity** (ID: 18): Unfiltered language model
- **Unfiltered_X** (ID: 19): Unfiltered model with 141 billion parameters

### Text Usage Examples

```python
from nexum import Client
from nexum.system.completions.utils.models import Models

# Initialize client
client = Client()

# Create a request with model display
messages = [{'role': 'user', 'content': 'Hello!'}]
response = client.completion.create(messages, model_check=True, model=2)
print(response)

# View all available models
all_models = Models().get_models()
print(all_models)

# Find model by ID
model = Models().get_model_by_id(1)
print(model)

# Find model by name
model = Models().get_model_by_name('Gemini-2.0-F-Thinking')
print(model)

# Universal model search (by ID or name)
model = Models().get_model(1)  # By ID
print(model)
model = Models().get_model('Gemini-2.0-F-Thinking')  # By name
print(model)
```

## Image Generation API

The image generation API allows you to create images from text prompts using various diffusion models.

### Creating Images

```python
from nexum import Client
from nexum.system.diffusion.utils.settings import Settings

client = Client()

# Generate image with default settings
prompt = "cute anime cat"
client.diffusion.create(prompt)  # Saves to ./media/image.jpg

# Using specific model and save path
client.diffusion.create("beautiful mountain landscape", path="./output/landscape.jpg", model="flux-2")

# Custom settings (only for sdxl-flash model)
settings = Settings(model=2)  # Initialize settings for sdxl-flash
settings.set_resolution((768, 512))  # Set custom resolution
settings.set_steps(20)  # Set the number of output steps
settings.negative_prompt("blurry, low quality")  # Set custom negative prompt

client.diffusion.create(
    "cute anime girl", 
    path="./output/custom_anime.jpg", 
    settings=settings,
    model=2
)

# Using Tor proxy
client.diffusion.create("cute anime cat", path="./output/proxy_cat.jpg", proxy=True)
```

### Available Image Models

Nexum currently supports the following image generation models:

1. **flux-2** (ID: 1)
   - Styles: Realistic and Anime
   - NSFW content: Not supported
   - Settings: Not customizable

2. **sdxl-flash** (ID: 2)
   - Styles: Realistic and Anime
   - NSFW content: Supported
   - Settings: Fully customizable

### Image Generation Settings

For models that support custom settings (currently only sdxl-flash), you can configure the following parameters:

```python
from nexum.system.diffusion.utils.settings import Settings

settings = Settings(model=2)  # Initialize settings for sdxl-flash

# Set custom negative prompt
settings.negative_prompt("low quality, blurry, distorted")

# Set specific seed for reproducible results (or 'random' for random seed)
settings.set_seed(42)  # Or settings.set_seed('random')

# Set custom resolution (height, width)
settings.set_resolution((768, 512))  

# Set the number of output steps (more = more details but slower)
settings.set_steps(20)
```

Default settings for sdxl-flash:
- Negative prompt: `(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation`
- Seed: random
- Resolution: 1024x1024
- Steps: 15

### Image Usage Examples

```python
from nexum import Client
from nexum.system.diffusion.utils.models import Models
from nexum.system.diffusion.utils.settings import Settings

# Initialize client
client = Client()

# Basic image generation
client.diffusion.create('cute anime cat')  # Saves to ./media/image.jpg

# Generation using specific model and save path
client.diffusion.create('cute anime girl', path='./media/girl.png', model=2)

# Generation with custom settings
settings = Settings(model=2)
settings.negative_prompt('(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy...')
settings.set_seed('random')
settings.set_resolution((1024, 1024))
settings.set_steps(15)
client.diffusion.create(
    'cute anime girl', 
    path='./media/girl_steps_15.png', 
    model=2, 
    settings=settings
)

# View all available image generation models
diffusion_models = Models().get_models()
print(diffusion_models)

# Find model by ID or name
model = Models().get_model(1)  # By ID
print(model)
model = Models().get_model('flux-2')  # By name
print(model)
```

## Tor Integration

Nexum provides optional Tor proxy integration for enhanced privacy. This feature requires a running Tor service on your machine.

### Using Tor Proxy

Add the `proxy=True` parameter to any API call:

```python
# Generate text with Tor proxy
response = client.completion.create(messages, proxy=True)

# Generate image with Tor proxy
client.diffusion.create(prompt, path="./output/image.jpg", proxy=True)
```

### Tor Utilities

```python
from nexum.utils.webtor import Interfice_Tor

# Install Tor if not installed
# Interfice_Tor.install_tor()

# Get a new Tor IP address
Interfice_Tor.new_ip()

# Check your current Tor IP address
current_ip = Interfice_Tor.check_ip()
print(current_ip)

# Complete example using Tor
Interfice_Tor.new_ip()
nexus = Client()

messages = [{'role': 'user', 'content': 'Hello!'}]
print(nexus.completion.create(messages, model_check=True, model=2, proxy=True))
print(nexus.diffusion.create('cute anime cat', proxy=True))
```

install_tor - works only on Windows, automatic installation on macOS and Linux is not available, but you can download it manually from the [official website](https://archive.torproject.org/tor-package-archive/torbrowser).

## Advanced Usage

### Multi-Turn Conversations

```python
from nexum import Client

client = Client()

messages = [
    {"role": "user", "content": "Hi, can you help me with a Python task?"},
    {"role": "ai", "content": "Of course! I'd be happy to help with your Python task. What are you working on?"},
    {"role": "user", "content": "How do I sort a dictionary by value in Python?"}
]

response = client.completion.create(messages)
print(response)

# Add the response to continue the conversation
messages.append({"role": "ai", "content": response})
messages.append({"role": "user", "content": "Can you show me another example?"})

response = client.completion.create(messages)
print(response)
```

### Checking Available Models

```python
from nexum.system.completions.utils.models import Models

models = Models()
all_models = models.get_models()

# Output all available models
for provider, provider_models in all_models.items():
    print(f"\n{provider} Models:")
    for model in provider_models:
        print(f"  - {model['model_name']} (ID: {model['model_id']})")
        if model['description']:
            print(f"    Description: {model['description']}")
```

## Troubleshooting

### Common Issues

1. **Connection Errors**
   - Ensure your internet connection is stable
   - When using Tor, check that the Tor service is running on your machine

2. **Model Not Found**
   - Double-check the model ID or name
   - Use the `Models` class to get a list of available models

3. **Image Generation Failure**
   - Ensure the directory for saving images exists or use `os.makedirs()` to create it
   - Try a different model or a simpler prompt

### Getting Help

If you encounter issues not described in this documentation, please:
- Check the updated documentation
- Look for similar issues in the project repository
- Submit a detailed bug report with your code and error messages

## API Reference

### Client

```python
Client()
```

**Properties:**
- `completion`: Access to the text generation API
- `diffusion`: Access to the image generation API

### Completion

```python
client.completion.create(messages, model=1, model_check=False, proxy=False)
```

**Parameters:**
- `messages`: List of message dictionaries with 'role' and 'content' keys
- `model`: Model ID (int) or name (str), default 1 (Gemini-2.0-F-Thinking)
- `model_check`: Whether to include model information in the response, default False
- `proxy`: Whether to use Tor proxy, default False

**Returns:**
- Generated text response as a string

### Diffusion

```python
client.diffusion.create(prompt, path='./media/image.jpg', settings=None, model=1, proxy=False)
```

**Parameters:**
- `prompt`: Text prompt for image generation
- `path`: Output file path, default './media/image.jpg'
- `settings`: Optional Settings object for customizable models
- `model`: Model ID (int) or name (str), default 1 (flux-2)
- `proxy`: Whether to use Tor proxy, default False

**Returns:**
- Boolean indicating success or failure

### Settings

```python
Settings(model=2)
```

**Methods:**
- `negative_prompt(prompt)`: Set negative prompt
- `set_seed(seed)`: Set generator seed (int or 'random')
- `set_resolution(res=(height, width))`: Set output resolution
- `set_steps(steps)`: Set output steps

**Property:**
- `setting`: Get current settings dictionary
