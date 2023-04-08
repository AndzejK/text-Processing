from pathlib import Path
import re
file_dir=Path('files')

merged_cont=''
# they how we can extract index in the list
for index,file_path in enumerate(file_dir.iterdir()):
    if re.search(r'.*\.csv', str(file_path)) and len(str(file_path)) > 16:
        with open(file_path,'r') as file:
            content=file.readlines() # we get a list of lines
            new_content=content[1:] # we skip for each file first line!
        if index==0:
            # since content is a list we need to convert into a str
            content=''.join(content)
            merged_cont=merged_cont+content+'\n'
        else:
            new_content=''.join(new_content)
            merged_cont=merged_cont+new_content+'\n'
# Since content is stored in merged_cont I need to write it to a new file
with open('files/concatenated_file.csv','w') as file:
    file.write(merged_cont)
            