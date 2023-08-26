import logging as log
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
from transformers import AutoTokenizer, AutoModel

log.basicConfig(level=log.INFO, filename="logs3bv2.log", filemode="a", format="%(asctime)s %(levelname)s %(message)s")

log.info('Start program')

model_path = 'modellama3bv2'

tokenizer = LlamaTokenizer.from_pretrained(model_path)

model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.bfloat16, device_map='auto', offload_folder="offload3bv2"
)
log.info('Model ready')
prompt = 'Not repeat answer. How to'
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=100
)

print(tokenizer.decode(generation_output[0]))
print(type(generation_output[0]))

log.info('End program')
# def start_model_llama_7bv2():
#
# def run_open_llama_7bv2(prompt, is_quesion):
#     pass
