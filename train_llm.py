from transformers import GPT2LMHeadModel, GPT2Tokenizer

def train_language_model(text_data):
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    inputs = tokenizer(text_data, return_tensors="pt", max_length=1024, truncation=True)

    model.train()

    print("Fine-tuning the model...")
    model_output = model(**inputs, labels=inputs["input_ids"])
    print("Model training complete.")

    return model, tokenizer

if __name__ == "__main__":
    with open("all_text_data.txt", "r") as file:
        all_text_data = file.read()

    print("Training the Language Model...")
    trained_model, tokenizer = train_language_model(all_text_data)
    print("Training complete.")

    output_dir = "trained_llm"
    trained_model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

    print("Trained model and tokenizer saved to:", output_dir)
