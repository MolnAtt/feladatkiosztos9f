from django.contrib import admin
from .models import Tanulo
from .models import Tetel
from .models import Valasztott

# Register your models here.

admin.site.register(Tanulo)
admin.site.register(Tetel)
admin.site.register(Valasztott)
