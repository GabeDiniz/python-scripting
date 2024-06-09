import re
from collections import Counter
from PyPDF2 import PdfReader # pip install pypdf2

def extract_text_from_pdf(pdf_file: str) -> list[str]:    # Returns a list of pages of text (i.e., ["This is page 1", "This is page 2"])
  with open(pdf_file, "rb") as pdf:
    reader = PdfReader(pdf, strict=False)

    print("Pages: ", len(reader.pages))   # Grab number of pages in the document
    print("-"*10)   # Divider

    pdf_text: list[str] = [page.extract_text() for page in reader.pages]
    return pdf_text
  
def count_words(text_list: list[str]) -> Counter:
  all_words: list[str] = []
  for text in text_list:
    split_text: list[str] = re.split(r"\s+|[,;?!.-]\s*", text.lower())  # Removes punctuation from text (i.e., Hello! -> hello)

    all_words += [word for word in split_text if word]  # Appends word so long as word != ''

  return Counter(all_words)   # Counter counts the number of words that appear


def main():
  extracted_text: list[str] = extract_text_from_pdf("sample.pdf")
  counter: Counter = count_words(text_list=extracted_text)

  for word, mentions in counter.most_common(5):
    print(f"{word:10}: {mentions} times")   # {word:10} -> the 10 reserves space which results in nicer print formatting

if __name__ == "__main__":
  main()