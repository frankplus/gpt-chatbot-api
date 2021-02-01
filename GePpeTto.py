from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline

class GePpeTto:
	def __init__(self) -> None:
		tokenizer = AutoTokenizer.from_pretrained("./models/GePpeTto")
		model = AutoModelWithLMHead.from_pretrained("./models/GePpeTto")

		self.generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

	def generate_text(self, prompt):
		output = self.generator(
			prompt, 
			do_sample=True,
			max_length=50,
			top_k=50,
			top_p=0.95,
			num_return_sequences=1
		)
		print(output)
		return output[0]["generated_text"][len(prompt):]