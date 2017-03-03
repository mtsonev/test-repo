### M. Elise Lauterbur
### In progress. Yes you can break it, but if you pet it and treat it nicely it will work for you.
### This program reads a phylip formatted file and creates a file that retains only those nucleotide positions (columns) for which there are at least the critical number of proteins or fewer than the critical number of gaps (dashes).

### Give the file name, what kind of character ("letter" or "dash") you want to look for, your critical number of characters, and the length of the leading identification sequence

import numpy as np
import string
import sys
## read in file, strip first row and first 10 characters of each subsequent row
## put first row and first 10 characters into output file
## strip spaces
## create array
## count letters in each column
## add column to output file if >=3 letters

class Phylip:

        def __init__(self, filename, char = "letter", crit = 3, ident = 10):
                self.file = filename
                self.char = char
                self.crit = crit
                self.ident = ident
                self.species = None # list of species identifiers
                self.seq_array = None # array of sequences only
                self.new_array = None # array of only columns wanted
                self.output_name = "ripped_"+filename #output file name

        def makeArray(self):
                p = open(self.file, 'r') # open phylip file
                header = p.readline() # pull out header
                s = list(p) # make a list of all of the sequences
                sequences = [list(s[x][self.ident:].replace(" ","").strip("\n")) for x in range(len(s))] # turn the list of sequences into list of characters
                        # s[x][self.ident:] gets rid of first "ident" characters
                        # replace() gets rid of spaces
                        # strip("\n") gets rid of newline characters
                self.seq_array = np.array(sequences) # turn it into an array
                self.species = [s[x][:self.ident] for x in range(len(s))] # grab the sequence identifiers
                self.new_array = np.array([[x] for x in self.species]) # create new array
                p.close()
                return self.species, self.seq_array, self.new_array

        def countLetters(self): # move column to file if it has more than the critical number of letters
                for c in range(self.seq_array.shape[1]): # for each column
                        col = self.seq_array[:,c] # pull out the column
                        num_letters = sum(list(col).count(x) for x in string.ascii_letters) # count the number of letters
                        if num_letters >= self.crit: # if the number of letters is greater than the critical number
                                self.new_array = np.insert(self.new_array, self.new_array.shape[1], values = col, axis = 1) # add to new array
                        else:
                                pass
                self.new_array = self.new_array.astype(object) # change the type of the array so you can concatenate the columns
                for i in range(self.new_array.shape[1]-1):
                        self.new_array[:,0] += self.new_array[:,1]
                        self.new_array = np.delete(self.new_array, 1, 1)
                np.savetxt(self.output_name, self.new_array, fmt = "%s")

        def countDashes(self): # move column to file if it has fewer than the critical number of dashes
                for c in range(self.seq_array.shape[1]): # for each column
                        col = list(self.seq_array[:,c]) # pull out the column
                        num_dashes = sum(col.count(x) for x in "-")
                        if num_dashes <= self.crit:
                                self.new_array = np.insert(self.new_array, self.new_array.shape[1], values = col, axis = 1) # add to new array
                        else:
                                pass
                self.new_array = self.new_array.astype(object) # change the type of the array so you can concatenate the columns
                for i in range(self.new_array.shape[1]-1):
                        self.new_array[:,0] += self.new_array[:,1]
                        self.new_array = np.delete(self.new_array, 1, 1)
                np.savetxt(self.output_name, self.new_array, fmt = "%s")


if __name__=="__main__":
        try: filename = sys.argv[1] # check to see if a file name was entered
        except IndexError:
                sys.exit("Usage: phylip_rip.py <filename> <letter/dash> <critical count> <ID string length>") 
        try: 
                char, crit, ident = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]) # check to see if values entered for char and crit and ident
                run = Phylip(filename, char, crit, ident)
        except IndexError:
                run = Phylip(filename)
                print("Insufficient arguments specified, running with default count by letter, critical count of 3, ID string length of 10")
        run.makeArray()
        if run.char == "letter":
                run.countLetters()
        elif run.char == "dash":
                run.countDashes()
        else:
                sys.exit("There was a problem, neither 'letter' nor 'dash' specified")
