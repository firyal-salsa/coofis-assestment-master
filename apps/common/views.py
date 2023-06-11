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
        document.save()

        if document.current_reviewer != document.reviewers.last():
            # If it's not the last reviewer, assign the next reviewer
            document.assign_next_reviewer()
        else:
            # If it's the last reviewer, update the role to 'creator'
            document.role = 'creator'

        document.status = 'reviewed'
        document.save()

        # Render a success message or redirect to another page

    return render(request, 'review_document.html', {'document': document})


def assign_reviewer(document):
    # Assign the next reviewer to the document
    reviewers = document.reviewers.all()
    if not reviewers:
        # If there are no reviewers assigned yet, assign the first reviewer
        document.reviewers.add(User.objects.filter(role='reviewer').first())
    else:
        current_reviewer = document.current_reviewer
        if current_reviewer:
            # If there is a current reviewer, assign the next reviewer
            current_reviewer_index = reviewers.index(current_reviewer)
            if current_reviewer_index < len(reviewers) - 1:
                document.reviewers.set([reviewers[current_reviewer_index + 1]])
        else:
            # If there is no current reviewer, assign the first reviewer
            document.reviewers.set([reviewers[0]])

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
        document.save()

        if document.current_reviewer != document.reviewers.last():
            # If it's not the last reviewer, assign the next reviewer
            assign_reviewer(document)
        else:
            # If it's the last reviewer, update the role to 'creator'
            document.role = 'creator'

        document.status = 'reviewed'
        document.save()

        if document.current_reviewer != document.reviewers.last():
            # If it's not the last reviewer, assign the next reviewer
            assign_reviewer(document)
        else:
            # If it's the last reviewer, update the role to 'creator'
            document.role = 'creator'

        document.status = 'reviewed'
        document.save()

        # Render a success message or redirect to another page

    return render(request, 'review_document.html', {'document': document})
    

def assign_reviewer(document):
    # Assign the next reviewer to the document
    reviewers = document.reviewers.all()
    if not reviewers:
        # If there are no reviewers assigned yet, assign the first reviewer
        document.reviewers.add(User.objects.filter(role='reviewer').first())
    else:
        current_reviewer = document.current_reviewer
        if current_reviewer:
            # If there is a current reviewer, assign the next reviewer
            current_reviewer_index = reviewers.index(current_reviewer)
            if current_reviewer_index < len(reviewers) - 1:
                document.reviewers.set([reviewers[current_reviewer_index + 1]])
        else:
            # If there is no current reviewer, assign the first reviewer
            document.reviewers.set([reviewers[0]])