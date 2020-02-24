from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Device

    # User Group 应该是django自带的表结构，这里直接使用django自带的
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User  
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group 
        fields = ['url', 'name']

class DeviveModelSerializer(serializers.ModelSerializer):
    #image_code = serializers.CharField(max_length=4,min_length=4,allow_null=True)
    class Meta:
        model = Device
        # 所有字段都选中
        # fields = "__all__"
        fields = ['ip','dev_name','vendor','model','series']
        #exclude = ['is_delete']
        #read_only_fields = ['bread','bcomment']
        '''
        extra_kwargs = {
            'btitle':{
                'min_length':'10',
            }
        }
        '''