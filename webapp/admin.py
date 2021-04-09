from django.contrib import admin
from .models import Member, Deceased, Contributions

admin.site.register(Member)
admin.site.register(Deceased)
admin.site.register(Contributions)
