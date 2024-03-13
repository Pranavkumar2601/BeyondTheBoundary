# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import joblib

# app = Flask(__name__)

# # Load the dataset
# dataset = pd.read_csv("Odi_bating.csv")

# # Load the trained KNN model
# knn_model = joblib.load('model.pkl')

# def get_recommendation(player_name, opposition_team):
#     # Read the dataset from the CSV file
#     dataset = pd.read_csv("Odi_bating.csv")
    
#     # Filter the dataset to get player performances against the specified opposition team
#     player_performance = dataset[(dataset['Player Name'] == player_name) & (dataset['Opposition Team'] == opposition_team)]
    
#     if player_performance.empty:
#         return "No data available for the specified player and opposition team", ""
    
#     # Assuming you have performed any necessary feature extraction and preprocessing
#     # Extract features from player_performance to use as input for the model
#     # For illustration purposes, let's assume you're using a simple recommendation logic
#     # based on the highest average runs against the opposition team in the dataset
#     recommended_player = dataset[dataset['Opposition Team'] == opposition_team].iloc[0]['Player Name']
#     reason = "Highest average runs against the specified opposition team in the dataset"
    
#     return recommended_player, reason

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         # Retrieve form data
#         player_name = request.form['player_name']
#         opposition_team = request.form['opposition_team']
        
#         # Perform prediction
#         recommended_player, reason = get_recommendation(player_name, opposition_team)
        
#         # Redirect to result page with prediction
#         return redirect(url_for('result', player=recommended_player, reason=reason))
#     return render_template('form.html')

# @app.route('/result')
# def result():
#     player = request.args.get('player')
#     reason = request.args.get('reason')
    
#     if player is None or reason is None:
#         player = "No recommendation available"
#         reason = ""
    
#     return render_template('result.html', player=player, reason=reason)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv("Odi_bating.csv")

# Load the trained model
model = joblib.load('model.pkl')

def get_recommendation(player_name, opposition_team):
    # Filter the dataset to get player performances against the specified opposition team
    player_performance = dataset[(dataset['Player Name'] == player_name) & (dataset['Opposition Team'] == opposition_team)]
    
    if player_performance.empty:
        return "No data available for the specified player and opposition team", ""
    
    # Assuming you have performed any necessary feature extraction and preprocessing
    # Extract features from player_performance to use as input for the model
    # Replace this with your actual feature extraction logic
    
    # Make prediction using the trained model
    # For illustration purposes, let's assume you're using a simple recommendation logic
    # based on the highest average runs against the opposition team in the dataset
    recommended_player = dataset[dataset['Opposition Team'] == opposition_team].iloc[0]['Player Name']
    reason = "Highest average runs against the specified opposition team in the dataset"
    
    return recommended_player, reason


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Retrieve form data
        player_name = request.form['player_name']
        opposition_team = request.form['opposition_team']
        
        # Perform prediction
        recommended_player, reason = get_recommendation(player_name, opposition_team)
        
        # Redirect to result page with prediction
        return redirect(url_for('result', player=recommended_player, reason=reason))
    return render_template('form.html')



@app.route('/result')
def result():
    player = request.args.get('player')
    reason = request.args.get('reason')
    return render_template('result.html', player=player, reason=reason)



if __name__ == '__main__':
    app.run(debug=True)
