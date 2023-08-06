from sklearn.model_selection import train_test_split
import autokeras as ak

class AutoML:
    def train(self, X, y):
        # Divide el conjunto de datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        # Usa AutoKeras para encontrar el mejor modelo
        clf = ak.StructuredDataClassifier(max_trials=10)
        clf.fit(X_train, y_train, epochs=10)
        accuracy = clf.evaluate(X_test, y_test)
        return clf, accuracy


