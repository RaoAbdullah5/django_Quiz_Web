from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
admin.site.site_header = _("Quizzy")  # Custom header name
admin.site.site_title = _("My Admin Panel")  # Custom title on browser tab
admin.site.index_title = _("Welcome to Admin Panel")  # Custom index title