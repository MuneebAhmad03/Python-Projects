import os
from pypdf import PdfWriter



merger = PdfWriter()
pdfs = []

print("Enter the filename you want to merge one by one. Type done when you are finished")

while True:
    name = input(f"Enter the file name {len(pdfs) +1} or (done)\n")

    if name.lower() == "done":
        break
    if not name.endswith(".pdf"):
        name += ".pdf"

    if os.path.exists(name):
        pdfs.append(name)
        print(f"Added : {name}")

    else:
        print(f"Error: Could not found the file name {name}.\nPlease write the correct name.")

if pdfs:
    print(f"Merging {len(pdfs)} files")

    for pdf in pdfs:
        merger.append(pdf)

    output_name = f"merge-file.pdf"
    merger.write(output_name)
    merger.close()

    print(f"Success Files are merged in {output_name}")

else:
    print("No pdf file were added. Exiting...")
