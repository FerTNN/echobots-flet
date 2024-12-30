import pandas as pd
import json
import os
import re
import requests
from urllib.parse import urlparse, parse_qs

class ExcelToJsonConverter:
    def __init__(self, excel_file, output_folder="output", images_folder="images"):
        self.excel_file = excel_file
        self.output_folder = output_folder
        self.images_folder = os.path.join(output_folder, images_folder)
        self.columns = [
            "Бот", "Нынешний юз", "Первый запуск", "Второй запуск", 
            "Старый юз", "Кд", "Примечания", "Дата смерти", "Владелец",
            "Функционал (команды)", "Кол-во юзеров", "Статус",
            "Каналы Ботов", "Сурсы", "Айди"
        ]
        self._setup_folders()

    def _setup_folders(self):
        """Create necessary folders if they don't exist"""
        os.makedirs(self.output_folder, exist_ok=True)
        os.makedirs(self.images_folder, exist_ok=True)

    def _extract_drive_id(self, url):
        """Extract Google Drive file ID from URL"""
        if not url or not isinstance(url, str):
            return None
        
        if 'drive.google.com' not in url:
            return None

        parsed = urlparse(url)
        if 'file/d/' in url:
            file_id = url.split('file/d/')[1].split('/')[0]
        else:
            query_params = parse_qs(parsed.query)
            file_id = query_params.get('id', [None])[0]
        
        return file_id

    def _download_image(self, url, row_index):
        """Download image from Google Drive"""
        file_id = self._extract_drive_id(url)
        if not file_id:
            return None

        download_url = f"https://drive.usercontent.google.com/u/0/uc?id={file_id}&export=download"
        
        try:
            response = requests.get(download_url)
            if response.status_code == 200:
                file_path = os.path.join(self.images_folder, f"image_{row_index}_{file_id}.jpg")
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                return file_path
        except Exception as e:
            print(f"Error downloading image: {e}")
        
        return None

    def _process_cell(self, value, row_index):
        """Process cell content, download images if needed"""
        if pd.isna(value):
            return "Пустая ячейка"
        
        value = str(value)
        if 'drive.google.com' in value:
            image_path = self._download_image(value, row_index)
            return {
                'text': value,
                'image_path': image_path
            }
        
        return value if value not in ['?', '-'] else value

    def convert(self):
        """Convert Excel file to JSON"""
        # Read Excel file
        df = pd.read_excel(self.excel_file)
        
        # Ensure all columns exist
        for col in self.columns:
            if col not in df.columns:
                df[col] = "Пустая ячейка"

        # Process merged cells
        for col in df.columns:
            current_value = None
            merge_count = 0
            
            for idx in range(len(df)):
                if pd.notna(df.iloc[idx][col]):
                    if merge_count > 0:
                        # Fill previous merged cells
                        df.iloc[idx-merge_count:idx, df.columns.get_loc(col)] = current_value
                    current_value = df.iloc[idx][col]
                    merge_count = 0
                else:
                    merge_count += 1

            # Handle last merge group if exists
            if merge_count > 0:
                df.iloc[-merge_count:, df.columns.get_loc(col)] = current_value

        # Convert to JSON
        result = []
        for idx, row in df.iterrows():
            entry = {}
            for col in self.columns:
                entry[col] = self._process_cell(row[col], idx)
            result.append(entry)

        # Save JSON
        output_file = os.path.join(self.output_folder, 'output.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        return output_file

def main():
    converter = ExcelToJsonConverter('table.xlsx')
    output_file = converter.convert()
    print(f"Conversion completed. Output saved to: {output_file}")

if __name__ == "__main__":
    main()