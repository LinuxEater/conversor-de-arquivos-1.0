# Conversor de Arquivos (Temporary name: Conversor de Moedas)

A Django project to convert files, currently focused on TXT to PDF conversion with Unicode font support.

## Features

- Upload TXT files and convert them to PDF.
- Supports Unicode characters using the DejaVu Sans font.
- Simple and clean UI for file upload.

## Getting Started

### Prerequisites

- Python 3.8+
- Django 5.x
- fpdf2

### Installation

1. Clone the repo:

```bash
git clone https://github.com/LinuxEater/conversor-de-moedas.git
cd conversor-de-moedas
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the development server:

```bash
python manage.py runserver
```

5. Access `http://127.0.0.1:8000` and use the file converter.

## Notes

- The DejaVu Sans font is included in the `fonts` folder.
- Feel free to rename the repository as you wish.

## License

MIT License
