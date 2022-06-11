from django.apps import AppConfig


class BlogConfig(AppConfig):  # this name and path we need to provide there at installed app section
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
