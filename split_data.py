import json
import os

# Ana JSON dosyasının yolunu belirt
input_file = 'testnew-2fe14-default-rtdb-export (4).json'  # Dosya adını kendi dosyana göre değiştir

# Verilerin kaydedileceği klasör
output_folder = 'son_ekg'
os.makedirs(output_folder, exist_ok=True)

# JSON dosyasını yükle
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Her bir data_X alanını ayrı dosyaya kaydet
for key, value in data.items():
    if key.startswith('data_'):
        index = key.split('_')[1]  # "48", "49" gibi
        output_filename = f"ekg_data{index}.json"
        output_path = os.path.join(output_folder, output_filename)

        # Sadece "values" kısmını kaydetmek istersen:
        # to_save = value["values"]
        # Eğer tamamını (örneğin: {"values": [...]} şeklinde) kaydetmek istersen:
        to_save = value

        with open(output_path, 'w', encoding='utf-8') as out_file:
            json.dump(to_save, out_file, ensure_ascii=False, indent=2)

print("Veriler başarıyla ayrıldı ve kaydedildi.")
