import pandas as pd

#  ımdb tablosunu okuma
imdb = pd.read_csv("movies_imdb.csv")

#
ext = pd.read_csv("movies.csv")

print("--- imdb.shape ---")
print(imdb.shape)
display(imdb.head())
# boyut kontrol edilir
print("\n--- ext.shape ---")
print(ext.shape)
display(ext.head())

#  film adı aynı kolon ismiyle olmalı - name ise title ile değiştirilir

ext = ext.rename(columns={
    "name": "title"
})

#  gereken kolonlar seçilir
ext_small = ext[["title", "year", "budget", "gross", "votes"]]

print(ext_small.shape)
display(ext_small.head())


combined = imdb.merge(
    ext_small,
    on=["title", "year"],  
    how="left"              
)
# kaç filmde gross var / merge kalitesi anlaşılır
print("combined shape:", combined.shape)
display(combined.head())

#  çıktısı alınır EDA ve ML de kıllanulacak dataset
print("\nBudget dolu satır sayısı:", combined["budget"].notna().sum())
print("Gross dolu satır sayısı:", combined["gross"].notna().sum())


output_path = "movies_with_revenue.csv"
combined.to_csv(output_path, index=False)