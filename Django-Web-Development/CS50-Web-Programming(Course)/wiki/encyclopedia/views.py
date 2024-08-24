from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
import markdown2
from django.urls import reverse_lazy
from . import util

class EntryListView(TemplateView):
    template_name = "encyclopedia/list_entries.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entries"] = util.list_entries()
        return context
    
class EntryDetail(View):
    template_name = "encyclopedia/view_entry.html"

    def get(self, request, *args, **kwargs):
        title = kwargs.get("title")
        entry = util.get_entry(title)
        entry = markdown2.markdown(entry)
        return render(request, self.template_name, {"entry": entry, "title": title})
    
class CreateEntry(View):
    template_name = 'encyclopedia/create_entry.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        entry = util.save_entry(title, content)
        return redirect('entry_detail', str=title)
        
