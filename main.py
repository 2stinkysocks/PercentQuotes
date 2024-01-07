doc = open("document.txt", "r", encoding='utf-8')
text = " ".join(doc.readlines())
doc.close()

quote = 0
textn = 0

isquote = False

def addWord():
    global isquote
    if isquote:
        global quote
        quote += 1
    else:
        global textn
        textn += 1

def toggleQuote():
    global isquote
    if isquote: 
        isquote = False
    else:
        isquote = True

for ch in text:
    if ch == " " or ch == "…":
        addWord()
    elif ch == "\"" or ch == "“" or ch == "”":
        toggleQuote()

print("Total words: ", quote+textn)
print("Quotes: ", quote)
print("Text: ", textn)
print("Percent not quotes: ", 100*(textn/(quote+textn)))
while True:
    pass
