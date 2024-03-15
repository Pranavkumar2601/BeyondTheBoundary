# import pandas as pd
# from flask import Flask, render_template, request, redirect, url_for
# import joblib
# import ipywidgets as widgets
# from IPython.display import display

# app = Flask(__name__)


# dataset = pd.read_csv("Odi_bating.csv")

# dataset['HS'] = dataset['HS'].str.replace('*', '')

# # Convert 'HS' column to numeric, errors='coerce' will replace non-numeric values with NaN
# dataset['HS'] = pd.to_numeric(dataset['HS'], errors='coerce')

# # Replace NaN values with 0
# dataset['HS'].fillna(0, inplace=True)


# # Load the trained KNN model
# knn_model = joblib.load('model.pkl')

# def get_opposition_teams():
#     # Retrieve unique opposition team names from the dataset
#     opposition_teams = dataset['Opposition Team'].unique()
#     return opposition_teams

# def get_recommendation(player_name, opposition_team):
#     # Filter the dataset to get player performances against the specified opposition team
#     player_performance = dataset[(dataset['Player Name'] == player_name) & (dataset['Opposition Team'] == opposition_team)]
    
#     if player_performance.empty:
#         return "No data available for the specified player and opposition team", ""
    
    
#     selected_features = ['Runs', 'HS', 'Ave', 'SR', '100', '50', '4s', '6s']
#     features = player_performance[selected_features].values
    
#     # Make prediction using the trained model
#     predicted_player = knn_model.predict(features)
    
    
#     return predicted_player[0], "Recommended based on the trained model"


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
#     return render_template('result.html', player=player, reason=reason)


# if __name__ == '__main__':
#     app.run(debug=True)




#### using javaScript  susbstittution
# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import joblib

# app = Flask(__name__)

# # Load the dataset
# dataset = pd.read_csv("Odi_bating.csv")

# # Load the trained model
# model = joblib.load('model.pkl')

# def get_recommendation(player_name, opposition_team):
#     # Filter the dataset to get player performances against the specified opposition team
#     player_performance = dataset[(dataset['Player Name'] == player_name) & (dataset['Opposition Team'] == opposition_team)]
    
#     if player_performance.empty:
#         return "No data available for the specified player and opposition team", ""
    
    
#     recommended_player = dataset[dataset['Opposition Team'] == opposition_team].iloc[0]['Player Name']
#     reason = "Highest average runs against the specified opposition team"
    
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
#     return render_template('result.html', player=player, reason=reason)



# if __name__ == '__main__':
#     app.run(debug=True)


#####################################cheking function
# import pandas as pd
# from flask import Flask, render_template, request, redirect, url_for
# import joblib

# app = Flask(__name__)

# # Load dataset
# dataset = pd.read_csv("Odi_bating.csv")

# # Load the trained KNN model
# knn_model = joblib.load('model.pkl')

# def get_opposition_teams():
#     # Retrieve unique opposition team names from the dataset
#     opposition_teams = dataset['Opposition Team'].unique()
#     return opposition_teams

# def get_recommendation(player_name, opposition_team):
#     # Filter the dataset to get player performances against the specified opposition team
#     player_performance = dataset[(dataset['Player Name'] == player_name) & (dataset['Opposition Team'] == opposition_team)]
    
#     if player_performance.empty:
#         return "No data available for the specified player and opposition team", ""
    
#     selected_features = ['Runs', 'HS', 'Ave', 'SR', '100', '50', '4s', '6s']
#     features = player_performance[selected_features].values
    
#     # Make prediction using the trained model
#     predicted_player = knn_model.predict(features)
    
#     return predicted_player[0], "Recommended based on the trained model"

# @app.route('/')
# def home():
#     return render_template('home.html', opposition_teams=get_opposition_teams())

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
#     return render_template('form.html', opposition_teams=get_opposition_teams())

# @app.route('/result')
# def result():
#     player = request.args.get('player')
#     reason = request.args.get('reason')
#     return render_template('result.html', player=player, reason=reason)

# if __name__ == '__main__':
#     app.run(debug=True)


########### Model Checkig
# import pandas as pd
# from flask import Flask, render_template, request, redirect, url_for
# import joblib

# app = Flask(__name__)

# # Load dataset
# dataset = pd.read_csv("Odi_bating.csv")

# # Load the trained KNN model
# knn_model = joblib.load('model.pkl')

# def get_opposition_teams():
#     # Retrieve unique opposition team names from the dataset
#     opposition_teams = dataset['Opposition Team'].unique()
#     return opposition_teams

# def get_recommendation(player_name, opposition_team):
#     # Filter the dataset to get player performances against the specified opposition team
#     player_performance = dataset[(dataset['Player Name'] == player_name) & (dataset['Opposition Team'] == opposition_team)]
    
#     if player_performance.empty:
#         return "No data available for the specified player and opposition team", ""
    
#     selected_features = ['Runs', 'HS', 'Ave', 'SR', '100', '50', '4s', '6s']
#     features = player_performance[selected_features].values
    
#     # Make prediction using the trained model
#     predicted_player = knn_model.predict(features)
    
#     return predicted_player[0], "Recommended based on the trained model"

# @app.route('/')
# def home():
#     return render_template('home.html', opposition_teams=get_opposition_teams())

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
#     return render_template('form.html', opposition_teams=get_opposition_teams())

# @app.route('/result')
# def result():
#     player = request.args.get('player')
#     reason = request.args.get('reason')
#     return render_template('result.html', player=player, reason=reason)

# if __name__ == '__main__':
#     app.run(debug=True)


import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__)

# Load dataset
dataset = pd.read_csv("Odi_bating.csv")
dataset['HS'] = dataset['HS'].str.replace('*', '')

# # Convert 'HS' column to numeric, errors='coerce' will replace non-numeric values with NaN
dataset['HS'] = pd.to_numeric(dataset['HS'], errors='coerce')

# # Replace NaN values with 0
dataset['HS'].fillna(0, inplace=True)

# Load the trained KNN model
knn_model = joblib.load('model.pkl')

def get_opposition_teams():
    # Retrieve unique opposition team names from the dataset
    opposition_teams = dataset['Opposition Team'].unique()
    return opposition_teams

def get_player_names():
    # Retrieve unique player names from the dataset
    player_names = dataset['Player Name'].unique()
    return player_names


def get_recommendation(player_name, opposition_team):
    # Filter the dataset to get player performances against the specified opposition team
    player_performance = dataset[(dataset['Player Name'] == player_name) & (dataset['Opposition Team'] == opposition_team)]
    
    if player_performance.empty:
        return "No data available for the specified player and opposition team", ""
    
    selected_features = ['Runs', 'HS', 'Ave', 'SR', '100', '50', '4s', '6s']
    features = player_performance[selected_features].values
    
    # Make prediction using the trained model
    predicted_player = knn_model.predict(features)
    
    return predicted_player[0], "Recommended based on the trained model"

@app.route('/')
def home():
    return render_template('home.html', opposition_teams=get_opposition_teams(), player_names=get_player_names())


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
    return render_template('form.html', opposition_teams=get_opposition_teams(), player_names=get_player_names())

@app.route('/result')
def result():
    player = request.args.get('player')
    reason = request.args.get('reason')
    return render_template('result.html', player=player, reason=reason)

if __name__ == '__main__':
    app.run(debug=True)
