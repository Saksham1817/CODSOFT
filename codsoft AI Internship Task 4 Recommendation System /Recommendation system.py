from collections import defaultdict

users = {
    "Harry": [("Harry Potter", 5), ("Spider Man", 4), ("James Bond", 3)],
    "Tobi": [("Harry Potter", 4), ("The Dark Knight", 5), ("Two States", 3)],
    "Ethan": [("James Bond", 5), ("Two States", 4), ("World War One", 3)],
    "Veer": [("James Bond", 5), ("Two States", 5), ("The Dark Knight", 3)],
    "Tommy": [("Harry Potter", 3), ("The Dark Knight", 3), ("World War One", 3)],
    "Jolly": [("James Bond", 5), ("Two States",  3), ("Harry Potter", 4)],
    "Bob": [("Harry Potter", 4), ("Harry Potter", 3), ("World War One", 5)],
    "Bean": [("James Bond", 5), ("Two States", 4), ("The Dark Knight", 3)],
    "Elon": [("James Bond", 4), ("Harry Potter", 4), ("Spider Man", 3)],
}

movies = {
    "Harry Potter": {"genre": "fantasy", "keywords": ["magic", "adventure"]},
    "Spider Man": {"genre": "sci-fi", "keywords": ["space", "aliens"]},
    "James Bond": {"genre": "mystery", "keywords": ["detective", "crime"]},
    "The Dark Knight": {"genre": "thriller", "keywords": ["suspense", "action"]},
    "Two States": {"genre": "romance", "keywords": ["love", "relationships"]},
    "World War One": {"genre": "historical fiction", "keywords": ["war", "history"]},
}


def create_user_vector(user_data):
    user_vector = defaultdict(int)
    for movie, rating in user_data:
        for keyword in movies[movie]["keywords"]:
            user_vector[keyword] += rating
        user_vector[movies[movie]["genre"]] += rating  # Add genre to user vector
    return user_vector


def create_movie_vector(movie_data):
    movie_vector = defaultdict(int)
    for keyword in movie_data["keywords"]:
        movie_vector[keyword] = 1
    movie_vector[movie_data["genre"]] = 1  # Add genre to movie vector
    return movie_vector


def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1.values(), vec2.values()))
    mag1 = sum(v * v for v in vec1.values()) ** 0.5
    mag2 = sum(v * v for v in vec2.values()) ** 0.5
    if mag1 * mag2 == 0:
        return 0
    return dot_product / (mag1 * mag2)


user_vectors = {user: create_user_vector(data) for user, data in users.items()}
movie_vectors = {movie: create_movie_vector(data) for movie, data in movies.items()}


def recommend_movies(user, genre, n=3):
    user_vec = user_vectors[user]
    # Filter movie vectors based on the user's chosen genre
    genre_movie_vectors = {movie: vec for movie, vec in movie_vectors.items() if movies[movie]["genre"] == genre}
    similarities = {movie: cosine_similarity(user_vec, movie_vec) for movie, movie_vec in genre_movie_vectors.items() if movie not in [b[0] for b in users[user]]}
    sorted_sims = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
    return sorted_sims[:n]


user = "Harry"
user_genre = "sci-fi"  # Example user-chosen genre
recommendations = recommend_movies(user, user_genre)
print(f"Recommendations for {user} in the {user_genre} genre:")
for movie, similarity in recommendations:
    print(f"- {movie} ({similarity:.2f})")
