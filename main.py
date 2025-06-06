from parsers.nmap_parser import NmapParser


if __name__ == "__main__":
    # /home/mrinvictuslab/Python-Tools/Clean_Enum/App/TestNmapOutput/service_scan.txt
    userfile = input("[>] Enter The File Path: ")
    nparser = NmapParser(userfile)
    result = nparser._load_file()
    print(result)
