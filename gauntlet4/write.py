import base64

# Replace 'base64_data' with your actual base64 encoded string
base64_data = './db.txt'

# Decode the base64 data
decoded_data = base64.b64decode(base64_data)

# Write the decoded data to a file
with open('decoded_database.db', 'wb') as file:
    file.write(decoded_data)

