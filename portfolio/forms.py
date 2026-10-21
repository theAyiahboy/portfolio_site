from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=120, label="Full name")
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=40)
    subject = forms.ChoiceField(choices=[
        ("project", "I’d like you to build a project"),
        ("collaboration", "Collaboration opportunity"),
        ("internship", "Internship or work opportunity"),
        ("question", "Question about your work"),
        ("other", "Something else"),
    ])
    message = forms.CharField(max_length=5000, widget=forms.Textarea)
