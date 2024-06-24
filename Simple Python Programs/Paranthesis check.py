# Bracket check Function
def Valid(inputText):
    hashBrackets = { "}":"{", ")":"(", "]":"["}
    stackTemp=[]
    # Loop char of InputText
    for currentChar in inputText:
        if stackTemp:
            previousChar = stackTemp.pop()
            if(hashBrackets.get(currentChar) == previousChar):                                       
                pass
            else:
                stackTemp.append(previousChar)
                stackTemp.append(currentChar)
        else:
            stackTemp.append(currentChar)
    if stackTemp:
        return "not Valid"
    else:
        return "Valid"            

#Input Text
inputText = "{[[]{}]}()()"
inputText1 = "([)]"
inputText2 = ")(}"

#Function Call
print(Valid(inputText))
print(Valid(inputText1))
print(Valid(inputText2))