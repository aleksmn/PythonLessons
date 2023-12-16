
# task 2
serials_db = [ { "title": "Chronicles of the Galaxy", "genre": "Adventure", "seasons": 5, "rating": 8 }, { "title": "Mystery Island", "genre": "Fantasy", "seasons": 3, "rating": 9 }, { "title": "Epic Quest", "genre": "Fantasy", "seasons": 4, "rating": 7 }, { "title": "Crime Files", "genre": "Crime Drama", "seasons": 6, "rating": 5}, { "title": "Medical Miracles", "genre": "Medical Drama", "seasons": 2, "rating": 8 }, { "title": "Time Travelers", "genre": "Adventure", "seasons": 4, "rating": 8 }, { "title": "Comedy Central", "genre": "Comedy", "seasons": 7, "rating": 9 } ]

def search_by_genre(genre):
    found_serials = []
    for serial in serials_db:
        if serial["genre"].lower() == genre.lower():
            found_serials.append(serial)
    return found_serials

def search_by_rating(rating):
    found_serials = []
    for serial in serials_db:
        if serial["rating"] == rating:
            found_serials.append(serial)
    return found_serials


def display_all_serials():
    for serial in serials_db:
        print(f"Title: {serial['title']}, Genre: {serial['genre']}, Seasons: {serial['seasons']}, Rating: {serial['rating']}")

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Search TV shows by genre")
        print("2. Search TV shows by rating")
        print("3. Display information about all TV shows")
        print("4. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            genre = input("Enter the genre: ")
            found_serials = search_by_genre(genre)
            if found_serials:
                print("TV shows with genre", genre)
                for serial in found_serials:
                    print(serial["title"])
            else:
                print("No TV shows found with genre", genre)

        elif choice == "2":
            rating = float(input("Enter the rating: "))
            found_serials = search_by_rating(rating)
            if found_serials:
                print("TV shows with rating", rating)
                for serial in found_serials:
                    print(serial["title"])
            else:
                print("No TV shows found with rating", rating)

        elif choice == "3":
            display_all_serials()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid input. Please try again.")