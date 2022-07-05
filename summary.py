from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

summaries = []


def summary_text(text):
    chapter_list = text.split("!!!")
    for chapter in chapter_list:
        summarized = summarizer(chapter, min_length=10, max_length=30)
        summaries.append(summarized)
    return summaries
  