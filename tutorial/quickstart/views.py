from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from quickstart.models import Device
from .serializers import DeviveModelSerializer
from rest_framework.viewsets import ModelViewSet
from django.views import View
from django.http import HttpResponse,JsonResponse


# 这里就是熟悉的django的views
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined') # 排序查询集
    serializer_class = UserSerializer    # 这是我们上面写的辣个类


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DRFDeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviveModelSerializer #指明该视图在进行序列化或反序列化时使用的序列化器
'''
class DRFView(View):
    def get(self, request):
        devices = Device.objects.all()
        ser = DeviveModelSerializer(devices, many=True)
        # 使用序列化器进行操作 注意  many=True
        return JsonResponse(ser.data, safe=False)
        # 在初始化json响应对象时，safe默认是True，非字典数据无法传输，设置为False，允许非字典数据传输
        # safe=False 非字典传输    将列表格式的数据(在前端叫做数组)也可转成json进行传输
        # 为True，会提示（In order to allow non-dict objects to be serialized set the safe parameter to False.）

    def post(self, request):
        # 获取数据
        json_byte = request.body
        json_str = json_byte.decode()
        json_dict = json.loads(json_str)

        # 将数据传入序列化器
        ser = DeviveModelSerializer(data=json_dict)
        # 校验
        ser.is_valid()  # 判断不通过直接报错，给前端返回400
        print(ser.is_valid())
        print(ser.errors)
        # 保存是模型对象
        ser.save()
        return JsonResponse(ser.data, safe=False)

'''