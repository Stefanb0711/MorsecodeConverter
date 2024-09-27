
morsecode_alphabet = {
    'A': '·-',
    'B': '-···',
    'C': '-·-·',
    'D': '-··',
    'E': '·',
    'F': '··-·',
    'G': '--·',
    'H': '····',
    'I': '··',
    'J': '·---',
    'K': '-·-',
    'L': '·-··',
    'M': '--',
    'N': '-·',
    'O': '---',
    'P': '·--·',
    'Q': '--·-',
    'R': '·-·',
    'S': '···',
    'T': '-',
    'U': '··-',
    'V': '···-',
    'W': '·--',
    'X': '-··-',
    'Y': '-·--',
    'Z': '--··',
    '0': '-----',
    '1': '·----',
    '2': '··---',
    '3': '···--',
    '4': '····-',
    '5': '·····',
    '6': '-····',
    '7': '--···',
    '8': '---··',
    '9': '----·',
    '.': '·-·-·-',
    ',': '--··--',
    '?': '··--··',
    "'": '·----·',
    '!': '-·-·--',
    '/': '-··-·',
    '(': '-·--·',
    ')': '-·--·-',
    '&': '·-···',
    ':': '---···',
    ';': '-·-·-·',
    '=': '-···-',
    '+': '·-·-·',
    '-': '-····-',
    '_': '··--·-',
    '"': '·-··-·',
    '$': '···-··-',
    '@': '·--·-·',
    ' ': '/',
    "Ä": ".- .-",
    "Ö": "--- .",
    "Ü": "..- -"
}



while True:

    morse_text = ""

    benutzer_text = input("Geben sie den zu morsenden Text ein:\n")

    benutzer_text = benutzer_text.upper()

    try:
        for buchstabe in benutzer_text:
            morse_text += morsecode_alphabet[buchstabe]


        print(f"Ihr gemorster Code: {morse_text}")

    except:
        print("Die Buchstaben die Sie morsen wollen sind ungültig. Versuchen Sie es nochmal.")





