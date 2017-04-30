#!/usr/bin/env python  
# _#_ coding:utf-8 _*_  
from rest_framework import serializers
from OpsManage.models import *
from django.contrib.auth.models import Group,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','last_login','is_superuser','username',
                  'first_name','last_name','email','is_staff',
                  'is_active','date_joined')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Assets
        fields = ('id','service_name')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')
          
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone_Assets
        fields = ('id','zone_name')         

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line_Assets
        fields = ('id','line_name')          

class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid_Assets
        fields = ('id','raid_name')         
        
# class AssetStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assets_Satus
#         fields = ('id','status_name') 
        
class CronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cron_Config
        fields = ('id','cron_minute','cron_hour','cron_day',
                  'cron_week','cron_month','cron_user',
                  'cron_name','cron_desc','cron_server',
                  'cron_command','cron_script','cron_status') 
        

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('id','assets_type','name','sn','buy_time','expire_date',
                  'buy_user','management_ip','manufacturer','provider',
                  'model','status','put_zone','group','business')  

        

class ProjectConfigSerializer(serializers.ModelSerializer): 
    project_number = serializers.StringRelatedField(many=True)#ProjectNumberSerializer(required=False)
    class Meta:
        model = Project_Config
        fields = ('id','project_env','project_name','project_local_command',
                  'project_repo_dir','project_dir','project_exclude',
                  'project_address','project_repertory','project_status',
                  'project_remote_command','project_number')   

class AnbiblePlaybookSerializer(serializers.ModelSerializer): 
    server_number = serializers.StringRelatedField(many=True)#ProjectNumberSerializer(required=False)
    class Meta:
        model =  Ansible_Playbook
        fields = ('id','playbook_name','playbook_desc','playbook_vars',
                  'playbook_uuid','playbook_file','playbook_auth_group',
                  'playbook_auth_user','server_number')   

class ServerSerializer(serializers.ModelSerializer): 
    assets = AssetsSerializer(required=False)
#     keyfile = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = Server_Assets
        fields = ('id','ip','hostname','username','port','passwd',
                  'line','cpu','cpu_number','vcpu_number',
                  'cpu_core','disk_total','ram_total','kernel',
                  'selinux','swap','raid','system','assets') 

    def create(self, data):
        if(data.get('assets')):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets;
        server = Server_Assets.objects.create(**data)  
        return server 
           
         
class NetworkSerializer(serializers.ModelSerializer): 
    assets = AssetsSerializer(required=False)
    class Meta:
        model = Network_Assets
        fields = ('id','ip','bandwidth','port_number','firmware',
                  'cpu','stone','configure_detail','assets')    
    def create(self, data):
        if(data.get('assets')):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets;
        server = Network_Assets.objects.create(**data)  
        return server   
    
class DeployOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Order
        fields = ('id','order_project','order_subject','order_content',
                  'order_branch','order_comid','order_tag','order_audit',
                  'order_status','order_level','order_cancel','create_time',
                  'order_user')     