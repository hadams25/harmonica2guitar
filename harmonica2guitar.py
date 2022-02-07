import sys
import re

inFile = sys.argv[1]
outFile = sys.argv[2]

#key of c
key = {
    "1" : [5,-2],
    "-1" : [5,-1],
    "2" : [5,0],
    "-2" : [5,3],
    "3" : [5,3],
    "-3" : [4,2],
    "4" : [4,3],
    "-4" : [3,0],
    "5" : [3,2],
    "-5" : [3,3],
    "6" : [2,0],
    "-6" : [2,2],
    "-7" : [1,0],
    "7" : [1,1],
    "-8" : [1,3],
    "8" : [0,0],
    "-9" : [0,1],
    "9" : [0,3],
    "-10" : [0,5],
    "10" : [0,8]
}

#Bb
# key = {
#     "1" : [5," "],
#     "-1" : [5," "],
#     "2" : [5," "],
#     "-2" : [5,1],
#     "3" : [5,1],
#     "-3" : [4,0],
#     "4" : [4,1],
#     "-4" : [4,3],
#     "5" : [3,0],
#     "-5" : [3,1],
#     "6" : [3,3],
#     "-6" : [2,0],
#     "-7" : [2,2],
#     "7" : [2,3],
#     "-8" : [1,1],
#     "8" : [1,3],
#     "-9" : [1,4],
#     "9" : [0,1],
#     "-10" : [0,3],
#     "10" : [0,6]
# }

class tab_staff:
    def __init__(self, notes, lyrics):
        self.notes = notes
        self.lyrics = lyrics
        self.indices = []
        self.tab = ["e -", "B -", "G -", "D -", "A -", "E -"]

        self.staff = ["   " + notes, "   " + lyrics]

        self.process_note_indices()
        self.generate_tab()

        for x in self.tab:
            self.staff.append(x)



    def add(self, note):
        pos = key.get(note)
        if(pos == None): return
        for string in range(len(self.tab)):
            if (string == pos[0]):
                self.tab[string] += str(pos[1])
            else:
                self.tab[string] += ("-")

    def add_blank(self):
        for string in range(len(self.tab)):
            self.tab[string] += ("-")

    def process_note_indices(self):
        self.indices = []
        for i in range(len(self.notes)):
            if self.notes[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.indices.append(i)

    def generate_tab(self):
        separated_notes = re.findall("((-)?[1-9](0)?)",self.notes)
        for i in range(len(self.notes)):
            if i in self.indices:
                self.add(separated_notes[self.indices.index(i)][0])
            else:
                self.add_blank()

input_tab = []

try:
    with open(inFile, 'r') as file:
        for line in file:
            if(line != "\n"):
                input_tab.append(line)


except:
    print("error opening file: " + str(inFile))



with open(outFile, 'w') as file:
    for i in range(0, len(input_tab), 2):
        tab = tab_staff(input_tab[i], input_tab[i+1])
        file.write(tab.staff[0])
        file.write(tab.staff[1])
        if tab.staff[1][-1] != "\n": file.write("\n")
        for x in tab.staff[2:]:
            file.write(x + "\n")
        file.write("\n")

