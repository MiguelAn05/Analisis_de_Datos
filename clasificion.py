import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

try:
    archivo_csv = "datos_categorizados.csv"
    dataframe = pd.read_csv(archivo_csv)

    
    dataframe = dataframe.drop(columns=['Grupo de Edad'])

    
    X = dataframe.drop(columns=['DEATH_EVENT'])
    y = dataframe['DEATH_EVENT']

    
    plt.figure()
    y.value_counts().plot(kind='bar', title='Distribución de clases')
    plt.show()

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    
    best_accuracy = 0
    best_depth = 0
    best_classifier = None

    for depth in range(1, 21):
        classifier = DecisionTreeClassifier(max_depth=depth, random_state=42)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_depth = depth
            best_classifier = classifier

    print(f"El  árbol de decisión tiene una profundidad de {best_depth} y accuracy en el conjunto de prueba: {best_accuracy:.2f}")

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")