import argparse

from transformers import pipeline

parser = argparse.ArgumentParser()
parser.add_argument(
    '--prompt',
    default='How to be a good programmer?'
)
args = parser.parse_args()

def get_response(output=None):
    response = output[0]['generated_text'].split('### Response:')[1]
    if 'Below is an instruction that describes' in response:
        response = response.split('Below is an instruction')[0]
    return response

pre_prompt = f"Below is an instruction that describes a task. " +\
             f"Write a response that appropriately completes the request. "+\
             f"### Instruction: "
prompt = args.prompt

final_prompt = pre_prompt + prompt

print(args.prompt)

generator = pipeline(
    "text-generation", 
    model=f"infer_model",
)

output = generator(final_prompt, max_length=512)

print(get_response(output))