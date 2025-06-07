from parsers.nmap_parser import NmapParser
from core import exepcions

def main():
    # /home/mrinvictuslab/Python-Tools/Clean_Enum/App/TestNmapOutput/service_scan.txt
    print("[>] Enter FilePath:")
    filepath = input("").strip()
    
    nparser = NmapParser(filepath)
    
    try:    
        nparser.execution()
        print("[✔] File loaded. Ready to parse.")
    except exepcions.FileNotFoundErrorCustom as e:
        print(f"[☠️] {e}")
    except exepcions.FileFormatNotSupportedError as e:
        print(f"[☠️] {e}")
    except exepcions.InvalidPathTypeError as e:
        print(f"[☠️] {e}")
    except exepcions.FileEncodingError as e:
        print(f"[☠️] {e}")
    except Exception as e:
        print(f"[⚠️] Unexpected error: {e}")
    

if __name__ == "__main__":
    main()
