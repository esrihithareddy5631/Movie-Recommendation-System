from movies import movies

def display_genres():
    genres = set()

    for movie in movies:
        for genre in movie["genre"]:
            genres.add(genre)

    genres = sorted(list(genres))

    print("\nAvailable Genres:")
    for i, genre in enumerate(genres, start=1):
        print(f"{i}. {genre}")

    return genres


def recommend_movies(selected_genre, min_rating):

    recommendations = []

    for movie in movies:
        if selected_genre in movie["genre"] and movie["rating"] >= min_rating:
            recommendations.append(movie)

    recommendations.sort(key=lambda x: x["rating"], reverse=True)

    return recommendations


def main():

    print("=" * 50)
    print("WELCOME TO MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)

    genres = display_genres()

    try:
        choice = int(input("\nSelect Genre Number: "))
        selected_genre = genres[choice - 1]
    except:
        print("Invalid Choice!")
        return

    try:
        rating = float(input("Minimum Rating (0-10): "))
    except:
        print("Invalid Rating!")
        return

    result = recommend_movies(selected_genre, rating)

    print("\nRecommended Movies\n")

    if len(result) == 0:
        print("No movies found.")
    else:
        for movie in result:
            print("-----------------------------")
            print("Title :", movie["title"])
            print("Genre :", ", ".join(movie["genre"]))
            print("Rating:", movie["rating"])

    print("\nThank you for using the system!")


if __name__ == "__main__":
    main()