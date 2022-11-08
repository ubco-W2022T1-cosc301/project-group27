import pandas as pd

def load_and_process(raw):
    df = pd.read_csv(raw)
    clean = (df.copy().drop(['Remove', 'Source.Name','SourceFile', 'Other', 'Std Dev', 'Audit'], axis=1)
             .drop(clean[clean.Campus == 'Campus'].index)
             .astype(str)
    )
    
    
    return clean