from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, role, full_name=None, phone_number="Not Set"):

        if not email:
            raise ValueError("Users must have email address")

        if full_name is None:
            user = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                full_name=first_name + " " + last_name,
                role=role,
                phone_number=phone_number,
                password=password
            )
        else:
            user = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                full_name=full_name,
                role=role,
                phone_number=phone_number,
                password=password
            )

        if (role == 1 or role.role_name == 'Program Manager'):
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_active = True
            user.is_staff = False
            user.is_superuser = False

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, role, position, full_name=None, phone_number="Not Set", department="Not Set"):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            full_name=first_name + " " + last_name,
            role=Role.objects.get(id=role),
            phone_number=phone_number,
            department=department,
            position=position,
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_doctor = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=200, default="Not Set")
    last_name = models.CharField(max_length=200, default="Not Set")
    full_name = models.CharField(max_length=200, default="Not Set")
    phone_number = models.CharField(max_length=12, default="Not Set")
    department = models.ForeignKey("account.Department", on_delete=models.CASCADE)
    position = models.CharField(max_length=200, default="Not Set")
    role = models.ForeignKey("account.Role", on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    objects = AccountManager()

    def __str__(self):
        return self.email

class Role(models.Model):
    role_name = models.CharField(max_length=20)

    def __str__(self):
        return self.role_name

class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name