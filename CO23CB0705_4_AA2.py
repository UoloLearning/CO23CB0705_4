# Create a phone book using a nested dictionary
phone_book = {
    'friend1': {
        'name': 'Eva',
        'phone': '1234567890',
        'email': 'eva@avoramail.com'
    },
    'friend2': {
        'name': 'Mel',
        'phone': '9876543210',
        'email': 'mel@avoramail.com'
    },
    'friend3': {
        'name': 'Elder Robot',
        'phone': '5555555555',
        'email': 'elderrobot@avoramail.com'
    }
}

# Display the details of each friend
for friend, details in phone_book.items():
    print(f"Friend: {friend}")
    print(f"Name: {details['name']}")
    print(f"Phone: {details['phone']}")
    print(f"Email: {details['email']}")
    print()
