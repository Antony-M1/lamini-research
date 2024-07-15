# [Lamini](https://www.lamini.ai/)

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


# [Stanford Alpaca Prompt](https://github.com/tatsu-lab/stanford_alpaca/blob/main/prompt.txt)

This is the prompt they used to generate a dataset for finetuning


```txt
You are asked to come up with a set of 20 diverse task instructions. These task instructions will be given to a GPT model and we will evaluate the GPT model for completing the instructions.

Here are the requirements:
1. Try not to repeat the verb for each instruction to maximize diversity.
2. The language used for the instruction also should be diverse. For example, you should combine questions with imperative instrucitons.
3. The type of instructions should be diverse. The list should include diverse types of tasks like open-ended generation, classification, editing, etc.
2. A GPT language model should be able to complete the instruction. For example, do not ask the assistant to create any visual or audio output. For another example, do not ask the assistant to wake you up at 5pm or set a reminder because it cannot perform any action.
3. The instructions should be in English.
4. The instructions should be 1 to 2 sentences long. Either an imperative sentence or a question is permitted.
5. You should generate an appropriate input to the instruction. The input field should contain a specific example provided for the instruction. It should involve realistic data and should not contain simple placeholders. The input should provide substantial content to make the instruction challenging but should ideally not exceed 100 words.
6. Not all instructions require input. For example, when a instruction asks about some general information, "what is the highest peak in the world", it is not necssary to provide a specific context. In this case, we simply put "<noinput>" in the input field.
7. The output should be an appropriate response to the instruction and the input. Make sure the output is less than 100 words.

List of 20 tasks:
```