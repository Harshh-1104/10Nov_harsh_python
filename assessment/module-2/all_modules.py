import datetime as dt

users = {"harsh":"1234","ved":"5678"}
posts = []
post_count={}

def login():
    print("\n============ LOGIN ==============")
    username = input("Enter username = ")
    passw = input("Enter password = ")

    
    if username in users and users[username] == passw :
        print("Login successful")
        return username
    else:
        print("Invalid username or password")
        return None


def create_post(username):
    print("\n ================== CREATE POST ==================")

    title = input("Enter Title = ")
    desc= input("Enter Description = ")

    date = dt.date.today()

    post = {
        "author": username,
        "title": title,
        "description": desc,
        "date": date
    }

    posts.append(post)
    
    if username in post_count:
        post_count[username] = post_count[username] + 1
    else:
        post_count[username] = 1
        
    print("====================== POST CREATED SUCCESSFULLY ======================")


def all_posts():
    print("\n==================== ALL POSTS ====================")

    if len(posts) == 0:
        print("No posts available")
        return

    for post in posts:
        print("\nAuthor = ", post["author"])
        print("Title = ", post["title"])
        print("Date = ", post["date"])
        print("Description = ", post["description"])
        print("====================================================")



def search_posts_by_username():
    print("\n======================= SEARCH POSTS BY USERNAME ========================")
    name = input("Enter username = ")

    if name not in users:
        print("user does not exist")
        return
    if name not in post_count or post_count[name] == 0:
        print("No posts under this username.")
        return
    for post in posts:
        if post["author"] == name:
            print("\nAuthor = ", post["author"])
            print("Title = ", post["title"])
            print("Date = ", post["date"])
            print("Description = ", post["description"])
            print("====================================================")
           
        
    
