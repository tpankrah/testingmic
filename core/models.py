from django.db import models

# Create your models here.


class CheckType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Monitor(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    last_checked = models.DateTimeField(auto_now=True)
    response = models.TextField(null=True, blank=True)
    response_code = models.IntegerField(null=True, blank=True)
    response_time = models.FloatField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Check(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    check_type = models.ForeignKey(CheckType, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    response_code = models.IntegerField(null=True, blank=True)
    response_time = models.FloatField(null=True, blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Check for {self.monitor.name} at {self.checked_at}"


class Oncall(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.contact_name} for {self.moniqr.name}"
    

