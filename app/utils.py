

import pandas as pd

def load_all_data():
    benin = pd.read_csv("data/benin_clean.csv")
    sierra = pd.read_csv("data/sierra_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")

    benin["Country"] = "Benin"
    sierra["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"

    return pd.concat([benin, sierra, togo], ignore_index=True)
