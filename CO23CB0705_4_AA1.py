student_data = {
    'name': 'Conji', 
    'details': {
        'age': 25, 
        'city': 'New York'
    }
}

# Updating the nested dictionary with new values
student_data['details']['age'] = 13
student_data['details']['city'] = 'New town, Avora'
student_data['details']['occupation'] = 'Wizard Student'

# Printing the updated nested dictionary
print(student_data)
