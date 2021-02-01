from transformers import AutoTokenizer, AutoModelWithLMHead, TextGenerationPipeline

class GePpeTto:
	def __init__(self) -> None:
		tokenizer = AutoTokenizer.from_pretrained("./models/GePpeTto")
		model = AutoModelWithLMHead.from_pretrained("./models/GePpeTto")

		self.generator = TextGenerationPipeline(model = model, tokenizer = tokenizer)

	def generate_text(self, prompt):
		output = self.generator(prompt)
		print(output)
		return output[0]["generated_text"][len(prompt):]

generator = GePpeTto()
print(generator.generate_text("ciao"))