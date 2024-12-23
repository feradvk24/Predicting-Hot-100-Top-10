from sklearn.metrics import classification_report, mean_absolute_error, mean_squared_error, r2_score
import numpy as np


def get_classification_report(model, X_train, X_test, y_train, y_test):
    """
    Train a model and print the classification report.

    Args:
        model: The machine learning model to train and evaluate.
        X_train: Training feature set.
        X_test: Test feature set.
        y_train: Training labels.
        y_test: Test labels.

    Returns:
        None
    """
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    

def evaluate_regression_model(model, X_train, X_test, y_train, y_test):
    """
    Train a regression model and evaluate its performance using common metrics.

    Args:
        model: The regression model to train and evaluate.
        X_train: Training feature set.
        X_test: Test feature set.
        y_train: Training labels.
        y_test: Test labels.

    Returns:
        None
    """
    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Predict on the test data
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    # Print the scores
    print("Regression Evaluation Metrics:")
    print(f"R-squared: {r2:.2f}")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")