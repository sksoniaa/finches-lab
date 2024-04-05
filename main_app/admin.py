from django.contrib import admin
# add Feeding to the import
from .models import Finch, Feeding, Toy

admin.site.register(Finch)
# register the new Feeding Model 
admin.site.register(Feeding)
admin.site.register(Toy)