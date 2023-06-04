from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from base.services import get_path_upload_avatar, validate_size_image
from django.core.validators import FileExtensionValidator


class UserManager(BaseUserManager):

  def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
    # if not email:
    #     raise ValueError('Users must have an email address')
    now = timezone.now()
    # email = self.normalize_email(email)
    user = self.model(
        username=username,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        registered_at=now, 
        last_login=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, username, password, **extra_fields):
    user=self._create_user(username, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    """Кастомная модель пользователя
    """
    username = models.CharField(max_length=150, unique=True, verbose_name='Логин')
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст', null=True, )
    email = models.CharField(max_length=50, null=True, )
    phone = models.CharField(max_length=50, verbose_name='Телефон', null=True, )
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name='Страна')
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name='Город')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='Время входа')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to=get_path_upload_avatar, 
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    @property
    def is_authenticated(self):
        """Аутентифицирован ли пользователь
        """
        return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-registered_at']
