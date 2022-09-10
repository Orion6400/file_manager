import os
import pathlib
import shutil

fileFormat = {
    "web": [".html5", ".html", ".htm", ".xhtml"],
    "Pictures": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "Videos": [".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg",
               ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt",
                  ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd",
                  ".xls", ".xlsx", ".ppt", ".pptx"],
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Audios": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav",
               ".wma"],
    "Database": [".sql"]
}

fileType = list(fileFormat.keys())
fileFormats = list(fileFormat.values())
source_folder = "C:\\Users\\dev64\\Downloads"
for files in os.scandir(source_folder):
    filename = pathlib.Path(files)
    fileformatetype = filename.suffix.lower()

    src = str(filename)
    dest = "C://Users//dev64//file_manager//others"
    dest_path = "C://Users//dev64//file_manager//"
    if fileformatetype == "":
        print(src,"has not file formate")
    else:
        for formats in fileFormats:
            if fileformatetype in formats:
                folder = fileType[fileFormats.index(formats)]
                print(folder)
                if os.path.isdir(dest_path+folder)==False:
                    os.mkdir(dest_path+str(folder))
                dest = dest_path+str(folder)
            else:
                if os.path.isdir(dest) == False:
                    os.mkdir(dest)

    print(src,"move to",dest)
    shutil.move(src,dest)

print("Script executed")



