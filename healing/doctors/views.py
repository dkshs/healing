from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from healing.utils.validate import is_doctor
from healing.utils.validate import validate

from .models import Doctor
from .models import Specialty


@login_required(login_url="sign_in")
def medical_registration(request):
    if request.method == "POST":
        if is_doctor(request.user):
            messages.error(request, "You are already a doctor")
            return redirect("medical_registration")
        crm = request.POST.get("crm") or ""
        mic = request.FILES.get("mic") or ""
        full_name = request.POST.get("full_name") or ""
        zip_code = request.POST.get("zip_code") or ""
        street = request.POST.get("street") or ""
        neighborhood = request.POST.get("neighborhood") or ""
        number = request.POST.get("number") or ""
        rg = request.FILES.get("rg") or ""
        image = request.FILES.get("image") or ""
        medical_specialty = request.POST.get("medical_specialty") or ""
        description = request.POST.get("description") or ""
        consultation_value = request.POST.get("consultation_value") or ""

        if not validate(
            [
                crm,
                mic,
                full_name,
                zip_code,
                street,
                neighborhood,
                number,
                rg,
                image,
                medical_specialty,
                consultation_value,
            ],
        ):
            messages.error(request, "Please fill in all fields")
            return redirect("medical_registration")

        try:
            Doctor.objects.create(
                crm=crm,
                medical_identity_card=mic,
                name=full_name,
                zip_code=zip_code,
                street=street,
                neighborhood=neighborhood,
                number=number,
                rg=rg,
                image=image,
                specialty=Specialty.objects.get(id=medical_specialty),
                description=description,
                consultation_value=consultation_value,
                user=request.user,
            )
            messages.success(request, "Doctor registered successfully")
        except Specialty.DoesNotExist:
            messages.error(request, "Specialty does not exist")
        except Exception as e:  # noqa: BLE001
            messages.error(request, f"Error registering. {e!s}")
        return redirect("medical_registration")
    specialties = Specialty.objects.all()
    return render(request, "medical_registration.html", {"specialties": specialties})
