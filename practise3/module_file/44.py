filepath=''' The Mars Helicopter, Ingenuity, is a technology demonstration to test powered, 
controlled   flight on another world for the first time. 
It hitched a ride to Mars   on the  Perseverance rover. 
   Once the rover reached a   suitable "airfield" location, 
it released Ingenuity to the surface   so it could perform a series 
  of test flights over a  30-Martian-day experimental window.'''
def count_words(filepath):
    import re
    # with open(filepath,'r+') as f:
    #     file=f.read()
    #a=re.sub("\s\s+","\n",th) # after word which dont have " " will be changed by "\n"
    file=filepath
    a=re.sub("\s\s+"," ",file)
    a=a.strip()
    print(len(a.split(' ')))
count_words(filepath)
