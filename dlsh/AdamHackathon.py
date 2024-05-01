import random

 # Main function (not necessary but we use it for the code flow)



if __name__ == "__main__":
    with open('cs4222_students_list.csv', 'r') as file:
        next(file)     # skip the first line
        lines = file.readlines()

# Initialise the dictionary
        
    students_dictionary = {}


# Populate the dictionary
    
    for line in lines:
        ID, last_name, first_name = line.strip().split(',')
        students_dictionary[last_name] = {'ID': ID, 'first_name': first_name}


# Sort the array (Last Name) (Insertion Sort)
        
    def insertionSort(arr):
        for i in range(1,len(arr)):
            key=arr[i]
            j=i-1

            while j>=0 and key<arr[j]:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=key
            
    # Get the list of last names and sort it
    last_names = list(students_dictionary.keys())
    insertionSort(last_names)
    print(last_names)

    # Update the dictionary with sorted last names
    sorted_students_dictionary = {}
    for last_name in last_names:
        sorted_students_dictionary[last_name] = students_dictionary[last_name]

    # Print the sorted dictionary
    print(sorted_students_dictionary)
    for last_name, student_info in sorted_students_dictionary.items():
        print(f"Last Name: {last_name}, First Name: {student_info['first_name']}, ID: {student_info['ID']}")

    
   # THE DICTIONARY IS NOW SORTED BY THE LAST NAME
        

    # Open the file for writing
    with open('cs4222_students_list.csv', 'w') as file: # deletes everything just by opening in 'w', so watch out when running the code more than once

    # Iterate over the dictionary
    for ID, info in sorted_students_dictionary.items():
        last_name = info['last_name']
        first_name = info['first_name']
        module_code1 = 'CS4221'
        module_code2 = 'CS4222'
        module_code3 = 'CS4141'
        module_title1 = 'Foundation of Computer Science 1'
        module_title2 = 'Software Development'
        module_title3 = 'Introducton to Programming'

        marks1 = random.randint(0, 100)
        marks2 = random.randint(0, 100) 
        marks3 = random.randint(0, 100) 

        file.write(f"{ID},{last_name},{first_name},{module_code1},{module_title1},{marks1}, {module_code2},{module_title2},{marks2}, {module_code3},{module_title3},{marks3}\n")