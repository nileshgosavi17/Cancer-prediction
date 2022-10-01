import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from joblib import dump, load
from sklearn.model_selection import train_test_split, cross_val_score
import warnings
warnings.filterwarnings("ignore")


class KNNeighbors:

    def __init__(self):
        pass

    def load_test_dataset(self, df):
        df = df.copy()

        # Drop missing column


        # Split df into X and y
        y = df['diagnosis']
        X = df.drop(['diagnosis','id'], axis=1)

        # Train-test split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, train_size=0.7, shuffle=True,
                                                                                random_state=1)
        return self.X_train, self.X_test, self.y_train, self.y_test

    def train_model(self):
        df = pd.read_csv('dataset/data.csv')
        self.X_train, self.X_test, self.y_train, self.y_test = self.load_test_dataset(df)
        targets = df.diagnosis
        drop_columns = ['id', 'diagnosis']
        attributes = df.drop(labels=drop_columns, axis=1)
        scaler = StandardScaler()
        scaler.fit(attributes)
        scaled_numerical = scaler.transform(attributes)
        df_scaled_numerical = pd.DataFrame(data=scaled_numerical,
                                           columns=['radius_mean', 'texture_mean', 'perimeter_mean',
                                                    'area_mean', 'smoothness_mean', 'compactness_mean',
                                                    'concavity_mean',
                                                    'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
                                                    'radius_se', 'texture_se', 'perimeter_se', 'area_se',
                                                    'smoothness_se',
                                                    'compactness_se', 'concavity_se', 'concave points_se',
                                                    'symmetry_se',
                                                    'fractal_dimension_se', 'radius_worst', 'texture_worst',
                                                    'perimeter_worst', 'area_worst', 'smoothness_worst',
                                                    'compactness_worst', 'concavity_worst', 'concave points_worst',
                                                    'symmetry_worst', 'fractal_dimension_worst'])

        self.model = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
        #print(df_scaled_numerical)
        self.model.fit(df_scaled_numerical, targets)
        self.model.fit(self.X_train, self.y_train)


        dump(self.model, str("savedmodels/KNeighborsClassifier.joblib"))

    def make_prediction(self, saved_model_name=None, test_data=None):
        try:
            # Load Trained Model
            clf = load(str('savedmodels/' + saved_model_name + ".joblib"))
            print("Model Loaded...")
        except Exception as e:
            print("Model not found...")

        if test_data is not None:
            result = clf.predict(test_data)
            return result

        return "NO data"
