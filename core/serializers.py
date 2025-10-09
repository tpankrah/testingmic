from rest_framework import serializers
from .models import CheckType, Tenant, Monitor, Check, Oncall

class CheckTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckType
        fields = ['id', 
                  'name', 
                  'description']     

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 
                  'name', 
                  'description', 
                  'owner']

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = ['id', 
                  'name', 
                  'url', 
                  'type', 
                  'notes', 
                  'status', 
                  'tenant', 
                  'last_checked', 
                  'response', 
                  'response_code', 
                  'response_time', 
                  'created_at']

class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ['id', 
                  'monitor', 
                  'check_type', 
                  'tenant', 
                  'status', 
                  'response_code', 
                  'response_time', 
                  'checked_at']    

class OncallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oncall
        fields = ['id', 
                  'monitor', 
                  'tenant', 
                  'contact_name', 
                  'contact_info', 
                  'phone', 
                  'email', 
                  'priority']

