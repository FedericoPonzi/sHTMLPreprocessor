import os.path
def getFooter():
	with open('html/footer.html') as footer:
		return footer.readlines()
def getHeaders():
	with open('html/header.html') as header:
		return header.readlines()

filesToCompile = os.listdir("html")
for f in os.listdir("html"):
	if f == "footer.html" or f == "header.html":
		continue
	with open("html" + os.sep + f, "r") as file:
		with open("compiled" + os.sep + f, "w") as compiled:
			toWrite= getHeaders() + file.readlines() + getFooter()
			print toWrite
			compiled.writelines(toWrite)


