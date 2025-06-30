from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Load lightweight open-source model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_answer(question, context):
    prompt = f"Answer the question based on the following data:\n{context}\n\nQuestion: {question}"
    result = generator(prompt, max_length=200, do_sample=True)[0]["generated_text"]
    return result.strip()
