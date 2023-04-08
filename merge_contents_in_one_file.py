from pathlib import Path
file_dir=Path('files')

merged_cont=''
for file_path in file_dir.iterdir():
    with open(file_path,'r') as file:
        content=file.read()
    merged_cont=merged_cont+content+'\n'

with open('files/allmergedcontent.csv','w') as file:
    file.write(merged_cont)
