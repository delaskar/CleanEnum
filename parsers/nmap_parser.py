import logging
import re
from pathlib import Path
from core import exepcions

# Logging Settings
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)


class NmapParser:
    allowed_suffixes = [".txt", ".nmap", ".gnmap"]
    
    def __init__(self, filepath):
        self.filepath = filepath            
        self.nmap_output_lines = []         
        self.os = None
        self.nmap_ports = []                
        self.classified_ports = {}          


    def _load_file(self):
        if not isinstance(self.filepath, (str, Path)):
            raise exepcions.InvalidPathTypeError("The 'filepath' parameter must be a string or a Path object.")

        path = Path(self.filepath)
        
        if not path.exists():
            raise exepcions.FileNotFoundErrorCustom(f"File Not Found: {path}")
       
        if path.suffix not in self.allowed_suffixes:
            raise exepcions.FileFormatNotSupportedError(f"Illegal Format: {path.suffix}")
        
        try:
            with path.open('r', encoding='utf-8') as file:
                self.nmap_output_lines = file.readlines()
                logging.info(f"File uploaded successfully: {path.name}")
        except UnicodeDecodeError as e:
            raise exepcions.FileEncodingError("Encoding error: Could not decode as UTF-8.") from e
        
    
    def _extract_ports(self):
        for line in self.nmap_output_lines:
            regex = r"^(\d+)\/(\w+)\s+(\w+)\s+(\S+)(?:\s+(.*))?$"
            match = re.match(regex, line.strip())

            if match:
                port, proto, state, service, version = match.groups()
                print("PORT", port)
                print("PROTO", proto)
                print("STATE", state)
                print("SERVICE", service)
                print("VERSION", version) 
    
    def execution(self):
        self._load_file()
        self._extract_ports()
