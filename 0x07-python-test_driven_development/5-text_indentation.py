#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " " and text[i + 1] == " ":
            continue
        if text[i] is " " and (text[i - 1] == "." or text[i - 1] == "?" or text[i - 1] == ":"):
            continue
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()
