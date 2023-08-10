morse_code_library = {'A': '.-', 'Ą': '.-.-', 'B': '-...', 'C': '-.-.', 'Ć': '-.-..',
                      'D': '-..', 'E': '.', 'Ę': '..-..', 'F': '..-.', 'G': '--.',
                      'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                      'Ł': '.-..-', 'M': '--', 'N': '-.', 'Ń': '--.--', 'O': '---',
                      'Ó': '---.', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
                      'Ś': '...-...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..', 'Ź': '--..-.', 'Ż': '--..-',

                      '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                      '8': '---..', '9': '----.',

                      '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                      '!': '-.-.--', '/': '-..-.', '\\': '-..-.', '(': '-.--.',
                      ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
                      '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
                      '"': '.-..-.', '$': '...-..-', '@': '.--.-.',

                      ' ': '/'}

def morse_code_converter():
    text = input("Enter text you want to convert to Morse Code: ")
    try:
        morse_code = [morse_code_library[char] for char in text.upper()]
    except KeyError:
        print("You entered the wrong diacritic character. Please use only Latin and Polish diacritic characters.")
    else:
        print("Your text in mode code:", ' '.join(morse_code))
    finally:
        morse_code_converter()

morse_code_converter()
