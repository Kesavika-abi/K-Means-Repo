# app.py

import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_data(df):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df = df[numeric_cols]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    return scaled, df.columns.tolist(), df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        df = pd.read_csv(filepath)
        data_scaled, columns, original_df = preprocess_data(df)

        # Elbow Method Plot
        distortions = []
        K = range(1, 10)
        for k in K:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(data_scaled)
            distortions.append(kmeans.inertia_)

        plt.figure()
        plt.plot(K, distortions, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Distortion')
        plt.title('Elbow Method For Optimal k')
        elbow_plot_path = 'static/elbow_plot.png'
        plt.savefig(elbow_plot_path)
        plt.close()

        # Apply KMeans with k=3 (can be changed after elbow observation)
        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(data_scaled)
        original_df['Cluster'] = clusters

        # Cluster Scatter Plot (first two features)
        plt.figure()
        plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=clusters, cmap='viridis')
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
        plt.title("Spotify User Segments")
        cluster_plot_path = 'static/cluster_plot.png'
        plt.savefig(cluster_plot_path)
        plt.close()

        # Export clustered data
        output_path = os.path.join("uploads", "clustered_output.csv")
        original_df.to_csv(output_path, index=False)

        return render_template(
            'result.html',
            tables=[original_df.to_html(classes='data', header=True, index=False)],
            cluster_plot=cluster_plot_path,
            elbow_plot=elbow_plot_path,
            download_link=output_path
        )

    return "Invalid file format. Please upload a CSV file."

if __name__ == '__main__':
    app.run(debug=True)
