from django.shortcuts import render, get_object_or_404
from .models import Document

def create_document(request):
    if request.method == 'POST':
        # Process the form submission
        # Get the form data from the request

        # Create a new document object
        document = Document.objects.create(status='draft')
        # Save the document

        # Render a success message or redirect to another page

    return render(request, 'create_document.html')

def submit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if document.status != 'draft':
        # Render an error message or redirect to another page
        pass

    if request.method == 'POST':
        # Process the form submission
        # Get the form data from the request

        # Update the document status and save it
        document.status = 'submitted'
        document.save()

        # Render a success message or redirect to another page

    return render(request, 'submit_document.html', {'document': document})

def review_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if document.status != 'submitted':
        # Render an error message or redirect to another page
        pass

    if request.method == 'POST':
        # Process the form submission
        # Get the form data from the request

        # Update the document comments and status, and save it
        document.comments = '... reviewer comments ...'
        document.status = 'reviewed'
        document.save()

        # Render a success message or redirect to another page

    return render(request, 'review_document.html', {'document': document})
