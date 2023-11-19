import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Charger les données depuis le fichier CSV
file_path = "customer_churn.csv"
data = pd.read_csv(file_path)

label_encoder = LabelEncoder()

# Appliquer le LabelEncoder à la colonne "Location"
data['Location'] = label_encoder.fit_transform(data['Location'])
data['Company'] = label_encoder.fit_transform(data['Company'])
data['Names'] = label_encoder.fit_transform(data['Names'])
data['Onboard_date'] = label_encoder.fit_transform(data['Onboard_date'])

# Diviser les données en features (X) et labels (y)
X = data.drop('Churn', axis=1)  
y = data['Churn']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normaliser des données 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialiser les classificateurs
rf_classifier = RandomForestClassifier()
svm_classifier = SVC()
lr_classifier = LogisticRegression()

# Entraîner les classificateurs
rf_classifier.fit(X_train_scaled, y_train)
svm_classifier.fit(X_train_scaled, y_train)
lr_classifier.fit(X_train_scaled, y_train)

# Faire des prédictions sur les ensembles de test
rf_predictions = rf_classifier.predict(X_test_scaled)
svm_predictions = svm_classifier.predict(X_test_scaled)
lr_predictions = lr_classifier.predict(X_test_scaled)

# Évaluer les classificateurs
rf_accuracy = accuracy_score(y_test, rf_predictions)
svm_accuracy = accuracy_score(y_test, svm_predictions)
lr_accuracy = accuracy_score(y_test, lr_predictions)

print(rf_accuracy)
print(svm_accuracy)
print(lr_accuracy)

# Sélectionner le meilleur classificateur
best_classifier = max([(rf_accuracy, 'Random Forest'), (svm_accuracy, 'SVM'), (lr_accuracy, 'Logistic Regression')])

print(f"Le meilleur classificateur est {best_classifier[1]} avec une précision de {best_classifier[0]:.2f}")

# Sauvegarder le meilleur classificateur
if best_classifier[1] == 'Random Forest':
    joblib.dump(rf_classifier, 'RF_modele.pkl')
elif best_classifier[1] == 'SVM':
    joblib.dump(svm_classifier, 'SVM_modele.pkl')
else:
    joblib.dump(lr_classifier, 'LR_modele.pkl')
