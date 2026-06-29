#function to check if a word is palindrome.

def check_word(word):
    if word==word[ : :-1]:
        print(f"The word \'{word}\' is palindrome ")
    else:
        print(f"The word \'{word}\'  is not palindrome")
word=input("enter a word :")
check_word(word)