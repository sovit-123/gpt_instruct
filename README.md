# gpt_instruct
GPT instruct based models in less than a billion parameters.

GPT 2 model trained on the Alpaca dataset for slightly over 50000 steps released.
Download and extract the `infer_model.zip` file (**see Releases**) in the project directory and run `gpt2_instruct.py --prompt "<your prompt>"`.
Prompt should be within quotes.

**Example**

```
python gpt2_instruct.py --prompt "Give three points on how to stay healthy."
```

Output:

```
1. Eat nutritious food that is low in fat. 
2. Get enough sleep and rest every night. 
3. Follow recommended guidelines for exercise.
```



***If you retrain the model, copy the models, tokenizers, merges, ... from the resulting folder into the `infer_model` folder or change the path in the `gpt_instruct.py` file***
