from django.apps import AppConfig

class DashboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import User
        registry.register(User)
        registry.register(self.get_model('Task'))
        registry.register(self.get_model('Supervisor'))