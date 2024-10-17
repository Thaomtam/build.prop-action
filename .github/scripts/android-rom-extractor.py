#!/usr/bin/env python3

import os
import zipfile
import sys

def extract_files(zip_file, extracted_files):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for file in extracted_files:
            if any(file in name for name in zip_ref.namelist()):
                print(f"Extracting {file} from {zip_file}...")
                for name in zip_ref.namelist():
                    if file in name:
                        zip_ref.extract(name, os.getcwd())
            else:
                print(f"File {file} not found in {zip_file}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: android-rom-extractor.py <zip_file>")
        sys.exit(1)
    
    zip_file = sys.argv[1]
    extracted_files = os.getenv("EXTRACTED_FILES", "vendor.img").split(',')
    
    if not os.path.isfile(zip_file):
        print(f"Error: File {zip_file} not found.")
        sys.exit(1)

    extract_files(zip_file, extracted_files)
    print(f"Extraction completed for {extracted_files}.")
