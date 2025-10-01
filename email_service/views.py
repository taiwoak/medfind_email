from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

@csrf_exempt
def send_mail_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    data = json.loads(request.body)

    to_email = data.get("to")
    from_email = data.get("from") or settings.DEFAULT_FROM_EMAIL
    template = data.get("template")
    context = data.get("context", {})

    if not (to_email and template):
        return JsonResponse({"error": "Missing parameters"}, status=400)

    try:
        message = render_to_string(f"email_service/{template}.txt", context)
        subject = f"{context['name']} is Now Live on MedFind!"

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[to_email],
        )
        email.send()
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
