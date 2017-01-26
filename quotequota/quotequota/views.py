from django.shortcuts import render, redirect, get_object_or_404
from .models import Quote

def random_quote(request):
    return redirect(Quote.objects.order_by('?')[0])

def render_quote(request, ident):
    quote = get_object_or_404(Quote, pk=int(ident))
    return render(request, "quote_page.html", dict(quote=quote))
