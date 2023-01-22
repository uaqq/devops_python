import re

def remove_nested_brackets(text):
    while True:
        new_text = re.sub(r"\[(.*?)\[(.*?)\](.*?)\]", r"[\1\3]", text)
        if new_text == text:
            return new_text
        text = new_text

text = input('Введите текст: ')

result = re.sub(r"\[.*?\]", "", remove_nested_brackets(text))

print(result.strip())