# Helpingai_T2

Helpingai_T2 is a Python module that allows you to interact with the Perplexity AI. It's simple to use and can be easily integrated into your Python projects.

## Installation

You can install Helpingai_T2 using pip. Run the following command in your terminal:

```bash
python -m pip install -U Helpingai-T2
```

Join our [Discord server](https://discord.gg/3fJENZMzqY) for live chat, support, or if you have any issues with this package.

## Support this repository:
- ⭐ **Star the project:** Star this repository. It means a lot to us! 💕
- 🎉 **Join our Discord Server:** Chat with us and others. [Join here](https://discord.gg/3fJENZMzqY)
- 📺 **Subscribe to our YouTube channel:** Stay updated with our latest tutorials and updates. [Subscribe here](https://youtube.com/@OEvortex?si=-NVlePE4S6jFAVBx)
- 📬 **Join our Telegram group:** Join our community for discussions and support. [Join here](https://t.me/+DjtjCbsEV7k3NDll)


## Usage

Here are some examples of how you can use the Helpingai_T2 module in your code:

### Single Prompt Example

This example takes a single input from the user and generates a response using the Perplexity AI.

```python
from Helpingai_T2 import Perplexity

# Get a prompt from the user
prompt = input("👦: ")

# Generate a response using the Perplexity AI
for a in Perplexity().generate_answer(prompt):
    print(f"🤖: {a['answer']}")
```

### Continuous Conversation Example

This example continuously takes input from the user and generates responses, creating an ongoing conversation with the Perplexity AI.

```python
from Helpingai_T2 import Perplexity

# Start a continuous conversation with the user
while True:
    # Get a prompt from the user
    prompt = input("👦: ")

    # Generate a response using the Perplexity AI
    for a in Perplexity().generate_answer(prompt):
        print(f"🤖: {a['answer']}")
```

