# PDF to Images Converter

This Python script converts each page of a PDF document into separate image files. It utilizes the PyMuPDF library (`fitz`) to handle PDF operations and the Python Imaging Library (`PIL`) for image processing.

## Usage

### Prerequisites

Make sure you have the required dependencies installed:

```bash
pip install PyMuPDF pillow
```

### Running the Script

```bash
python pdf_to_images.py
```

Make sure to customize the `pdf_path` and `output_folder` variables in the script according to your PDF file location and desired output folder.

## Example

```python
if __name__ == "__main__":
    pdf_path = "path/to/your/pdf/document.pdf"
    output_folder = "path/to/your/output/folder"
    
    pdf_to_images(pdf_path, output_folder)
```

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.