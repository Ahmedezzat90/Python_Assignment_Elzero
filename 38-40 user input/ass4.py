email = "Osama@Nn.Sa"
email = email.strip()  # Remove leading and trailing spaces
email = email.lower()  # Convert all characters to lowercase

# Extract name before the @ symbol
name = email.split("@")[0]
name = name.capitalize()  # Capitalize the first letter

# Extract email service provider
service_provider = email.split("@")[1].split(".")[0]

# Extract top level domain
top_level_domain = email.split(".")[-1]

print("Your Name Is", name)
print("Email Service Provider Is", service_provider)
print("Top Level Domain Is", top_level_domain)