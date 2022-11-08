import pandas as pd

def load_and_process(raw):
    df = pd.read_csv(raw)
    
    clean = (df.copy()
             .drop(['Remove', 'Source.Name','SourceFile', 'Other', 'Std Dev', 'Audit'], axis=1)
             .astype(str)
    )
    clean = (clean.drop(clean[clean.Campus == 'Campus'].index)
             .dropna(how='all')
             )

    
    return clean