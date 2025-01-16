def encrypting_txt(text, n, m):
    """
    Encrypting the text as per given requirements
    """
    encrypted_text = "" #stores the encrypted text in an empty string
    
    for char in text:
        # Handle lowercase letters
        if char.islower():
            position = ord(char) - ord('a') # Converts the letters into their unicode values 
            if position < 13:  # First half (a-m)
                #applying the sets of rules and keeps it within the first half 
                new_position = ((position + (n * m)) % 13)
                encrypted_text += chr(new_position + ord('a')) # adds it to the empty variable string 
            else:  # Second half (n-z)
                # apply the seconds sets of rule to the second half of the alpahabet 
                new_position = ((position - (n + m)) % 13 + 13) # Keep within second half
                encrypted_text += chr(new_position + ord('a'))
            
        # Handle uppercase letters
        elif char.isupper():
            position = ord(char) - ord('A')
            if position < 13:  # First half (A-M)
                new_position = ((position - n) % 13) # Keep within first half
                encrypted_text += chr(new_position + ord('A'))
            else:  # Second half (N-Z)
                new_position = ((position + (m * m)) % 13 + 13) # Keep within second half
                encrypted_text += chr(new_position + ord('A'))
            
        # Special characters and numbers stays the same 
        else:
            encrypted_text += char
            
    return encrypted_text

def decrypting_txt(encrypted_text, n, m):
    """
    Decryptes the encrypted text using the same sets of rules, but reversed. 
    """
    decrypted_text = ""
    
    for char in encrypted_text:
        # Handle lowercase letters
        if char.islower():
            position= ord(char) - ord('a')
            if position < 13:  
                new_position = ((position - (n * m)) % 13) # subracting or shifting backwards, rather than forward 
                decrypted_text += chr(new_position + ord('a'))
            else: # handles second half of the alphabet
                new_position = ((position - 13 + (n + m)) % 13 + 13)
                decrypted_text += chr(new_position + ord('a'))
            
        # Handle uppercase letters
        elif char.isupper():
            position = ord(char) - ord('A')
            if position < 13:  # Was encrypted using first half rule
                new_position = ((position + n) % 13)
                decrypted_text += chr(new_position + ord('A'))
            else:  # Was encrypted using second half rule
                new_position = ((position - 13 - (m * m)) % 13 + 13)
                decrypted_text += chr(new_position + ord('A'))
            
        # Keep special characters and numbers unchanged
        else:
            decrypted_text += char
            
    return decrypted_text

def main(): 
    while True:  
        try:
            # Get user input for n and m
            n = int(input("Enter the value for n: "))
            m = int(input("Enter the value for m: "))
            
            # Read from input file
            with open("raw_text.txt", 'r') as file:
                original_text = file.read()
            
            # Encrypt the text
            encrypted_text = encrypting_txt(original_text, n, m)  # Changed function name
            
            # Write encrypted text to file
            with open("encrypted_text.txt", 'w') as file:
                file.write(encrypted_text)
                
            # Decrypt the text and save it
            decrypted_text = decrypting_txt(encrypted_text, n, m)
            with open("decrypted_text.txt", 'w') as file:
                file.write(decrypted_text)
            
            # Verify the decrypted text with the original text 
            if original_text == decrypted_text:
                print("\nEncryption and decryption completed successfully!")
                print("Original text matches decrypted text.")
            else:
                print("\nWarning: Decrypted text doesn't match original text!")
                
            program = input("Would you like to encrypt the text again? (yes/no): ").lower()
            if program != "yes" and program  != "y":
                print("Thank you for using this encrytpion program!")
                break
        
        except FileNotFoundError:
            print("Error: raw_text.txt not found!")
        except ValueError:
            print("Error: Please enter valid numbers for n and m!")
        
if __name__ == "__main__":
    main()