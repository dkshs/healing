from django.contrib.auth.models import User

from healing.doctors.models import Doctor


def validate(fields: list[str]) -> bool:
    return all(str(field).strip() != "" for field in fields)


def is_doctor(user: User) -> bool:
    return Doctor.objects.filter(user=user).exists()
