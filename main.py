import requests
import random

API_KEY = "faef3ce96dde4b92db5a67a6d064a386"
BASE_URL = "https://api.themoviedb.org/3"

watched_movies = []

def search_movie(movie_name):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    data = response.json()
    if data.get("results"):
        return data["results"][0]
    return None

def get_trending(time_window="week"):
    url = f"{BASE_URL}/trending/all/{time_window}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("results", [])

def recommend_random():
    trending = get_trending("week")
    if trending:
        choice = random.choice(trending)
        title = choice.get("title") or choice.get("name")
        rating = choice.get("vote_average", "N/A")
        return title, rating
    return None, None

def main():
    while True:
        print("\nChoose an option:")
        print("1. Search for a movie by name")
        print("2. Show top trending movies/shows this week")
        print("3. Recommend me something random (Anime/Movie) with rating")
        print("4. Show my watched list")
        print("5. Exit")

        choice = input("Enter choice: ")

                if choice == "1":
            movie_name = input("Enter movie name: ")
            result = search_movie(movie_name)
            if result:
                title = result.get("title") or result.get("name")
                release_date = result.get("release_date", "N/A")
                rating = result.get("vote_average", "N/A")
                overview = result.get("overview", "No description available.")

                print("\nMovie Found!")
                print(f"Title: {title}")
                print(f"Release Date: {release_date}")
                print(f"Rating: {rating}/10")
                print(f"Overview: {overview}")

                watched_movies.append(title)
            else:
                print("Movie not found.")

        elif choice == "2":
            trending = get_trending("week")
            print("\nTop Trending Movies/Shows This Week:")
            for i, item in enumerate(trending[:10], 1):
                title = item.get("title") or item.get("name")
                print(f"{i}. {title}")

        elif choice == "3":
            title, rating = recommend_random()
            if title:
                print(f"Recommendation: {title} (Rating: {rating}/10)")
                watched_movies.append(title)
            else:
                print("No recommendations available.")

        elif choice == "4":
            print("\nYour Watched Movies/Shows:")
            if watched_movies:
                for i, movie in enumerate(watched_movies, 1):
                    print(f"{i}. {movie}")
            else:
                print("No movies watched yet.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
