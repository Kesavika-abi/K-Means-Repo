
# Spotify User Listening Pattern Segmentation using K-Means Clustering

This project is a Flask-based web application that segments Spotify users based on their listening behavior using the K-Means clustering algorithm. It includes an interactive interface to upload CSV datasets, visualize optimal clusters using the Elbow Method, and export the segmented data.

## Use Case

**Objective**: Identify distinct listening behavior segments to enable personalized recommendations or marketing strategies.

**Example Features Used**:
- Hours listened per day
- Genre preference (numerically encoded)
- Skip rate
- Number of liked songs
- Artist diversity index

## Features

- Upload your own CSV file of user data
- Automatically preprocesses and standardizes data
- Elbow method to determine optimal number of clusters (k)
- Visual clustering plot based on key behavioral features
- Export segmented results to CSV
- Clean and responsive interface using HTML/CSS

## Folder Structure

spotify-user-segmentation/
│
├── static/
│   └── style.css                # CSS styling
│
├── templates/
│   ├── index.html               # Upload form page
│   └── result.html              # Result page (table + visualizations)
│
├── uploads/                     # Uploaded and output CSV files
│
├── synthetic_spotify_user_data.csv # Example dataset
├── app.py                       # Flask application
├── requirements.txt             # Required dependencies
└── README.md                    # Project documentation
````

## Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/spotify-user-segmentation.git
cd spotify-user-segmentation
```

### 2. Install Dependencies

Ensure you're using Python 3.8 or above.

pip install -r requirements.txt
```

### 3. Run the Application

python app.py
```

Then visit:
`http://127.0.0.1:5000/`

## How to Use

1. Upload a CSV file containing Spotify user behavior data.
2. The app will:

   * Preprocess the data
   * Show the elbow method plot
   * Apply K-Means clustering (default k=3)
   * Visualize clusters
   * Let you download the output with cluster labels
