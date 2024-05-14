from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def load_language_model(model_dir):
    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
    model = GPT2LMHeadModel.from_pretrained(model_dir)
    return model, tokenizer

def answer_question(model, tokenizer, question):
    input_text = tokenizer.encode(question, return_tensors="pt")
    attention_mask = torch.ones_like(input_text)  
    output = model.generate(input_text, attention_mask=attention_mask, pad_token_id=tokenizer.eos_token_id, max_length=1000, num_return_sequences=1, no_repeat_ngram_size=2)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    model_dir = "trained_llm"
    model, tokenizer = load_language_model(model_dir)

    while True:
        user_input = input("Ask a question (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        answer = answer_question(model, tokenizer, user_input)
        print("Answer:", answer)
