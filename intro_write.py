"""
git remote add origin git@github.com:AndzejK/text-Processing.git
git branch -M main
git push -u origin main
"""
# 1 way of writing/creating txt file
file = open('files/file_1.txt','w')
file.write('First sentence\n')
file.write('2nd sentence')
file.close()

# 2 way of writing/creating txt file - Multiline string
file1 = open('files/file_2.txt','w')
content="""
Hey, I'm python!
Open 
write
close
"""
file1.write(content)
file1.close() 

# 3 way of writing/creating txt file - with
with open('files/file_3.txt','w') as file:
    file.write('With this method "with" I dont need to have a close method()\ncoz indention does its job, mate!')