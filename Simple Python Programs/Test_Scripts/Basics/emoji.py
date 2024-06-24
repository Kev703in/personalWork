
def emojiChecker(message):
    messageWords=message.split(" ")
    emojis={":)":"🙂",":D":"😀",":(":"😞"}
    outputMessage=""
    for word in messageWords:
        outputMessage += emojis.get(word, word) +" "
    return outputMessage

message = input(">")
message = emojiChecker(message)
print(message)