import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assignment.settings")  # Replace with your project's settings module
django.setup()




from api.models import CompanyData
from data import *

for i in result:
    CompanyData.objects.create(**i)