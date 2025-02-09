# 🎵 Music Recommendation System

A simple music recommendation system built using Python and Flask that suggests songs based on user preferences. The project uses a CSV dataset of songs and provides recommendations based on the entered genre.

---

## 🌟 Features

- Search songs by genre (e.g. Pop, Rock, Hip-Hop).
- Interactive UI with a responsive design.
- "Like" button to engage with recommended songs.
- Background image for an enhanced visual experience.
- Built using Python, Flask, HTML, CSS.

---

## 🛠️ Technologies Used

- **Backend:** Python (Flask, Pandas)
- **Frontend:** HTML, CSS (Responsive Design)
- **Database:** CSV file for storing songs
- **Deployment:** Flask development server

---

## 📂 Project Structure

```
Music-Recommendation-System/
│-- app.py                     # Flask backend
│-- requirements.txt            # Dependencies
│-- data/
│   ├── songs.csv                # Dataset with song information
│-- static/
│   ├── music.jpg                 # Background image
│   ├── styles.css                 # Styling for the web app
│-- templates/
│   ├── index.html                 # Home page
│   ├── recommendations.html        # Recommendations page
│-- README.md                     # Project documentation
```

---

## 🚀 How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShrihariKasar/music-recommendation-system.git
   cd music-recommendation-system
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For macOS/Linux
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```

5. **Open in your browser:**
   ```
   http://127.0.0.1:5000
   ```

---

## 📊 Dataset Details

The `songs.csv` file contains the following fields:

| Song Name                | Artist        | Genre    | Popularity |
|-------------------------|---------------|----------|------------|
| Shape of You             | Ed Sheeran     | Pop      | 95         |
| Blinding Lights          | The Weeknd     | Pop      | 92         |
| Smells Like Teen Spirit  | Nirvana        | Rock     | 90         |

You can expand the dataset by adding more songs in the CSV file.

---

## 🎨 UI Preview

![Music Recommendation UI](https://github.com/ShrihariKasar/Music-Recommendation-System/blob/main/static/UI%20Interface.png)

---

## 🔥 Future Improvements

- Add personalized recommendations using machine learning.
- Integrate a user login system.
- Implement a favorites feature to save liked songs.
- Deploy on platforms like Heroku or AWS.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📞 Contact

For any queries or feedback, reach out via:

- GitHub: [ShrihariKasar](https://github.com/ShrihariKasar)
- Email: shreeharikasar@gmail.com
