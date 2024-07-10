# Lamini

Lamini makes it possible for enterprises to turn proprietary data into the next generation of LLM capabilities.

Here a tutorial [Link](https://learn.deeplearning.ai/courses/finetuning-large-language-models)

# .env

Create a .env file
```.env
LAMINI_API_KEY=<YOUR_API_KEY>
```

# REST PAI

```curl
curl --location "https://api.lamini.ai/v1/completions" \
--header "Authorization: Bearer <LAMINI_API_KEY>" \
--header "Content-Type: application/json" \
--data '{
    "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
    "prompt": "How are you?"
}'
```

# Local Setup

### Step 1: Create Environment

```command
python3 -m venv .venv
```
```command
source .venv/bin/activate
```

### Step 2: Install dependencies

```command
pip install -r requirements.txt
```