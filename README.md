# Django Wiki Encyclopedia

A simple wiki encyclopedia web application built with Django that allows users to create, edit, search, and manage wiki entries using Markdown formatting.

## Features

- **View Wiki Entries**: Browse and read wiki entries with Markdown rendering
- **Create New Entries**: Add new wiki pages with title and Markdown content
- **Edit Existing Entries**: Modify existing wiki entries
- **Delete Entries**: Remove wiki entries with confirmation
- **Search Functionality**: Search for wiki entries by title
- **Random Page**: Discover content by visiting random wiki entries
- **Markdown Support**: All entries are written in Markdown and rendered as HTML

## Technologies Used

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, Bootstrap 4
- **Markdown Processing**: Python-markdown library
- **Styling**: Custom CSS with Bootstrap components

## Project Structure

```
wiki/
├── manage.py
├── encyclopedia/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── util.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   └── encyclopedia/
│   │       └── styles.css
│   └── templates/
│       └── encyclopedia/
│           ├── index.html
│           ├── layout.html
│           ├── entry.html
│           ├── create.html
│           ├── edit.html
│           ├── search_results.html
│           ├── delete_confirm.html
│           └── error.html
├── entries/
│   ├── CSS.md
│   ├── Django.md
│   ├── Git.md
│   ├── HTML.md
│   └── Python.md
└── wiki/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/django-wiki.git
   cd django-wiki
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django markdown
   ```

4. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000`

## Usage

### Viewing Entries
- Visit the home page to see a list of all wiki entries
- Click on any entry title to view its content

### Creating New Entries
- Click "Create New Page" in the sidebar
- Enter a title and content in Markdown format
- Click "Save" to create the entry

### Editing Entries
- Navigate to any wiki entry
- Click the "Edit" button at the bottom of the page
- Modify the content and click "Save Changes"

### Deleting Entries
- Navigate to any wiki entry
- Click the "Delete" button at the bottom of the page
- Confirm the deletion in the confirmation dialog

### Searching
- Use the search box in the sidebar
- Enter keywords to find matching entries
- Results show entries with titles containing the search term

### Random Page
- Click "Random Page" in the sidebar to visit a randomly selected entry

## File Structure Explanation

- **`views.py`**: Contains all the view functions handling different pages
- **`urls.py`**: URL routing configuration
- **`util.py`**: Utility functions for reading and writing entry files
- **`templates/`**: HTML templates for different pages
- **`static/`**: CSS and other static files
- **`entries/`**: Directory containing all wiki entries as Markdown files

## Key Features Implementation

### Markdown Processing
The application uses the `python-markdown` library to convert Markdown content to HTML:
```python
import markdown
md = markdown.Markdown()
html_content = md.convert(markdown_content)
```

### File-based Storage
Wiki entries are stored as individual `.md` files in the `entries/` directory, making them easy to manage and version control.

### Search Functionality
Search is implemented using Python's string matching to find entries containing the search query in their titles.

### Random Page Feature
Uses Python's `random.choice()` to select a random entry from the available entries list.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built as part of CS50's Web Programming with Python and JavaScript course
- Uses Django framework for web development
- Bootstrap for responsive design
- Python-markdown for Markdown processing

## Screenshots

### Home Page
The main page displaying all available wiki entries.

### Entry View
Individual wiki entry page with rendered Markdown content and edit/delete options.

### Create/Edit Pages
Forms for creating new entries or editing existing ones with large text areas for content.

### Search Results
Search functionality showing matching entries based on title keywords.

