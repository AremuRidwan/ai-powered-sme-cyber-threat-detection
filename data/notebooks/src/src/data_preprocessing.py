import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(file_paths):
    dfs = [pd.read_csv(path) for path in file_paths]
    data = pd.concat(dfs, ignore_index=True)

    data = data.dropna()
    data = data.replace([float('inf'), -float('inf')], 0)

    X = data.drop(columns=['Label'])
    y = data['Label']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler
