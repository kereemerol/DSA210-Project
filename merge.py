import pandas as pd
# IMDb title.basics ve title.ratings dosyalarının yolları
basics_path = "../data/raw/title.basics.tsv"
ratings_path = "../data/raw/title.ratings.tsv"
# TSV dosyalarını okuma
basics = pd.read_csv(basics_path, sep="\t", low_memory=False, na_values="\\N")
ratings = pd.read_csv(ratings_path, sep="\t", low_memory=False, na_values="\\N")
#boyutları kontrol etmek
print("Basics dosyası şekli:", basics.shape)
print("Ratings dosyası şekli:", ratings.shape)

basics = basics[basics["titleType"] == "movie"]#Sadece filmler
basics = basics[(basics["startYear"] >= 1995) & (basics["startYear"] <= 2024)]# Sadece 1995-2024 arasındaki filmler
basics = basics[basics["isAdult"] == 0]# Non-adult
basics = basics[basics["runtimeMinutes"].notna()]  #Süre bilgisi olanlar

#Tablo kontrol
print("Basics filtrelerden sonra:", basics.shape)
# Imdb tabloları tconst ile birleştirilir
merged = basics.merge(ratings, on="tconst", how="inner")
print("Birleşmiş tablo:", merged.shape)

# En az 1000 oy alanlar seçilir
merged = merged[merged["numVotes"] >= 1000]
print("1000 oy filtresinden sonra:", merged.shape)

#Analiz sütunları seçilir
merged = merged[[
    "tconst", "primaryTitle", "startYear", "runtimeMinutes", 
    "genres", "averageRating", "numVotes"
]]

merged.columns = [
    "id", "title", "year", "runtime", "genres",
    "rating", "numVotes"
]

# Birleşmiş tablo csv olarak kaydedilir
output_path = "../data/movies_imdb.csv"
merged.to_csv(output_path, index=False)
