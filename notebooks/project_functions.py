import pandas as pd

def load_and_process(raw):
    df = pd.read_csv(raw)
    
    
    clean = (df.copy()
             .drop(['Remove', 'Source.Name','SourceFile', 'Other', 'Std Dev', 'Audit'], axis=1)
             .astype(str)
    )
    clean = (clean.drop(clean[clean.Campus == 'Campus'].index)
             .drop(clean[clean.Enrolled < 8].index, inplace=True)
             )
    
    clean['Average'] = clean['Average'].fillna(value=0)
    return clean