import os

#############################################################################
# Given a path to a list of files, Filter Test will search each file and
# write the line number and character number of any character that has
# an ascii value above 127 to the console.
#############################################################################
def filterText(path):
    # Looping through all files for entered path
    for filename in os.listdir(path):
        print("File: ", filename, end="")

        # Opening current filename
        file = open(path + "\\" + filename)

        # Keeping track of errors per file for output
        errorFound = False

        # Keeping track of current line for non ascii        
        currLine = 1

        try:
            # Iterating over every line in file
            for line in file:
                currChar = 1
                # Iterating over every character in that line
                for char in line:
                    if ord(char) > 127:
                        # Formatting for pretty output
                        if not errorFound:
                            print()
                            
                        print("\tLine:", currLine, ", Char No.:", currChar, "->", char)
                        errorFound = True

                    currChar += 1

                currLine += 1

            if errorFound:
                errorFound = False
            else:
                print("-> Clean")
        
        # Common error. Seems to be a few undefined characters in these files
        except UnicodeDecodeError:
            # Formatting for pretty output
            if not errorFound:
                print()
            print("\tLine:", currLine, ", Char No.:", currChar, "->", "UNDEFINED CHAR")

        except:
            # Formatting for pretty output
            if not errorFound:
                print()
            print("Unknown error")

        # Closing once fininshed reading
        file.close()

def main():
    path = input("Enter Path to Files: ") 
    filterText(path)
    
if __name__ == "__main__":
    main()