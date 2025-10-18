from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('email', 'first_name', 'last_name','is_staff', 'is_active')
  search_fields = ('email', 'first_name', 'last_ name')
  list_filter = ('is_staff', 'is_active')
  ordering = ('email',)

  fieldets = (
    (None, {
      'fields': ('email', 'password')
    }),
    ('Personal info', {
      'fields': ('first_name', 'last_ name', 'middle_name', 'city', 'street', 'house_number', 'apartment_number', 'postal_code')
    }),
    ('Permissions', {
      'fields': ('is_staff', 'is_active', 'is_superuser')
    }),
  )

  add_fieldsets = (
    (None, {
      'classes': ('wide'),
      'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')
    })
  )

  def get_form(self, request, obj = None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    if obj:
      form.base_fields['password'].widget.attrs['readonly'] = True
    return form


