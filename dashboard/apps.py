from django.apps import AppConfig

class DashboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import User, Group
        registry.register(User)
        registry.register(self.get_model('Application'))
        registry.register(self.get_model('UserCity'))
        registry.register(self.get_model('City'))
        
        
        registry.register(self.get_model('Job'))
        registry.register(Group)