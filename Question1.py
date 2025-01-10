def encrypting_txt(text, n, m):
    """
    Encrypts the text as per given requirements 
    """
    encrypted_text = ""
    
    for char in text:
        # Handle lowercase letters
        if char.islower():
            pos = ord(char) - ord('a')
            if pos < 13:  # First half (a-m)
                # Add flag bit (0) and then apply transformation
                new_pos = ((pos + (n * m)) % 13) # Keep within first half
                encrypted_text += chr(new_pos + ord('a'))
            else:  # Second half (n-z)
                # Add flag bit (1) and then apply transformation
                new_pos = ((pos - (n + m)) % 13 + 13) # Keep within second half
                encrypted_text += chr(new_pos + ord('a'))
            
        # Handle uppercase letters
        elif char.isupper():
            pos = ord(char) - ord('A')
            if pos < 13:  # First half (A-M)
                new_pos = ((pos - n) % 13) # Keep within first half
                encrypted_text += chr(new_pos + ord('A'))
            else:  # Second half (N-Z)
                new_pos = ((pos + (m * m)) % 13 + 13) # Keep within second half
                encrypted_text += chr(new_pos + ord('A'))
            
        # Keep special characters and numbers unchanged
        else:
            encrypted_text += char
            
    return encrypted_text

def decrypting_txt(encrypted_text, n, m):
    """
    Decryptes the encrypted text 
    """
    decrypted_text = ""
    
    for char in encrypted_text:
        # Handle lowercase letters
        if char.islower():
            pos = ord(char) - ord('a')
            if pos < 13:  # Was encrypted using first half rule
                new_pos = ((pos - (n * m)) % 13)
                decrypted_text += chr(new_pos + ord('a'))
            else:  # Was encrypted using second half rule
                new_pos = ((pos - 13 + (n + m)) % 13 + 13)
                decrypted_text += chr(new_pos + ord('a'))
            
        # Handle uppercase letters
        elif char.isupper():
            pos = ord(char) - ord('A')
            if pos < 13:  # Was encrypted using first half rule
                new_pos = ((pos + n) % 13)
                decrypted_text += chr(new_pos + ord('A'))
            else:  # Was encrypted using second half rule
                new_pos = ((pos - 13 - (m * m)) % 13 + 13)
                decrypted_text += chr(new_pos + ord('A'))
            
        # Keep special characters and numbers unchanged
        else:
            decrypted_text += char
            
    return decrypted_text

def main():
    try:
        # Get user input for n and m
        n = int(input("Enter the value for n: "))
        m = int(input("Enter the value for m: "))
        
        # Read from input file
        with open("raw_text.txt", 'r') as file:
            text = file.read()
        
        # Encrypt the text
        encrypted_text = encrypting_txt(text, n, m)  # Changed function name
        
        # Write encrypted text to file
        with open("encrypted_text.txt", 'w') as file:
            file.write(encrypted_text)
            
        # Decrypt the text and save it
        decrypted_text = decrypting_txt(encrypted_text, n, m)
        with open("decrypted_text.txt", 'w') as file:
            file.write(decrypted_text)
            
        # Verify the decryption
        if text == decrypted_text:
            print("\nEncryption and decryption completed successfully!")
            print("Original text matches decrypted text.")
        else:
            print("\nWarning: Decrypted text doesn't match original text!")
        
    except FileNotFoundError:
        print("Error: raw_text.txt not found!")
    except ValueError:
        print("Error: Please enter valid numbers for n and m!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()