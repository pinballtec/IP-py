from ip2geotools.databases.noncommercial import DbIpCity
string = input('Input of IP here: ')
ip = string
response = DbIpCity.get(ip, api_key='free')
print(f'\nCountry: {response.country}')
print(f'Region: {response.region}')
print(f'City: {response.city}')
print(f'Longitude: {response.longitude}')