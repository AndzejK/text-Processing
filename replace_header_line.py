with open('files/concatenated_file.csv','r') as file:
    # original content stored in the List()
    content=file.readlines() # readlines!! - LIST
# We channge the header from id,units,price to ID,AMOUNT,COST    
content[0]='ID,AMOUNT,COST\n'
# time to change the content in the FILE /concatenated_file.csv
with open('files/concatenated_file.csv','w') as file:
    file.writelines(content) # writelines!! - LIST


