def mad_libs_with_nouns(phrase):
  count = 0

  for i in range (len(phrase)):
    if phrase[i] == "_":
      count += 1

  print ("List " + str(count) + " noun(s). ")

  phrase_2 = phrase

  for i in range (count):
    noun = input("Enter a noun: ")
    underscore = phrase_2.index('_')
    phrase_2 = (phrase_2[:underscore] + noun + phrase_2[underscore+1:])
  
  return phrase_2


sentences = ['I really like _(s).',
  'I never start the day without my _(s).',
  '_(s), _(s), and _(s)  are my favorite things.',
  'The _ is mad at me.',
  'The _ jumped over the _.']

for i in range (len(sentences)):
  print(mad_libs_with_nouns ( sentences [i]))
