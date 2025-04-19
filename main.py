"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Kulhánek
email:  kulhanek.hk@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

text_1 = TEXTS[0].split()
text_2 = TEXTS[1].split()
text_3 = TEXTS[2].split()

name = (input("name:"))
password = (input("password:"))

line = ("-" * 40)

print(line)

if users.get(name) == password:
  print(f"Welcome to the app, {name}")
  print(f"We have {len(TEXTS)} texts to be analyzed.")
  print(line)

  text_number = (input("Enter a number btw. 1 and 3 to select:"))
  text_number = int(text_number)

  print(line)

  def text_analysis(text):
    print(f"There are {len(text)} words in selected text.")
    print(f"There are {len([word for word in text if word.istitle()])} titlecase words.")
    print(f"There are {len([word for word in text if word.isupper()])} uppercase words.")
    print(f"There are {len([word for word in text if word.islower()])} lowercase words.")
    print(f"There are {len([word for word in text if word.isdigit()])} numeric strings.")
    print(f"The sum of all the numbers {sum(int(word) for word in text if word.isdigit())}")

  def graph(text):
    print("LEN|OCCURENCES|NR.")
    print(line)
    import re
    from collections import Counter
    words = re.findall(r'\b\w+\b', str(text))
    lengths = [len(slovo) for slovo in words]
    lengths_counter = Counter(lengths)
    for length, quantity in sorted(lengths_counter.items()):
      print(f"{length:>2}| {'*' * quantity:<20}|{quantity}")

  if text_number == 1:
    text_analysis(text_1)
    print()
    print(line)
    graph(TEXTS[0])
    print()

  elif text_number == 2:
    text_analysis(text_2)
    print()
    print(line)
    graph(TEXTS[1])
    print()

  elif text_number == 3:
    text_analysis(text_3)
    print()
    print(line)
    graph(TEXTS[2])
    print()

else:
  print("unregistred user, terminating the program...")