import os.path
import re

#Input: name of the file (complete with .html extension)
#Output: the rows of the file.
def getFile(toGet):
	with open('html' + os.sep + toGet) as fileToGet:
		return fileToGet.readlines()
#Input: the file to compile
#Return the compiled html file.

def getToWrite(toCompile):
    #This is the regex used to find the prep statments
    regex = "<\?prep include \"([a-z]*\.[a-z]*)\" *\?>"
    #String to return:
    toReturn = ""
    #Scan all the lines and try to find the pattern
    for f in toCompile:
        tuples  = re.findall(regex, f)
    
        for el in tuples:
            toReplace=''.join(getFile(el))
            f = re.sub(regex, toReplace, f)
    
        toReturn = toReturn + f    
    return toReturn

#Main:
if __name__ == "__main__":
    for f in os.listdir("html"):
    	with open("html" + os.sep + f, "rU") as file:
    		toWrite = getToWrite(file.readlines())
    		with open("compiled" + os.sep + f, "w") as compiled:
    			compiled.writelines(toWrite)
    print "Done! :)"