import polars as pl

lf = (
    pl.LazyFrame({
        'Letter': ['a', 'a','a','b', 'b', 'b', 'c', 'c', 'd'],
        'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9]
    })
    .group_by('Letter')
    .agg(pl.col('Value'))
    .sort('Letter')
)

print(lf.fetch())
