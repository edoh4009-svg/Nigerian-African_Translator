"""
Zulu Dictionary for African Language Translator
Created by: [Edoh Godwin] - Team Lead
"""

zulu_dict = {
    # ========== GREETINGS & BASICS ==========
    "hello": "sawubona",
    "goodbye": "hamba kahle",
    "thank you": "ngiyabonga",
    "please": "ngicela",
    "yes": "yebo",
    "no": "cha",

    # ========== FAMILY & PEOPLE ==========
    "mother": "umama",
    "father": "ubaba",
    "child": "ingane",
    "friend": "umngane",
    "family": "umndeni",
    "woman": "owesifazane",
    "man": "indoda",

    # ========== COMMON OBJECTS ==========
    "water": "amanzi",
    "food": "ukudla",
    "house": "indlu",
    "book": "incwadi",
    "pen": "ipeni",
    "school": "isikole",
    "car": "imoto",

    # ========== NATURE & ENVIRONMENT ==========
    "sun": "ilanga",
    "moon": "inyanga",
    "tree": "isihlahla",
    "river": "umfula",
    "mountain": "intaba",
    "sky": "isibhakabhaka",
    "earth": "umhlaba",

    # ========== TIME & DAYS ==========
    "day": "usuku",
    "night": "ubusuku",
    "today": "namuhla",
    "tomorrow": "kusasa",
    "yesterday": "izolo",

    # ========== COLORS ==========
    "red": "obomvu",
    "blue": "oluhlaza okwesibhakabhaka",
    "white": "omhlophe",
    "black": "omnyama",

    # ========== ANIMALS ==========
    "dog": "inja",
    "cat": "ikati",
    "bird": "inyoni",
    "lion": "ibhubesi",

    # ========== COMMON PHRASES ==========
    "how are you": "unjani",
    "i am fine": "ngiyaphila",
    "what is your name": "ubani igama lakho",
    "my name is": "igama lami ngingu",
    "i love you": "ngiyakuthanda",

    # ========== NUMBERS (1-5) ==========
    "one": "kunye",
    "two": "kubili",
    "three": "kuthathu",
    "four": "kune",
    "five": "kuhlanu"
}

# Additional information
ZULU_INFO = {
    "language": "isiZulu",
    "native_speakers": "12 million",
    "region": "South Africa, Eswatini, Lesotho",
    "writing_system": "Latin script",
    "language_family": "Bantu, Nguni",
    "hello_meaning": "'Sawubona' means 'I see you'"
}


def get_zulu_info():
    """Return information about Zulu language"""
    return ZULU_INFO


def count_words():
    """Return number of words in dictionary"""
    return len(zulu_dict)


# Print info when file is run directly
if __name__ == "__main__":
    print(f"✅ Zulu Dictionary Loaded")
    print(f"📊 Total words: {len(zulu_dict)}")
    print(f"🌍 Language: {ZULU_INFO['language']}")
    print(f"📍 Region: {ZULU_INFO['region']}")
    print("\nSample translations:")
    samples = list(zulu_dict.items())[:5]
    for eng, zulu in samples:
        print(f"  {eng:15} → {zulu}")
