## Basic request

To send your first API request with the [OpenAI Python SDK](https://github.com/openai/openai-python), make sure you have the right [dependencies installed](https://platform.openai.com/docs/quickstart?context=python) and then run the following code:

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
```


## Setup

1. If you don’t have Python installed, install it [from Python.org](https://www.python.org/downloads/).

2. Navigate into the project directory:

   ```bash
   $ cd OpenAI_domain_classifier

   ```
4. create .env file and copy the content of .env-example file there. Then, place your API_KEY as stated.
5. Create a new virtual environment:

   - macOS:

     ```bash
     $ python -m venv venv
     $ . venv/bin/activate
     ```

   - Windows:
     ```cmd
     > python -m venv venv
     > .\venv\Scripts\activate
     ```

6. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```


```bash
$ cd classifier-flask
$ flask run
```

You should now be able to access the app from your browser at the following URL: [http://localhost:5000](http://localhost:5000)!
