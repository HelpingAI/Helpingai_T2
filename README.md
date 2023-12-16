# Helpingperplexityai

A simple module/way to use Perplexity AI in Python.

## Get started:

```
python -m pip install -U Helpingai_T3 #comming soon
```

## Example:

```python
from Helpingai_T3 import Perplexity

prompt = input("👦: ")
for a in Perplexity().generate_answer(prompt):
    print(f"🤖: {a['answer']}")
```

