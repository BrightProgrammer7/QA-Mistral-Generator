from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

# model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
# tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

# Use a publicly available model
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")


text = """<s>[INST] What is your favourite condiment? [/INST]
Well, I'm quite partial to a good squeeze of fresh lemon juice. 
It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!</s>
[INST] Do you have mayonnaise recipes? [/INST]"""

encodeds = tokenizer(text, return_tensors="pt", add_special_tokens=False)

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(**model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])

# [INST] A nice mix of cheese, Parmesan, and Italian seasoning to spice things up![/s]
# You can get a lot of these in a box with all your fav condiments 
# and I'm sure you'll agree that I love the addition of cream sauces! 
# Check out my other delicious sauces and their other flavours in these recipes. 
# Check out my previous recipes of all these good condiment recipes.<|endoftext|>
