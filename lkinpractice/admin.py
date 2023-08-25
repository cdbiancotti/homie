from django.contrib import admin
from lkinpractice.models import Lkin, LkinBusiness, GenericProfile


admin.site.register([Lkin, LkinBusiness, GenericProfile])
