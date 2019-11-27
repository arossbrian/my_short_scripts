from ipaddress import IPv4Address #For the IP Adress
from pyairmore.request import AirmoreSession # to create an airmore session
from pyairmore.services.messaging import MessagingService # This one sends messages

from openpyxl import load_workbook

phone_IP_address = "192.168.8.102"
# Let us create an IP address object

ip = IPv4Address(phone_IP_address)

# Now create a session
session = AirmoreSession(ip)

# we create a session at the top and we need to ensure
# that Airmore is running
session.is_server_running # True if Airmore is running

# Now we need to request authorization

was_accepted = session.request_authorization()

# Print true if it was accepted
print("Is requestes accepted???", was_accepted)

# Now thar we have done the follwing in the above code
# 1. Created a session
# 2. Made sure it is connected And
# 2. Authorized it

# We need to create a service called "MessagingService"

service = MessagingService(session)

# We use this service to send an sms like below
# service.send_message("254722 381301", "Testing Message from my computer as a test to Bulk SMS ")


# We are about to handle the worksheet that contains the contact details

# Path to file 
filepath = "/home/piper/Documents/shortpythonscripts/bulk_sms_with_pyairmore/kandaria_contacts.xlsx"

# Column to read
column = "A" # Beacuse my contacts are under column B

# Number of columns to get
lenght = 3

# we are importing our file
workbook = load_workbook(filename=filepath, read_only=True)
worksheet = workbook.active # We will get the active worksheet

# reading the phone numbers
phone_numbers1 = []
for i in range(lenght):
    cell = "{}{}".format(column, i+1)
    number = worksheet[cell].value

    if number!="" or number is not None:
        phone_numbers1.append(str(number))

print(phone_numbers1)

        
message = "This is a trial message to your phone numbers from Brian for meds offers"
for number in phone_numbers1:
    service.send_message(number, message)

