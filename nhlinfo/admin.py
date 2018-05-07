from django.contrib import admin
from .models import Conference, Division, Team, Goalie, Defense, Forward

# Register your models here.
admin.site.register(Conference)
admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Forward)
admin.site.register(Defense)
admin.site.register(Goalie)