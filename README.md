#Helpingai_T2

A simple module/way to use Perplexity AI in Python.

## Get started:

```
python -m pip install -U Helpingai_T2 
```

## Example:

```python
from Helpingai_T2 import Perplexity

prompt = input("👦: ")
for a in Perplexity().generate_answer(prompt):
    print(f"🤖: {a['answer']}")
```

