from django.contrib import admin
from salon.models import Salon, Service, UserProfile, Reservation, Comments

# Register your models here.

admin.site.register(Salon)
admin.site.register(Service)
admin.site.register(UserProfile)
admin.site.register(Reservation)
admin.site.register(Comments)



