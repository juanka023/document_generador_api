# Document Generation API

The Document Generation API is a tool designed to generate text documents in different formats based on provided data inputs. It's a flexible solution that allows users to generate documents using both plain text input and existing DOCX files.

## Features

- Generate text documents in plain text and DOCX formats.
- Accept input data in JSON format or upload a DOCX file.
- Seamlessly combine template-based rendering and user-provided data.

## Installation

To use the Document Generation API locally, follow these steps:

1. Clone the repository:
```
git clone https://github.com/yourusername/document-generation-api.git
```

2. Navigate to the project directory:
```
cd document-generation-api
```

3. Create a virtual environment (recommended):
```
python3 -m venv venv
```

4. Activate the virtual environment:
- On macOS and Linux:
```
  source venv/bin/activate
```
- On Windows:
```
  venv\Scripts\activate
```

5. Install the project dependencies:
```
pip install -r requirements.txt
```

6. Start the local development server:
```
python manage.py runserver
```

7. The API should now be accessible at http://localhost:8000.

## Usage

### Using JSON Input

Send a POST request to the `api/v1/generate/` endpoint with JSON data:

```json
{
"nombre": "Juanito",
"placa": "1234",
"entidad": 123456
}
```

### Using TXT Input

Upload a .txt file using the input_file field in the POST request with the following format:
```
nombre: ....
placa: ....
entidad: ...
```
### Using DOCX Input

Upload a .docx file using the input_file field in the POST request with the following format:
```
nombre: ....
placa: ....
entidad: ...
```

## Dependencies

- Django: Web framework for building the API.
- Django Rest Framework: Toolkit for building Web APIs.
- python-docx: Library for working with DOCX files.

## Contributing
Contributions are welcome! If you find a bug or have a feature suggestion, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.