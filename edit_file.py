with open ('files/file_4.csv','r') as file: # firstly we read this file since we wanna grab the content
    content=file.read()
modified_content=content[:-1]
# now we either overwrite the content or create a new file 
with open ('files/file_4_mod.csv','w') as file:
    file.write(modified_content)