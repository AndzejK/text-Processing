from pathlib import Path
file_dir=Path('files')

for file_path in file_dir.iterdir():
    with open(file_path,'r') as file:
        content=file.read()
        # changing header's name from amount to units
        new_content=content.replace("amount","units")
    with open(file_path,'w') as file:
        file.write(new_content)