from transformers import T5Tokenizer, T5ForConditionalGeneration
import re


class LlmModel:
    def __init__(self):
        print("loading model")
        self.tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
        self.model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

    def response(self, input_text):
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        text = self.tokenizer.decode(outputs[0])
        print(text)
        pattern = r"<[^>]+>"
        cleaned_output = re.sub(pattern, "", text)
        print(cleaned_output)
        return cleaned_output.strip()


llm_obj = LlmModel()