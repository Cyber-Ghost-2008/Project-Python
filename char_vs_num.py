def main(sentence):
    constant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowels = "aeiouAEIOU"
    digits = "1234567890"
    s_characters = "!@#$%^&\*()_+=-[]}{?/.>,<|"
    constant_count = 0
    vowel_count = 0
    digits_count = 0
    s_characters_count = 0

    for char in sentence:
        if char in constant:
            constant_count = constant_count + 1
        if char in vowels:
            vowel_count = vowel_count + 1

        if char in digits:
            digits_count = digits_count + 1

        if char in s_characters:
            s_characters_count = s_characters_count + 1

    print(f"Vowels: {vowel_count}")
    print(f"Constants: {constant_count}")
    print(f"Special Characters: {s_characters_count}")
    print(f"Digits: {digits_count}")
    
sentence = input("Enter the word: ")
main(sentence)