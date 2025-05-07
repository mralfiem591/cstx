# Custom Python Encryption and Execution Tool

This script allows you to encode Python files into a custom encrypted format (`.cstx`) and decode them back for execution. It uses AES encryption (via the `cryptography` library) to securely encrypt Python code while preserving its line structure.

## Features

- **Encoding**: Converts Python code into an encrypted `.cstx` file.
- **Decoding and Execution**: Decodes the `.cstx` file and directly executes the Python code.
- **Key Embedding**: The encryption key is embedded in the `.cstx` file for self-contained usage.
- **Line Preservation**: Maintains the original line structure of the Python code.

## File Format

The `.cstx` file is structured as follows:

1. A comment indicating the file type.
2. The encryption key in base64 format.
3. The encrypted Python code, line by line.

Example:

```plaintext
# Custom encrypted Python code in `.cstx`
KEY = gAAAAABk...
gAAAAABk... (encrypted line 1)
gAAAAABk... (encrypted line 2)
```

## Requirements

- Python 3.6 or higher
- `cryptography` library (`pip install cryptography`)

## Usage

1. **Run the Script**:

    ```bash
    python cstx.py
    ```

2. **Choose an Option**:
   - Enter `e` to encode a Python file.
   - Enter `d` to decode and execute a `.cstx` file.

3. **Encoding**:
   - Provide the path to the Python file you want to encode.
   - Specify the name of the `.cstx` file to save.

4. **Decoding**:
   - Provide the name of the `.cstx` file to decode and execute.

## Example Workflow

### Encoding

1. Run the script and choose `e` for encoding.
2. Input the path to the Python file you want to encode.
3. Specify the name of the `.cstx` file to save.

### Decoding

1. Run the script and choose `d` for decoding.
2. Input the name of the `.cstx` file to decode.
3. The decoded Python code will be executed directly.

## Notes

- The encryption key is embedded in the `.cstx` file, so no external key management is required.
- Ensure the `.cstx` file is not modified, as this may corrupt the encryption and prevent decoding.
- Use caution when executing decoded code, as it may contain arbitrary Python code.
