from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AccountAdmin(UserAdmin):
    exclude = ('username',)
    list_display = ('full_name', 'email', 'phone_number',
                    'role', 'is_superuser', 'last_login')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('last_login',)

    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name',
                                      'full_name', 'email', 'password', 'role', 'phone_number')}),
        # ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'full_name', 'role', 'department', 'position', 'password1', 'password2'),
        }),
    )


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)

# Register your models here.
