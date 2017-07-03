print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' #replaces %s with snow. %s stands for string
#Could do with this too
print "Its fleece was white as {}.".format("snow")
print "And everywhere that Mary went."
print "." * 10  # what'd that do?


end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens

#With a comma, it puts the words in one line with a space
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#Without a comma, it just prints on another line
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%s %r %r %r"

#%r is a reference, brings variable and could be different things.

print formatter % (1, 2, 3, 4) #prints 1 2 3 4
print formatter % ("one", "two", "three", "four") #prints one two three four
print formatter % (True, False, False, True) #prints True False False True
print formatter % (formatter, formatter, formatter, formatter) #prints %r %r %r %r 4 times
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didnt sing.",
    "So I said goodnight."
) #prints I had this thing. That you could type up right. But it didn't sing. So I said goodnight.

#okay so you were wrong, the strings print out with it's quotation marks too because it's a %r not a %s!!!
#also if there is an apostrophe in there, they will make change your quotations to a double quotation.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\n stands for newlines #Separates the months to different lines

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" #separates lines with 3 quotation marks!!!!

print "I am 6'2\" tall." #escape double-quote inside string
print 'I am 6\'2" tall.' #escape single-quote inside strin

tabby_cat = "\tI'm tabbed in." #\t is a tab!!!!
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \ a \ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
     #/ - | \ | in separate lines
     #oops wrong! It doesn't print all of them, it just keeps changing between them.
