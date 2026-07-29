letter = '''Dear <|name|>,
You are selected!
<|date|>'''

print(letter.replace("<|name|>", "Harry").replace("<|date|>", "24 December 2025"))