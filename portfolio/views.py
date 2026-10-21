
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm


def home(request):
    return render(request, "portfolio/index.html")


def about(request):
    return render(request, "portfolio/about.html")


def certifications(request):
    return render(request, "portfolio/certifications.html")


def projects(request):
    return render(request, "portfolio/projects.html")


def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            recipient = getattr(settings, "CONTACT_EMAIL", "")
            if not recipient or not settings.EMAIL_HOST:
                messages.error(request, "Email delivery is not configured yet. Please email me directly for now.")
            else:
                name = form.cleaned_data["full_name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                subject = form.cleaned_data["subject"]
                message = form.cleaned_data["message"]
                subject_label = form.fields["subject"].choices
                subject_label = dict(subject_label)[subject]
                try:
                    send_mail(
                        subject=f"{subject_label} — message from {name}",
                        message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject_label}\n\nMessage:\n{message}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[recipient],
                        reply_to=[email],
                        fail_silently=False,
                    )
                except Exception:
                    messages.error(request, "Your message could not be sent right now. Please try again later.")
                else:
                    messages.success(request, "Thanks for reaching out. Your message has been sent.")
                    return redirect("contacts")
    else:
        form = ContactForm()

    return render(request, "portfolio/contacts.html", {"form": form})
