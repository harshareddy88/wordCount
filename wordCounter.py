def count_words(text):
    words = text.split()
    return len(words)
user_input = input("Enter a sentence or paragraph: ").strip()
if not user_input:
    print("Error: No input provided. Please enter some text.")
else:
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")
