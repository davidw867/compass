#!/usr/bin/env python3

import os

def clear():
    os.system("clear")

def pause():
    input("\nPress Enter to continue...")

def main():
    while True:
        clear()

        print("=" * 45)
        print("     Compass One Developer Console")
        print("=" * 45)

        print("\nRepository Status")
        print("-----------------")
        print("GitHub: Connected")
        print("SSH: Connected")

        print("\nMenu")
        print("----")
        print("1. Git Status")
        print("2. Git Pull")
        print("3. Git Commit")
        print("4. Git Push")
        print("5. Quick Commit and Push")
        print("6. Exit")

        choice = input("\nSelect: ")

        if choice == "1":
            os.system("git status")
            pause()

        elif choice == "2":
            os.system("git pull")
            pause()

        elif choice == "3":
            message = input("Commit message: ")

            os.system("git add .")
            os.system(f'git commit -m "{message}"')
            pause()

        elif choice == "4":
            os.system("git push")
            pause()

        elif choice == "5":
            message = input("Commit message: ")

            os.system("git add .")
            os.system(f'git commit -m "{message}"')
            os.system("git push")
            pause()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
            pause()

if __name__ == "__main__":
    main()
