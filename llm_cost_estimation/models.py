# Define a list of OpenAI models, with descriptions, max tokens, and per-token costs
# for prompts and completions for each model
models = [
    {
        "name": "gpt-3.5-turbo-instruct",
        "description": "Same capabilities as the standard gpt-3.5-turbo model but "
        "uses completion rather than chat completion enpoint",
        "max_tokens": "4096",
        "prompt_cost_per_token": "1.5 / 1000000",
        "completion_cost_per_token": "2 / 1000000",
    },
    {
        "name": "gpt-3.5-turbo",
        "description": "Most capable GPT-3.5 model and optimized for chat at 1/10th "
        "the cost of text-davinci-003. Will be updated with our latest model "
        "iteration.",
        "max_tokens": "16385",
        "prompt_cost_per_token": "0.5 / 1000000",
        "completion_cost_per_token": "1.5 / 1000000",
    },
    {
        "name": "gpt-3.5-turbo-16k",
        "description": "Deprecated; same capabilities as the standard gpt-3.5-turbo model",
        "max_tokens": "16385",
        "prompt_cost_per_token": "3 / 1000000",
        "completion_cost_per_token": "4 / 1000000",
    },
    {
        "name": "gpt-4-32k",
        "description": "Same capabilities as the base gpt-4 mode but more context length.",
        "max_tokens": "32768",
        "prompt_cost_per_token": "30 / 1000000",
        "completion_cost_per_token": "0.12 / 1000",
    },
    {
        "name": "gpt-4-turbo",
        "description": "More capable than any GPT-3.5 model, able to do more complex tasks, and optimized for chat.",
        "max_tokens": "128000",
        "prompt_cost_per_token": "10 / 1000000",
        "completion_cost_per_token": "30 / 1000000",
    },
    {
        "name": "gpt-4",
        "description": "More capable than any GPT-3.5 model, able to do more complex tasks, and optimized for chat. Will be updated with our latest model iteration.",
        "max_tokens": "8192",
        "prompt_cost_per_token": "30 / 1000000",
        "completion_cost_per_token": "60 / 1000000",
    },
    {
        "name": "davinci-002",
        "description": "Fine-tunable base instruction model with instruct and code completions.",
        "max_tokens": "4097",
        "prompt_cost_per_token": "12 / 1000000",
        "completion_cost_per_token": "12 / 1000000",
    },
    {
        "name": "babbage-002",
        "description": "Fast, light, short-context fine-tunable base instruction model.",
        "max_tokens": "2049",
        "prompt_cost_per_token": "1.6 / 1000000",
        "completion_cost_per_token": "1.6 / 1000000",
    },
]
