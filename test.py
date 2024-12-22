def remove_spaces(text):
    return text.replace(" ", "")

# Exemple d'utilisation
crypted_message = "Th is is a test"
cleaned_message = remove_spaces(crypted_message)
print(cleaned_message)  # Output : "Thisisatest"