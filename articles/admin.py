from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article
from sorl.thumbnail.admin import AdminImageMixin

class MyModelAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'

admin.site.register(Article, SomeModelAdmin)


