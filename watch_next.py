import spacy

nlp = spacy.load("en_core_web_md")

with open("movies.txt", "r") as f:
    movies = f.readlines()


def movie_recommendation(description_hulk):
    doc = nlp(description_hulk)
    best_match = ""
    best_score = 0

    for movie in movies:
        movie_doc = nlp(movie.split(":")[1])
        score = doc.similarity(movie_doc)
        if score > best_score:
            best_match = movie.split(":")[0]
            best_score = score
        return best_match.strip()


description_hulk = ("""Will he save
            their world or destroy it? When the Hulk becomes too dangerous for the
            Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
            planet where the Hulk can live in peace. Unfortunately, Hulk land on the
            planet Sakaar where he is sold into slavery and trained as a gladiator.""")

best_match = movie_recommendation(description_hulk)
print("The next movie to watch that best matches your description would be:", best_match)
