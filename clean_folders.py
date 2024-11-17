# read file that contains (1), (2), [1], [2]
# delete it
# output how many files has been deleted
import os

path = r"C:\Users\walid nadirul ahnaf\Downloads"
download_list = os.listdir(path)
pattern = ["[1]", '(1)', '(2)', '[2]', '[3]', '(3)', '(4)', '[4]']
counter = 0

for i in download_list:
    for j in pattern:
        if j in i:
            print(os.path.join(path,i))
            counter+=1

if counter == 0: 
    print('the folder is already clean')     
    
else : 
    confirm = input("clear folder? ")
    if confirm == 'yes':

        for i in download_list:
            for j in pattern:
                if j in i:
                    os.remove(os.path.join(path,i))

        print(f"{counter} files has been deleted")


