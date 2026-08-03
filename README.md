# Very Simple Python AI Agents

This tiny project uses the OpenAI Agents SDK. A coordinator sends requests to:

- a **math helper**, which adds two numbers; or
- a **friendly helper**, which greets you and reports the UTC time.

## Set up

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Put your OpenAI API key in `.env`, then export it into the shell:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Do not commit your real API key.

## Run

Pass one simple request on the command line:

```bash
python simple_agents.py "add 7 and 5"
python simple_agents.py "what time is it?"
python simple_agents.py "hello!"
```

The program makes an OpenAI API request, so running it can use API credits.

## Test

The basic tools can be tested without an API key:

```bash
python -m pytest
```
