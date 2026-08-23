import re
from collections import Counter

def top_three_words(text: str):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    freq = Counter(words)
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:3]

if __name__ == "__main__":
    text = input().strip()
    results = top_three_words(text)
    for word, count in results:
        print(f"{word}:{count}")
