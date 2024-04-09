from pathlib import Path

file=input("File name: ")

filePath=Path(file)
fileextension=filePath.suffix   #gets extension of the archive

extension={     #Dictionary
    ".gif":"image/gif",
    ".jpg":"image/jpg",
    ".jpeg":"image/jpeg",
    ".png":"image/png",
    ".pdf":"application/pdf",
    ".txt":"text/txt",
    ".zip":"application/zip",
}
#After searching in dictionary mime_type, if a extension is not found, prints application/octet-stream
mime_type = extension.get(fileextension, "application/octet-stream")

print(mime_type)

#This could also be done with if/elif/else, but this way is simplier to code.


