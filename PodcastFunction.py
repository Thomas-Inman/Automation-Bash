# Import operating packages
import os
import sys


# Create Variables
extensions = {
    "Script" : ".txt",
    "RawRecording" : ".m4a",
    "Final" : ".mp3"
}
path = os.getcwd()
projectName = str(sys.argv[1])
fileName = ""


# Create functions
def createScript():
    os.chdir("/Users/thomasinman/Podcast/script")
    fileName = str(projectName + extensions["Script"])
    if not os.path.isfile("./" + fileName):
        open(fileName, "a").close()
    os.system("open " + fileName + ' -a "Sublime Text"')

def createQTP():
    os.chdir("/Users/thomasinman/Podcast/RawRecording")
    fileName = str(projectName + extensions["RawRecording"])
    if not os.path.isfile("./" + fileName):
        open(fileName, "a").close()
    os.system('open -a "QuickTime Player"')

def createFinal():
    os.chdir("/Users/thomasinman/Podcast/Final")
    fileName = str(projectName + extensions["Final"])
    if not os.path.isfile("./" + fileName):
        open(fileName, "a").close()
    os.system("open " + fileName + ' -a "Audacity"')


# Run functions
createScript()
createQTP()
createFinal()
