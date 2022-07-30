from email.mime import application
from django.db import models

# Create your models here.

# datacenter table
class DataCenter(models.Model):
    datacenter_name = models.CharField(null=False, blank=False, unique=True, max_length=500)

    def __str__(self):
        return self.datacenter_name
        

# Server table
class Server(models.Model):
    server_name = models.CharField(null=False, blank=False, max_length=500)
    datacenter = models.ForeignKey(DataCenter, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.server_name} - {self.datacenter}"


# application table
class Application(models.Model):
    app_name = models.CharField(null=False, blank=False, max_length=500)
    server = models.ForeignKey(Server, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.app_name} - {self.server}"


# action table
class Action(models.Model):
    action_name = models.CharField(null=False, blank=False, max_length=500)
    application = models.ForeignKey(Application, null=False, blank=False, on_delete=models.CASCADE)
