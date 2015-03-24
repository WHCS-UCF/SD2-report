#!/usr/bin/env python2
import sys

def section(depth, name):
    output = ""

    if depth >= 3 and depth <= 4:
        depth -= 3

        for i in range(depth):
            output += "sub"

        output = "\\" + output + "paragraph{" + name + "}"
    elif depth >= 0:
        for i in range(depth):
            output += "sub"

        output = "\\" + output + "section{" + name + "}"
    else:
        error("Bad depth")

    return output

def name2abbr(name, maxLen):
    """
    Rules:
        No vowels unless there is space
        Prefer beginning and ending characters of words
        Try to get every word, if possible
    """

    vowels = "aeiou"

    words = name.split(" ")
    abbr = ""

    for w in words:
        # everything lower except first char
        w = w.translate(None, vowels)
        w = w.lower()
        w = w[0].upper() + w[1:]
        wl = len(w)

        abbr += w

    return abbr

def error(string):
    print("Error: " + string)
    sys.exit(1)

toc = open("TableofContents.txt", "r").read()

i = 0
sectionCntr = [0]*5
for l in toc.split("\n"):
    if l == "":
        continue

    depth = 0
    #print("Line %d: %s" %(i, l))

    # skip the leading number
    name = l[(l.find(".")+2):].strip()
    leadingSpaces = l.rfind(" ", 0, l.find(".")) + 1

    depth = leadingSpaces/3

    sectionCntr[depth] += 1

    # reset counter for all sections below
    for c in xrange((depth+1),len(sectionCntr)):
        sectionCntr[c] = 0

    commentOut = "% Section "

    # Make a nice comment to help find where we are in the doc
    for c in xrange(depth+1):
        commentOut += str(sectionCntr[c])

        if c+1 != depth+1:
            commentOut += "."

    sys.stdout.write(" "*depth)
    print(commentOut)

    # print indent
    sys.stdout.write(" "*depth)
    print(section(depth, name))
    print("\lipsum[1]")
    #print(name2abbr(name,8))
