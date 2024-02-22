import fitz
from PIL import Image

def pdf_to_images(pdf_path, output_folder):
    
    pdf_document = fitz.open(pdf_path)
    
    for page_number in range(pdf_document.page_count):
        
        page = pdf_document[page_number]
        
        pixmap = page.get_pixmap()
        
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        
        image_path = f"{output_folder}/page_{page_number + 1}.png"
        image.save(image_path)
        print(f"Page {page_number + 1} Converted and saved as {image_path}")
        
    pdf_document.close()
    
if __name__ == "__main__":
    pdf_path = "pdf/logo.pdf"
    output_folder = "output-image"
    
    pdf_to_images(pdf_path, output_folder)
        