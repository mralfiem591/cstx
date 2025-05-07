import base64
import os
from cryptography.fernet import Fernet, InvalidToken

# Generate a key for encryption (you can save this key for reuse)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encode_python_to_custom(input_file, output_file):
    """Encodes Python code into a custom encrypted format, preserving line structure."""
    with open(input_file, 'r') as f:
        python_code = f.readlines()  # Read lines to preserve structure
    
    # Encrypt each line
    encrypted_lines = [
        cipher.encrypt(line.encode('utf-8')).decode('utf-8') for line in python_code
    ]
    
    # Save the key and encrypted lines to the custom file
    with open(output_file, 'w') as f:
        f.write("# Custom encrypted Python code in `.cstx`\n")
        f.write(f"KEY = {KEY.decode('utf-8')}\n")  # Write the key as base64
        f.write('\n'.join(encrypted_lines))  # Write the encrypted lines

def decode_and_execute_custom(input_file):
    """Decodes the custom encrypted format and directly executes the Python code."""
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()  # Read all lines
        
        # Extract the key from the first line
        if not lines[1].startswith("KEY = "):
            raise ValueError("Invalid file format: Missing encryption key.")
        
        key = lines[1].split("KEY = ")[1].strip()
        cipher = Fernet(key.encode('utf-8'))  # Create a cipher with the extracted key
        
        # Decrypt the remaining lines
        encrypted_lines = lines[2:]  # Skip the first 2 lines (comment + key)
        decrypted_lines = [
            cipher.decrypt(line.strip().encode('utf-8')).decode('utf-8') for line in encrypted_lines
        ]
        
        # Join the decrypted lines into the original Python code
        python_code = ''.join(decrypted_lines)
        
        # Execute the decoded Python code in the global namespace
        exec(python_code, globals())
    except (FileNotFoundError, ValueError, InvalidToken) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    prompt = input("Encode or decode? (e/d): ").lower()
    if prompt == 'e':
        # Encode Python code into a custom encrypted format
        encode_python_to_custom(
            input("Enter the path of the Python file to encode: "),
            os.path.join(os.path.dirname(__file__), input("Enter the file name to save as (Without extension): ") + '.cstx')
        )
    elif prompt == 'd':
        # Decode the custom encrypted format and directly execute the Python code
        decode_and_execute_custom(os.path.join(os.path.dirname(__file__), input("Enter the name of the custom file to decode: ")))
    else:
        print("Invalid option. Please enter 'e' to encode or 'd' to decode.")