# let's cheat at Spelling Bee

def word_reader(filename):
  # returns an iterator
  return (word.strip() for word in  open(filename)) 

if __name__ == "__main__":
  import sys
  if len(sys.argv) == 2: 
    rack = sys.argv[1].strip()
    if len(rack) != 7: 
      print( "7 letters required, ",len(rack), "entered - <enter required letter + six more>")
      exit()
  else:
    print("Usage: python cheat_at_Spelling Bee.py <enter required letter + six more>")
    exit()

  reqLet = rack[0] # required letter is first

  words = word_reader('wordList.txt')

  for word in words:
    if set(word.lower()).issubset(set(rack)):
      if (reqLet in word.lower()) and len(word) > 3:
        print(word)


  print("---------Done------------")


