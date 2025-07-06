from django.shortcuts import render
import markdown
from . import util

def convert_markdown_to_html(title):
    content = util.get_entry(title)
    md = markdown.Markdown()
    if content == None:
        return None
    return md.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_markdown_to_html(title)
    if html_content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Entry not found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
def search(request):
    if request.method == "POST":
        query = request.POST.get('q')
        entries = util.list_entries()
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search_results.html", {
            "query": query,
            "entries": matching_entries
        })

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if not title or not content:
            return render(request, "encyclopedia/create.html", {
                "error": "Both title and content are required."
            })
        
        if util.get_entry(title):
            return render(request, "encyclopedia/create.html", {
                "error": "An entry with this title already exists."
            })
        
        util.save_entry(title, content)
        
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": convert_markdown_to_html(title)
        })
    else:
        return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": convert_markdown_to_html(title)
            })
    
    # GET request - show edit form
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Entry not found."
        })
    
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

def delete(request, title):
    if request.method == "POST":
        # Delete the entry file
        import os
        file_path = f"entries/{title}.md"
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Redirect to index
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "message": f"Entry '{title}' has been deleted."
        })
    
    # GET request - show confirmation
    return render(request, "encyclopedia/delete_confirm.html", {
        "title": title
    })

def random_page(request):
    import random
    entries = util.list_entries()
    if entries:
        random_entry = random.choice(entries)
        return render(request, "encyclopedia/entry.html", {
            "title": random_entry,
            "content": convert_markdown_to_html(random_entry)
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": [],
            "message": "No entries available."
        })