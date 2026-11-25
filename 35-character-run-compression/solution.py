text = input("Text: ")
encoded = ""
i = 0
while i < len(text):
    char = text[i]
    count = 0
    while i < len(text) and text[i] == char:
        count += 1
        i += 1
    if char in "0123456789" or char == "\\":
        encoded += "\\"
    encoded += char + str(count)
print("Encoded:", encoded)
print("Original length:", len(text))
print("Encoded length:", len(encoded))
if len(encoded) < len(text):
    print("Compression is beneficial")
else:
    print("Compression is not beneficial")
