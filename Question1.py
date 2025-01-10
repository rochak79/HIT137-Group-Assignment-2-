def encrypting_text(text, n, m):
    """
    Encrypt the entire text using the encryption rules, as per the requirments. 
    """
    encrypted_text = ""
    
    for char in text:
        # Handle lowercase letters
        if char.islower():
            pos = ord(char) - ord('a')
            if pos < 13:  # First half (a-m)
                new_pos = (pos + (n * m)) % 26
            else:  # Second half (n-z)
                new_pos = (pos - (n + m)) % 26
            encrypted_text += chr(new_pos + ord('a'))
            
        # Handle uppercase letters
        elif char.isupper():
            pos = ord(char) - ord('A')
            if pos < 13:  # First half (A-M)
                new_pos = (pos - n) % 26
            else:  # Second half (N-Z)
                new_pos = (pos + (m * m)) % 26
            encrypted_text += chr(new_pos + ord('A'))
            
        # Keep special characters and numbers unchanged
        else:
            encrypted_text += char
            
    return encrypted_text

def main():
    try:
        # Get user input for n and m
        n = int(input("Enter the value for n: "))
        m = int(input("Enter the value for m: "))
        
        # Read from input file
        with open("raw_text.txt", 'r') as file:
            text = file.read()
        
        # Encrypt the text
        encrypting_text = encrypting_text(text, n, m)
        
        # Write to output file
        with open("encrypted_text.txt", 'w') as file:
            file.write(encrypting_text)
            
        print("Encryption completed successfully!")
        
    except FileNotFoundError:
        print("Error: raw_text.txt not found!")
    except ValueError:
        print("Error: Please enter valid numbers for n and m!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()