import numpy as np

# This function prints the shape of the feature and target arrays
# X: a 2D array of features
# y: a 1D array of targets

def print_shape(X, y):
    print("X shape is ", X.shape)
    print("y shape is ", y.shape)

# This function sorts the feature and target arrays
# X: a 2D array of features
# y: a 1D array of targets

def sort_dataset(X, y):
    idx = np.argsort(np.sum(X, axis=1))
    return X[idx], y[idx]

def make_polynomial(n_samples=100, n_features=5, degree = 2, noise=0.0, random_state=None):
    np.random.seed(random_state)

    X = np.random.uniform(low = -1.0, high = 1.0, size = (n_samples, n_features))

    # Add noise to features before any adjustments
    X += np.random.normal(scale=noise, size=(n_samples, n_features))

    y = np.power(np.sum(X, axis=1), degree)

    return X, y