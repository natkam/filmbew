import pandas as pd

df = pd.read_pickle('data/filmweb_df')
review_counts_per_author = df['author'].value_counts()
serious_authors = review_counts_per_author[review_counts_per_author >= 100]
review_set = df[df.author.isin(serious_authors.index)]
