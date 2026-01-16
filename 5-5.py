# Paragraph word count
paragraph = "cat dog mouse cat dog cat"
words = paragraph.split()
word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

for w, c in word_count.items():
    print(f"{w}: {c}")