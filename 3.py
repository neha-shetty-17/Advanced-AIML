import secrets, string

letters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(letters) for _ in range(12))
print("Generated Password:", password)
