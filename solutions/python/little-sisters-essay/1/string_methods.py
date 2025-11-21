def capitalize_title(title):
    return str.title(title)

def check_sentence_ending(sentence):
    if sentence[-1]==".":
        return True
    else :
        return False
def clean_up_spacing(sentence):
    return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
    a=sentence.replace(old_word,new_word)
    return a
    