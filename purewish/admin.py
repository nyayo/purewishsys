from django.contrib import admin
from .models import Posts, Donor, Messages, Volunteer, Stuff, Gallery, MailManager, ProjectManager, Profile


admin.site.register(Posts)
admin.site.register(Donor)
admin.site.register(Messages)
admin.site.register(Volunteer)
admin.site.register(Stuff)
admin.site.register(MailManager)
admin.site.register(Gallery)
admin.site.register(ProjectManager)
admin.site.register(Profile)
