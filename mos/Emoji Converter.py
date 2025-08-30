message = input(">")
words = message.split(' ')
emojis = {
    ":)" "sml"
    ":(" "sad"
}
output = ""
for word in words:
    emojis.get(words, word) + " "
print(output)