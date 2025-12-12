"""
AFRICAN LANGUAGE TRANSLATOR - DICTIONARIES PACKAGE
Team Project with 5 Languages
"""

# ========== IMPORT ALL 5 LANGUAGE DICTIONARIES ==========
try:
    from .swahili import swahili_dict
    print("✅ Swahili dictionary loaded")
except ImportError:
    swahili_dict = {}
    print("⚠️ Swahili dictionary not found - using empty")

try:
    from .yoruba import yoruba_dict
    print("✅ Yoruba dictionary loaded")
except ImportError:
    yoruba_dict = {}
    print("⚠️ Yoruba dictionary not found - using empty")

try:
    from .hausa import hausa_dict
    print("✅ Hausa dictionary loaded")
except ImportError:
    hausa_dict = {}
    print("⚠️ Hausa dictionary not found - using empty")

try:
    from .zulu import zulu_dict
    print("✅ Zulu dictionary loaded")
except ImportError:
    zulu_dict = {}
    print("⚠️ Zulu dictionary not found - using empty")

try:
    from .igbo import igbo_dict
    print("✅ Igbo dictionary loaded")
except ImportError:
    igbo_dict = {}
    print("⚠️ Igbo dictionary not found - using empty")

# ========== MAIN DICTIONARY ==========
LANGUAGES = {
    "Swahili": swahili_dict,
    "Yoruba": yoruba_dict,
    "Hausa": hausa_dict,
    "Zulu": zulu_dict,
    "Igbo": igbo_dict,
}

# ========== HELPER VARIABLES ==========
AVAILABLE_LANGUAGES = list(LANGUAGES.keys())
TOTAL_LANGUAGES = len(LANGUAGES)

# Count total words (skip empty dictionaries)
TOTAL_WORDS = 0
for lang_name, dictionary in LANGUAGES.items():
    if dictionary:  # Only count if not empty
        TOTAL_WORDS += len(dictionary)

# ========== HELPER FUNCTIONS ==========
def get_language_info():
    """Get information about all loaded languages"""
    info = []
    for lang_name, dictionary in LANGUAGES.items():
        word_count = len(dictionary) if dictionary else 0
        status = "✅ Loaded" if dictionary else "❌ Missing"
        info.append({
            'language': lang_name,
            'word_count': word_count,
            'status': status
        })
    return info

def translate_word(english_word, target_language):
    """Translate an English word to target language"""
    english_word = english_word.lower().strip()
    target_language = target_language.title()  # Make first letter capital
    
    if target_language in LANGUAGES:
        dictionary = LANGUAGES[target_language]
        if dictionary and english_word in dictionary:
            return dictionary[english_word]
    return None

def list_words_in_language(language_name):
    """List all words available in a specific language"""
    language_name = language_name.title()
    if language_name in LANGUAGES:
        dictionary = LANGUAGES[language_name]
        if dictionary:
            return sorted(dictionary.keys())
    return []

# ========== STARTUP MESSAGE ==========
print("\n" + "="*50)
print("AFRICAN LANGUAGE TRANSLATOR INITIALIZED")
print("="*50)
print(f"📊 Loaded {TOTAL_LANGUAGES} languages")
print(f"📝 Total words: {TOTAL_WORDS}")
print("="*50 + "\n")

# What gets imported when someone does: from languages import *
__all__ = [
    'LANGUAGES',
    'AVAILABLE_LANGUAGES',
    'TOTAL_LANGUAGES',
    'TOTAL_WORDS',
    'get_language_info',
    'translate_word',
    'list_words_in_language'
]
