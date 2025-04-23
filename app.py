from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load song dataset
df = pd.read_csv('data/songs.csv')

# Function to recommend songs
def recommend_songs(genre):
    recommendations = df[df['Genre'].str.lower() == genre.lower()]
    return recommendations[['Song Name', 'Artist']].to_dict(orient='records')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        genre = request.form['genre']
        recommendations = recommend_songs(genre)
        return render_template('recommendations.html', songs=recommendations)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)