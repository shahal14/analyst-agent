import pandas as pd
import os

def save_to_csv(results, path="data/cleaned_output.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv(path, index=False, encoding="utf-8")
    return df
