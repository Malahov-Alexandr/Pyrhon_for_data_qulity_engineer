text = '''  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''
cap_tex = ''
# split the text in sentences and delete \n
ls_text = text.split()
new_text = ' '.join(ls_text)
# do all letters lower case
text_1 = new_text.lower()
# replase 'iz' with 'is
text_3 = text_1.replace('iz','is')
#back 'iz' in correct place
text_4 = text_3.replace(' fix“is” ', ' fix“iz” ')
last_text = text_4.split(". ")
final =[]
# capitalize first letter of the sentence
for i in last_text:
    final.append(i.capitalize())
perfect_text = '. '.join(final)

#Need to add the last words of each sentense
ls = perfect_text.split('.')
last_w = []
for part in ls:
    s = part.split()
    if s != '8' and s != '7':
        last_w.extend(s[-1:])
the_latest_text = perfect_text[:223] + ' '+' '.join(last_w)+' '+ perfect_text[222:]
print(the_latest_text)
print(text.count(' '))
