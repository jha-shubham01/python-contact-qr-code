import qrcode

# Define the contact information for the vCard
first_name = "John"
last_name = "Doe"
email = "johndoe@email.com"
phone_number = "555-1234"

# Create the vCard string
vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name}\nEMAIL;TYPE=INTERNET:{email}\nTEL;TYPE=CELL:{phone_number}\nEND:VCARD"

# Generate the QR code
img = qrcode.make(vcard)

# Save the QR code image
img.save("contact_qr_code.png")
