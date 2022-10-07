text = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


def delete_empty_elements(text):
    text = text.replace('\n', '')
    text = text.replace('  ', ' ')
    return text


def normalize_text(text):
    text_new = []
    text = text.lower()
    text_sep = text.split('. ')
    for sentense in text_sep:
        each_sentense = sentense.strip()
        text_new.append(each_sentense.capitalize())
    new_text = '. '.join(text_new)
    return new_text


def create_a_new_sentense(text):
    ls = text.split('.')
    last_w = []
    for part in ls:
        s = part.split()
        last_w.extend(s[-1:])
    new_sentense = ' '.join(last_w)
    return new_sentense.capitalize()


def add_new_sentense_after_the_word(text):
    word = 'paragraph'
    index = text.index(word)
    new_string = text[:index + len(word) + 2] + create_a_new_sentense(text) + text[index + len(word):]
    return new_string


def correction_of_the_text(text):
    text = text.replace('iz', 'is')
    text = text.replace('“is”', ' “iz”')
    text = text.replace('normalise', 'normalize')
    return text


def counter_of_elements(text):
    element_1 = ' '
    return text.count(element_1)


print(correction_of_the_text(add_new_sentense_after_the_word(normalize_text(delete_empty_elements(text)))))
print(counter_of_elements(
    correction_of_the_text(add_new_sentense_after_the_word(normalize_text(delete_empty_elements(text))))))
