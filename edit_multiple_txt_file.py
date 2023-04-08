from pathlib import Path
import re
# getting the path of the directry!
file_dir=Path('files')
# listing through that dir
for file_path in file_dir.iterdir():
    # I want to modify content in files just file_4.csv, file_5.csv and file_4.csv
    if re.search(r'.*\.csv', str(file_path)) and len(str(file_path)) == 16:
        with open(file_path,'r') as file:
            content=file.read()
            new_content=content[:-1]
        # open again a file
        with open('files/'+file_path.stem+"-mod.csv",'w') as file:
            file.write(new_content)

