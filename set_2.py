'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if letter == " ":
        return " "
    else:
        # Calculate the new position in the alphabet
        new_position = (ord(letter) - ord('A') + shift) % 26
        # Convert back to a letter
        return chr(ord('A') + new_position)

def caesar_cipher(message, shift):
    '''Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    encrypted_message = ""    
    for char in message:
        if char == " ":  # Keep spaces unchanged
            encrypted_message += " "
        else:
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_message += shifted_char    
    return encrypted_message

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if letter == " ":  # Keep spaces unchanged
        return " "    
    shift_value = ord(letter_shift) - ord('A')  # Convert shift letter to numerical value
    shifted_char = chr(((ord(letter) - ord('A') + shift_value) % 26) + ord('A'))    
    return shifted_char

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    encrypted_text = '' # Repeat the key to match the length of the plaintext.   
    key_repeated = (key * (len(message) // len(key))) + key[:len(message) % len(key)]   
    for i in range(len(message)): # Iterate through each character in the plaintext.       
       if message[i].isalpha(): # Check if the character is an alphabet letter.           
           shift = ord(key_repeated[i].upper()) - ord('A') # Calculate the shift based on the corresponding key letter.           
           if message[i].isupper(): # Encrypt uppercase and lowercase letters separately.
               encrypted_text += chr((ord(message[i]) + shift - ord('A')) % 26 + ord('A'))
           else:
               encrypted_text += chr((ord(message[i]) + shift - ord('a')) % 26 + ord('a'))
       else:           
           encrypted_text += message[i] # If the character is not an alphabet letter, keep it unchanged.   
    return encrypted_text # Return the final encrypted text

def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
      
    # Ensure message length is a multiple of shift
    # Add underscores if necessary
    if len(message) % shift != 0:
        padding = shift - (len(message) % shift)
        message += '_' * padding
    
    # Construct the encoded message
    encoded = ''
    for i in range(len(message)):
        # Calculate the index in the original message
        original_index = (i // shift) + (len(message) // shift) * (i % shift)
        encoded += message[original_index]
    
    # Return the encoded message
    return encoded

def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Calculate the number of columns (num_cols)
    num_cols = len(message) // shift
    if len(message) % shift != 0:
        num_cols += 1
    
    # Create a 2D grid to represent the scytale
    grid = [[''] * num_cols for _ in range(shift)]
    
    # Fill the grid column by column
    idx = 0
    for col in range(num_cols):
        for row in range(shift):
            if idx < len(message):
                grid[row][col] = message[idx]
                idx += 1
    
    # Read the message row by row
    deciphered = ''
    for row in range(shift):
        for col in range(num_cols):
            if grid[row][col]:  # Only add non-empty cells
                deciphered += grid[row][col]
    
    return deciphered