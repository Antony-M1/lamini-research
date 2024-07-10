# Lamini


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