#!/usr/bin/env python3
"""
Swahili Language Module
African Languages Assignment
"""

def main():
    print("SWAHILI LANGUAGE BASICS")
    print("=" * 40)
    
    # Swahili vocabulary dictionary
    vocabulary = {
        "Greetings": {
            "Hello": "Jambo",
            "How are you?": "Habari yako?",
            "I'm fine": "Nzuri",
            "Goodbye": "Kwaheri"
        },
        "Common Phrases": {
            "Thank you": "Asante",
            "Please": "Tafadhali",
            "Yes": "Ndiyo",
            "No": "Hapana"
        }
    }
    
    # Display vocabulary
    for category, words in vocabulary.items():
        print(f"\n{category}:")
        for english, swahili in words.items():
            print(f"  {english:<15} → {swahili}")
    
    print(f"\nTotal phrases: {sum(len(words) for words in vocabulary.values())}")

if __name__ == "__main__":
    main()
