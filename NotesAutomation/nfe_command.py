# Import operating packages
import os
import sys


# Create note automator class
class NoteAutamator:
    ruby = ".rb"
    php = ".php"
    javascript = ".js"
    typescript = ".ts"
    python = ".py"
    mapleworksheet = ".mw"
    swift = ".swift"
    java = ".java"
    csharp = ".cs"
    dart = ".dart"
    text = ".txt"
    yaml = ".yaml"
    xml = ".xml"
    html = ".html"
    css = ".css"
    json = ".json"
    org = ".org"
    markdown = ".md"
    R = ".R"

    extensions = {
        "python" : python,
        "py" : python,
        ".py" : python,
        "text" : text,
        "txt" : text,
        ".txt" : text,
        "mapleworksheet" : mapleworksheet,
        "maple" : mapleworksheet,
        "mw" : mapleworksheet,
        ".mw" : mapleworksheet,
        "swift" : swift,
        ".swift" : swift,
        "java" : java,
        ".java" : java,
        "dart" : dart,
        "flutter" : dart,
        ".dart" : dart,
        "yaml" : yaml,
        ".yaml" : yaml,
        "json" : json,
        "jason" : json,
        ".json" : json,
        "org" : org,
        ".org" : org,
        "markdown" : markdown,
        "md" : markdown,
        ".md" : markdown,
        "php" : php,
        ".php" : php,
        "ruby" : ruby,
        "rb" : ruby,
        ".rb" : ruby,
        "javascript" : javascript,
        "js" : javascript,
        ".js" : javascript,
        "ts" : typescript,
        ".ts" : typescript,
        "r" : R,
        ".r" : R,
        "xml" : xml,
        ".xml" : xml,
        "html" : html,
        ".html": html,
        "css" : css,
        ".css" : css
    }

    fileName = ""
    folderName = ""
    extension = ""
    foundFileExtension = ""
    path = os.getcwd()
    print(path)

    def getArguments(self, folderArgNum=2, extArgNum=3):
        try:
            self.fileName = str(sys.argv[1])
        except Exception:
            print("Make sure to name your file and use the correct function command. \n")
            print(".... Terminating process")
            sys.exit()
        try:
            self.folderName = str(sys.argv[folderArgNum])
        except Exception:
            self.folderName = "General"
        try:
            self.extension = str(sys.argv[extArgNum]).lower()
            self.extension = self.extensions[self.extension]
        except Exception:
            self.extension = ".txt"

    def createFolder(self):
        if os.path.isdir(self.path + "/" + self.folderName):
            q = str(input("This folder already exists. Would you like to add the file into the existing folder?")).lower()
            if q == "y" or q == "yes":
                print("Adding file to existing folder.")
            else:
                print(".... Terminating process")
                sys.exit()
        else:
            os.mkdir(self.folderName)

    def createFile(self):
        self.fileName = str(self.fileName + self.extension)
        os.chdir(self.path + "/" + self.folderName)
        if not os.path.isfile("./" + self.fileName):
            open(self.fileName, "a").close()
        os.system("open " + self.fileName + ' -a "Sublime Text"')


# Create note | "nfe" command
note = NoteAutamator()
note.getArguments()
note.createFolder()
note.createFile()
