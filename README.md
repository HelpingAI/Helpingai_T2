# Helpingai_T2

Helpingai_T2 is a Python module that allows you to interact with the Perplexity AI. It's simple to use and can be easily integrated into your Python projects.

## Installation

You can install Helpingai_T2 using pip. Run the following command in your terminal:

```bash
python -m pip install -U Helpingai_T2 
```

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

## Community

- **Discord**: Join our vibrant community of developers and users on Discord. [Join Discord](https://discord.gg/3fJENZMzqY)
- **YouTube**: Subscribe to our YouTube channel, [OEvortex](https://youtube.com/@OEvortex?si=-NVlePE4S6jFAVBx), for video tutorials and updates.
- **Telegram**: Join our Telegram group for discussions and support. [Join Telegram](https://t.me/+DjtjCbsEV7k3NDll)

---
