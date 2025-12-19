
import datetime as dt
from all_modules import login, create_post, all_posts, search_posts_by_username


def main():
    user = login()

    if user is None:
        return

    while True:
        print("\n===================User Menu======================== ")
        print("(1) Create Post")
        print("(2) View All Posts")
        print("(3) Search Posts by Username")
        print("(4) Exit")

        choice = input("Enter your choice = ")

        if choice == "1":
            create_post(user)
        elif choice == "2":
            all_posts()
        elif choice == "3":
            search_posts_by_username()
        elif choice == "4":
            print("Goodbye tata see ya")
            break
        else:
            print("Invalid choice")

main()
