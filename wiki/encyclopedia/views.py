from django.shortcuts import render, redirect
from django import forms
import markdown2
import random
from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control'}))

def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"The requested page '{title}' was not found."
            }, status=404)

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(content)
    })

def search(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()
    
    if query in entries:
        return redirect("entry", title=query)
    
    results = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "results": results
    })

def random_page(request):
    entries = util.list_entries()

    if not entries:
        return redirect("index")
    
    random_page = random.choice(entries)
    return redirect("entry", title=random_page)

def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].strip()
            content = form.cleaned_data["content"]

            if util.get_entry(title):
                return render(request, "encyclopedia/new_page.html", {
                    "form": form,
                    "error": "An entry with this title already exists."
                })

            util.save_entry(title, content)
            return redirect("entry", title=title)

    return render(request, "encyclopedia/new_page.html", {"form": NewPageForm()})