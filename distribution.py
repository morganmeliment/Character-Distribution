"""
distribution.py
Author: Morgan Meliment
Credit: http://stackoverflow.com/questions/4659524/how-to-sort-by-length-of-string-followed-by-alphabetical-order, http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
inputstr = input("Please enter a string of text (the bigger the better): ").lower()
print("The distribution of characters in " + '"' + inputstr + '"' + " is:")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
tprint = []
for x in alphabet:
    count = inputstr.count(x)
    q = 0
    uy = []
    while q < count:
        q += 1
        uy.append(x)
    if uy != []:
        fin = "".join(c for c in uy)
        tprint.append(fin)
sakd = tprint.sort(key = len, reverse=True)
for d in sakd:
    print(d)






