"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir():
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_seperate_words(filename)
        print("Renaming {} to {}".format(filename, new_name))

        os.rename(filename, new_name)


def get_seperate_words(filename):
    new_name = ""
    for current_index, current_letter in enumerate(filename):
        new_name = new_name + current_letter
        if current_index < len(filename) - 1:
            next_character = filename[current_index + 1]
            if current_letter.isalnum() and (next_character.isupper() or next_character.isdigit()):
                new_name += "_"
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('.')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))



main()
# demo_walk()
