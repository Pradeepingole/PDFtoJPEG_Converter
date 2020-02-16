from pdf2image import convert_from_path
import PyPDF2, io
import os

path = input("Copy and paste full path to folder: ")

assert os.path.exists(path), "No file found at: "+str(path)

page_count = 1

os.chdir(path)                 # Changes directory to path with pdf files
for file in os.listdir(path):  # Iterates over different files
    if os.path.splitext(os.path.basename(file))[1] == '.pdf':   # Checks if file is pdf      
    
        pdf_reader = PyPDF2.PdfFileReader(file)                 # Uses PyPDF2 module to read files and get number of pages
        num_of_pages = pdf_reader.numPages
    
        jpeg = convert_from_path(file, output_folder=path,last_page=num_of_pages, first_page=0)     # Converts each page in the PDF to a jpeg

        for page in jpeg:                                   
            out_file = os.path.splitext(os.path.basename(file))[0]+str(page_count)+'.jpeg'          # Creates output file for each page
            page.save(os.path.join(out_file),'JPEG')        # saves page, increments page count                      
            page_count+=1

for file in os.listdir(path):                           # for loop to get rid of the .ppm files generated as a byproduct of conversion
    if os.path.splitext(os.path.basename(file))[1] == '.ppm':
        os.remove(file)     



input("\nAll pdf files changed to jpeg. Press enter to continue...")
