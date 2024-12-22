import os
import re
from collections import Counter

def create_sample_file():
    if not os.path.exists("sample.txt"):
        print("File 'sample.txt' does not exist. Please type the content below:")

        with open("sample.txt", "w") as file:
            file.write(input("Enter text: "))
            
        print("'sample.txt' created successfully.")

def word_frequency_analysis(top_n=5):
    create_sample_file()
    
    with open("sample.txt", "r") as file:
        content = file.read().lower()
    
    words = re.findall(r'\b\w+\b', content)
    word_count = Counter(words)
    total_words = sum(word_count.values())
    
    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    
    for word, count in word_count.most_common(top_n):
        print(f"{word} - {count} times")
    
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write(f"Top {top_n} Words:\n")

        for word, count in word_count.most_common(top_n):
            file.write(f"{word} - {count}\n")

    print("Results saved to 'word_count_report.txt'.")


create_sample_file()

while True:
    print("\nWord Frequency Counter")
    print("1. Analyze word frequency")
    print("2. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        top_n = int(input("Enter the number of top words to display: "))
        word_frequency_analysis(top_n)
    elif choice == "2":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")