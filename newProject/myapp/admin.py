from django.contrib import admin
from .models import Menu
from .models import MenuCategory
from .models import Loggeṛ
from .models import Teacher
from .models import Subject
from .models import Person

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Loggeṛ)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Person)