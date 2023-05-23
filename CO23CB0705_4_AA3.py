# Create a nested dictionary to store country details
country_details = {
    'USA': {
        'capital': 'Washington, D.C.',
        'currency': 'United States Dollar (USD)'
    },
    'Germany': {
        'capital': 'Berlin',
        'currency': 'Euro (EUR)'
    },
    'Japan': {
        'capital': 'Tokyo',
        'currency': 'Japanese Yen (JPY)'
    },
    'Brazil': {
        'capital': 'Brasília',
        'currency': 'Brazilian Real (BRL)'
    },
    'Australia': {
        'capital': 'Canberra',
        'currency': 'Australian Dollar (AUD)'
    }
}

# Display the details of each country
for country, details in country_details.items():
    print(f"Country: {country}")
    print(f"Capital: {details['capital']}")
    print(f"Currency: {details['currency']}")
    print()
