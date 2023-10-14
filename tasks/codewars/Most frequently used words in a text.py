import string
def top_3_words(text):
    for symb in string.punctuation.replace("'", ""):
        text = text.replace(symb, "")
        
    print(text)
    
    worsddsd