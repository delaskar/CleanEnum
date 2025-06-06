from pathlib import Path


class NmapParser:
    def __init__(self, filepath):
        self.filepath = filepath            
        self.allowed_suffixes = [".txt", ".nmap", ".gnmap"]
        self.nmap_output_lines = []         
        self.os = None
        self.nmap_ports = []                
        self.classified_ports = {}          


    def _load_file(self):
        if not isinstance(self.filepath, (str, Path)):
            raise ValueError("[❌] Invalid Entry: The input should be a str or an os path.")

        path = Path(self.filepath)
        
        if path.exists():
            print("[😎] File Found!")
            if path.suffix in self.allowed_suffixes:
                print(f"[👌] Valid File Format: {path.suffix}")
                try:
                    with open(path, 'r', encoding="utf-8") as file:
                        lines = file.readlines()
                        self.nmap_output_lines = lines
                        print("[😎] File uploaded successfully!")
                        return True
                except UnicodeDecodeError:
                    return "Error: 'UTF-8' codec can't decode byte."
            else:
                return "[☠️] Invalid File Format!"
        else:
            return "[☠️] File NOT Found"

