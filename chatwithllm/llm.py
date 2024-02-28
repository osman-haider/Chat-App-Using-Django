from transformers import T5Tokenizer, T5ForConditionalGeneration
import re

def llm_output(input_text,model,tokenizer):
    if model is None:
        tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
        model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

        input_ids = tokenizer(input_text, return_tensors="pt").input_ids

        outputs = model.generate(input_ids)
        text = tokenizer.decode(outputs[0])
        pattern = r"<[^>]+>"
        print("here if")
        cleaned_output = re.sub(pattern, "", text)
        return cleaned_output.strip(), model, tokenizer
    else:
        print("else")
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids

        outputs = model.generate(input_ids)
        text = tokenizer.decode(outputs[0])
        pattern = r"<[^>]+>"

        cleaned_output = re.sub(pattern, "", text)
        return cleaned_output.strip(), model, tokenizer