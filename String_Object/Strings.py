text = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.'''
cap_tex = ''
ls_text = text.split()
new_text = ' '.join(ls_text)
text_1 = new_text.lower()
text_2 = text_1.capitalize()
text_3 = text_2.replace('iz','is')
text_4 = text_3.replace(' fix“is” ', ' fix“iz” ')
last_text = text_4.split(". ")
final =[]
for i in last_text:
    final.append(i.capitalize())
perfect_text = '. '.join(final)
print(perfect_text)

#Need to add the last words of each sentense
ls = perfect_text.split('.')
last_w = []
for part in ls:
    s = part.split()
    if s != '':
        last_w.extend(s[-1:])
the_latest_text = perfect_text + ' '+' '.join(last_w)
print(the_latest_text)

