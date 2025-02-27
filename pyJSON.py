# Import class library Json. Json file is used to transfer data as packs.
import json
#Create data structure dictionary
#Creat a json dictionary
#Key and Value pairs in the dictionary. Name, age, city, interests are key.
#There are 4 empty spaces as an indentation in front of the code.
data1 = {
    'name' : 'Gazi Kutbay',
    'age'  :43,
    'City' : 'Seattle, WA',
    'interests':['Traveling','Soccer','Basketball','Running','Videogames','History'], #string array
    'is_student':True
}

#When we dumped the data, the dictionary above becomes a json file.
#First argument is dictionary, and then json file, 
#interpretation is get the data from dictionary,and going to make new json file, and write it to json, set entire indentation to 4.
#open data1 object and write to json file, indentation is 4 in the data.
with open('data1.json','w') as json_file:
    json.dump(data1,json_file,indent=4)
#for makesure all codes are executed, we use print statement.
print ("You have successfully written to data1.json")

