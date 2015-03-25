#!/usr/bin/env python2
import sys
import os.path

# Constants
MAX_DEPTH = 5
SPACE_SEP = 3

def error(string):
    print("Error: " + string)
    sys.exit(1)

def fileExists(fname):
    if os.path.isfile(fname):
        ans = raw_input("Clobbering %s (y/n): " % os.path.join(os.getcwd(), fname))

        if ans.find("n") != -1:
            error("not clobbering %s" % fname)

class Section(object):
    name = ""
    depth = -1
    position = 0
    parent = None

    def __init__(self, name, depth, position, parent):
        self.name = name         # what's our name?
        self.depth = depth       # what depth are we?
        self.parent = parent     # who is the parent section
        self.position = position # where are we within the parent section

    def __str__(self):
        return "%s [d%d, p%d]" % (self.name, self.depth, self.position)

    def toLatex(self):
        output = ""

        if self.depth >= 3 and self.depth <= 4:
            self.depth -= 3

            for i in range(self.depth):
                output += "sub"

            output = "\\" + output + "paragraph{" + self.name + "}"
        elif self.depth >= 0:
            for i in range(self.depth):
                output += "sub"

            output = "\\" + output + "section{" + self.name + "}"
        else:
            error("section %s - bad depth" % self.name)

        return output

    def getComment(self):
        output = "% Section "
        nextSection = self

        pos = []
        times = 0
        while nextSection:
            pos.append(nextSection.position)
            nextSection = nextSection.parent
            times += 1

            if times > MAX_DEPTH:
                error("bad parent tree detected")

        # reverse the list
        pos = pos[::-1]

        # Make a nice comment to help find where we are in the doc
        for p in enumerate(pos):
            output += str(p[1])

            if p[0]+1 != len(pos):
                output += "."

        return output

    def abbr(self, maxLen):
        """
        Rules:
            No vowels unless there is space
            Prefer beginning and ending characters of words
            Try to get every word, if possible
        """

        vowels = "aeiou"

        words = self.name.split(" ")
        abbr = ""

        for w in words:
            # everything lower except first char
            w = w.translate(None, vowels)
            w = w.lower()
            w = w[0].upper() + w[1:]
            wl = len(w)

            self.abbr += w

        return abbr

nameMap = { 1 : "summary",
            2 : "desc",
            3 : "constraints",
            4 : "system",
            5 : "hwsw",
            6 : "pcb",
            7 : "proto",
            8 : "mfg",
            9 : "test",
            10 : "demo",
            11 : "manage",
            12 : "appendix"
        };

def makeSectionFile(name, parent, subsections):
    fp = None
    filename = name + ".tex"
    try:
        fileExists(filename)
        fp = open(filename, "w")
    except IOError:
        error("Failed to open %s for writing section file" % name)

    fp.write(parent.getComment() + " in file " + filename + "\n\n")

    for s in subsections:
        fp.write(s.getComment())
        fp.write("\n")
        fp.write(s.toLatex())
        fp.write("\n\n")

    fp.close()

def main(argv):
    tocName = ""
    lipsum = False

    if len(argv) < 2:
        tocName = "TableofContents.txt"
    else:
        tocName = argv[1]

    if len(argv) < 3:
        lipsum = False
    else:
        lipsum = True

    try:
        toc = open(tocName, "r").read()
    except IOError as e:
        error("Failed to open ToC '%s'!" % tocName)

    sections = []
    parent = None
    lastSection = None
    lastDepth = -1
    posCounter = 0

    parentStack = []
    posStack = []

    for line in enumerate(toc.split("\n")):
        if line[1] == "":
            continue

        # skip the leading number
        numDelimPos = line[1].find(".")
        name = line[1][(numDelimPos+2):].strip()
        leadingSpaces = line[1].rfind(" ", 0, numDelimPos) + 1

        depth = leadingSpaces/SPACE_SEP

        if depth > MAX_DEPTH:
            error("ToC exceeded max depth on line %d: %s" % (line[0], line[1]))

        ###############

        if depth > lastDepth: # we are decending
            parentStack.append(lastSection)
            parent = lastSection

            #print "VVVVVV Parent " + str(parent)

            posStack.append(posCounter)
            posCounter = 1
        elif depth < lastDepth: # we are acending
            for i in range(lastDepth-depth):
                parentStack.pop()
                posCounter = posStack.pop()

            parent = parentStack[len(parentStack)-1]
            #print "^^^^^^ Parent " + str(parent)


        lastSection = Section(name, depth, posCounter, parent)
        sections.append(lastSection)

        posCounter += 1
        lastDepth = depth

        #print " "*depth + lastSection.getComment()
        #print " "*depth + lastSection.toLatex()
        #if lipsum:
        #    print(" "*depth + "\lipsum[1]")


    topLevel = []
    subchildren = []
    workingList = []
    count = 0

    for s in sections:
        if not s.parent:
            topLevel.append(s)

            if count > 0:
                subchildren.append(workingList)
            #print "%d : %s" %(count, str(workingList))
            #print [str(s) for s in workingList]
            workingList = []
        else:
            workingList.append(s)

        count += 1

    subchildren.append(workingList)

    fileExists("toc.tex")
    tocTop = open("toc.tex", "w")
    tocTop.write("% WHCS Top-level TOC\n\n")

    # make all of the subsections
    for s in topLevel:
        name = nameMap[s.position]
        tocTop.write(s.getComment() + "\n")
        tocTop.write(s.toLatex() + "\n")
        tocTop.write("\import{./}{%s.tex}\n\n" % name)
        makeSectionFile(name , s, subchildren[s.position-1])
    
    tocTop.close()

    #print [str(s) for s in sections]


if __name__ == "__main__":
    main(sys.argv)
