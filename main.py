#!/usr/bin/env python3
"""
AFRICAN LANGUAGE TRANSLATOR - TEAM PROJECT
Main Program File

TEAM MEMBERS:
1. [Momodu Daniel] - Swahili
2. [John Bright] - Yoruba
3. [Ibrahim Simpa] - Hausa
4. [Team Leader Edoh Godwin] - Zulu
5. [Kamsi] - Igbo

DESCRIPTION:
This program allows users to translate English words to 5 African languages.
Users can select a language, enter English words, and see translations.
"""

# ========== IMPORTS ==========
# Import ALL languages from the package
from languages import LANGUAGES, AVAILABLE_LANGUAGES, igbo_dict


# ========== HELPER FUNCTIONS ==========
def display_welcome():
    """Display welcome message"""
    print("\n" + "=" * 60)
    print("🌍 AFRICAN LANGUAGE TRANSLATOR".center(60))
    print("=" * 60)
    print("\nWelcome! Translate English words to African languages.")
    print(f"Available languages: {len(AVAILABLE_LANGUAGES)}")


def display_language_menu():
    """Display available languages with numbers"""
    print("\n📚 SELECT A LANGUAGE:")
    print("-" * 50)

    # Show all available languages
    for i, language in enumerate(AVAILABLE_LANGUAGES, 1):
        if language in LANGUAGES:
            word_count = len(LANGUAGES[language])
            # Show status icon based on word count
            if word_count >= 20:
                status = "✅"
            elif word_count > 0:
                status = "⚠️"
            else:
                status = "❌"

            print(f"{status} {i:2}. {language:10} ({word_count:3} words)")
        else:
            print(f"❌ {i:2}. {language:10} (Not loaded)")

    print(" 0. Exit Program")
    print("-" * 50)


def translate_interface(language_name):
    """Handle translation for a specific language"""
    # Check if language exists and has dictionary
    if language_name not in LANGUAGES or not LANGUAGES[language_name]:
        print(f"\n⚠️ {language_name} dictionary is not available yet.")
        print("   Please wait for team member to complete it.")
        return "menu"

    dictionary = LANGUAGES[language_name]

    print(f"\n{'=' * 50}")
    print(f"🔤 TRANSLATING TO: {language_name}")
    print(f"📊 Dictionary has {len(dictionary)} words")
    print("=" * 50)

    print("\n💡 Available commands:")
    print("   • Enter any English word to translate")
    print("   • Type 'list' - Show all available words")
    print("   • Type 'menu' - Go back to language selection")
    print("   • Type 'quit' - Exit program")
    print("-" * 40)

    while True:
        try:
            user_input = input("\n📝 English word: ").lower().strip()

            # Handle special commands
            if user_input == 'quit':
                print(f"\n👋 Goodbye! (Ka ọ dị in Igbo)")
                return 'quit'

            elif user_input == 'menu':
                print("\n↩️ Returning to main menu...")
                return 'menu'

            elif user_input == 'list':
                # Show all words in this language
                words = sorted(dictionary.keys())
                print(f"\n📋 All words in {language_name} ({len(words)} total):")

                # Display in columns (4 words per row)
                for i, word in enumerate(words, 1):
                    print(f"{word:15}", end=" ")
                    if i % 4 == 0:
                        print()  # New line every 4 words

                # Add newline if last row wasn't complete
                if len(words) % 4 != 0:
                    print()

            elif user_input in dictionary:
                # Found word - show translation
                translation = dictionary[user_input]
                print(f"\n✅ {user_input} → {translation}")

                # Add fun facts for specific words
                if language_name == "Swahili" and user_input == "hello":
                    print("   💡 'Hujambo' means 'How are you?' in Swahili")
                elif language_name == "Zulu" and user_input == "hello":
                    print("   💡 'Sawubona' means 'I see you' - a respectful greeting")
                elif language_name == "Yoruba" and user_input == "thank you":
                    print("   💡 'O ṣeun' is a common way to say thank you")
                elif language_name == "Hausa" and user_input == "hello":
                    print("   💡 'Sannu' is a common greeting in Hausa")
                elif language_name == "Igbo" and user_input == "hello":
                    print("   💡 'Ndewo' shows respect in Igbo culture")

            else:
                # Word not found
                print(f"\n❌ '{user_input}' not found in {language_name} dictionary")
                print("   💡 Try 'list' to see all available words")

                # Suggest some common words
                common_words = ["hello", "thank you", "water", "mother", "sun"]
                suggestions = [word for word in common_words if word in dictionary]
                if suggestions:
                    print(f"   💡 Or try: {', '.join(suggestions[:3])}")

        except KeyboardInterrupt:
            print("\n\n↩️ Returning to menu...")
            return 'menu'
        except EOFError:
            print("\n\n↩️ Returning to menu...")
            return 'menu'
        except Exception as e:
            print(f"\n⚠️ Error: {e}")
            print("   Please try again")


def show_project_info():
    """Display project information"""
    print("\n" + "=" * 60)
    print("📖 PROJECT INFORMATION")
    print("=" * 60)
    print("\n🌍 African Language Translator")
    print("   A team project to translate English words to African languages")

    print("\n👥 TEAM MEMBERS:")
    print("   1. [Name 1] - Swahili (East Africa)")
    print("   2. [Name 2] - Yoruba (Nigeria/Benin)")
    print("   3. [Name 3] - Hausa (West Africa)")
    print("   4. [Name 4] - Zulu (South Africa)")
    print("   5. [Name 5] - Igbo (Nigeria)")

    print("\n📚 LANGUAGES INCLUDED:")
    total_words = 0
    for lang in AVAILABLE_LANGUAGES:
        if lang in LANGUAGES:
            word_count = len(LANGUAGES[lang])
            total_words += word_count
            print(f"   • {lang:10} - {word_count:3} words")

    print(f"\n📊 TOTAL: {total_words} words across {len(AVAILABLE_LANGUAGES)} languages")
    print("\nPress Enter to continue...", end="")
    input()


def main():
    """Main program loop"""
    print("Loading African Language Translator...")

    # Check if we have languages loaded
    if not AVAILABLE_LANGUAGES:
        print("\n❌ No languages available!")
        print("   Please check that languages/__init__.py is set up correctly.")
        return

    # Main program loop
    while True:
        try:
            # Display welcome and menu
            display_welcome()
            display_language_menu()

            # Get user choice
            choice = input(f"\n🎯 Select option (1-{len(AVAILABLE_LANGUAGES)} or 0): ").strip()

            # Handle exit
            if choice == '0':
                print("\n👋 Goodbye! Thank you for using our translator!")
                print("   Kwaheri! (Swahili)")
                print("   O dabọ! (Yoruba)")
                print("   Sai anjima! (Hausa)")
                print("   Hamba kahle! (Zulu)")
                print("   Ka ọ dị! (Igbo)")
                break

            # Handle project info command
            if choice.lower() == 'info':
                show_project_info()
                continue

            # Convert to number and validate
            try:
                choice_num = int(choice)
            except ValueError:
                print("❌ Please enter a number")
                continue

            if 1 <= choice_num <= len(AVAILABLE_LANGUAGES):
                selected_language = AVAILABLE_LANGUAGES[choice_num - 1]

                # Enter translation interface
                result = translate_interface(selected_language)

                if result == 'quit':
                    print("\n👋 Thank you for using African Language Translator!")
                    break
                # If 'menu', loop continues

            else:
                print(f"❌ Please enter a number between 1 and {len(AVAILABLE_LANGUAGES)}, or 0 to exit.")

        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n⚠️ An unexpected error occurred: {e}")
            print("   The program will continue...")


# ========== RUN THE PROGRAM ==========
if __name__ == "__main__":
    main()



