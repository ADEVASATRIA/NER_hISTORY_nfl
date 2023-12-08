import spacy
from spacy import displacy

# Load model bahasa Inggris dari spaCy
nlp = spacy.load("en_core_web_sm")

# Baca isi file
file_path = "Text/nfl_history.txt"  # Gantilah dengan path ke file Anda
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Proses teks menggunakan spaCy
doc = nlp(text)

# Membuat kamus untuk menyimpan entitas berdasarkan jenisnya
entity_dict = {label: [] for label in set([ent.label_ for ent in doc.ents])}

# Mengumpulkan entitas berdasarkan jenisnya
for ent in doc.ents:
    entity_dict[ent.label_].append(ent.text)

# Menampilkan entitas berdasarkan jenisnya
print("Named Entities:")
for label, entities in entity_dict.items():
    print(f"{label}: {entities}")

# Visualisasi entitas dengan displaCy
displacy.serve(doc, style="ent")
