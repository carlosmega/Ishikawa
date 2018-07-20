from django.contrib import admin
from .models import Causa
from .models import Hallazgo
from .models import Agrupador
# Register your models here.

admin.site.register(Causa)
admin.site.register(Hallazgo)
admin.site.register(Agrupador)
