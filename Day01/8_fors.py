def printword():
    words = ["Imagination", "Is", "more" ,"important", "than", "knowledge"]
    newwords = []
    for word in words:
        print("The Word \"", word, "has",len(word), "characters")
        if len(word) > 5:
            newwords.append(word)
    print (newwords)
