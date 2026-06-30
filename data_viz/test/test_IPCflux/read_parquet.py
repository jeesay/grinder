import polars as pl
from pathlib import Path

dir = Path('./files')

for file in [f.name for f in dir.iterdir() if f.is_file()] :
	print(f"File : {file}", '\n')
	df = pl.read_parquet(f"{dir}/{file}")
	print(df)
