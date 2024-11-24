from flask import Flask, request, render_template
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
app = Flask(__name__)
data = pd.DataFrame({
    'Title': ['Inception', 'The Matrix', 'Interstellar', 'Shutter Island', 'Memento'],
    'Genre': ['Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Thriller', 'Thriller']
})
def recommend(movie_title):
    cv = CountVectorizer()
    genre_matrix = cv.fit_transform(data['Genre'])
    similarity = cosine_similarity(genre_matrix)
    idx = data[data['Title'] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommended = [data['Title'][i] for i, _ in scores[1:4]]
    return recommended
@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    if request.method == "POST":
        movie = request.form["movie"]
        recommendations = recommend(movie)
    return render_template("recommend.html", movies=data['Title'], recommendations=recommendations)
if __name__ == "__main__":
    app.run(debug=True)