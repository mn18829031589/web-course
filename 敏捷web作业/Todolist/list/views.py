from django.shortcuts import render

# Create your views here.
from list.models import Content
from django.http import JsonResponse,HttpResponse
import time
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
#返回所有Todo任务
#创建一个新的Todo任务
#返回一个指定ID的Todo任务
#删除一个Todo任务
def home(request):
    pass
@csrf_exempt
def creatTodoList(request):

    if request.method == "POST":

        content = request.POST.get('content')
        if Content.objects.filter(content=content).count()>0:
            return HttpResponse('输入的内容已存在，请不要重复输入')
        else:
            try:
                Content.objects.create(content=content)
            except ObjectDoesNotExist:
                return HttpResponse('输入失败')
            else:
                return HttpResponse('输入成功')

    else:
        return HttpResponse('error!')

@csrf_exempt
def deleteTodoList(request):

    if request.method == 'POST':
        content = request.POST.get('content')
        contentdb=Content.objects.filter(content=content).first()
        if contentdb:
            try:
                contentdb.delete()
            except ObjectDoesNotExist:
                return HttpResponse('删除失败')
            else:
                return HttpResponse('删除成功')
        else:
            return HttpResponse('内容不存在')
    else:
        return HttpResponse('error!')
#返回一个指定id的TODO任务
@csrf_exempt
def returnIdTODO(request):

    if request.method == 'POST':
        contentId=request.POST.get('contentId')
        idDB=Content.objects.filter(cId=contentId).first()
        if idDB:
            try:
                content=Content.objects.get(cId=contentId).content
                data={
                    'id':contentId,
                     'content':content,
                     'createTime':time.strftime('%Y.%m.%d', time.localtime(time.time()))
                }
                return JsonResponse(data)
            except Exception as e:
                print(e)
                return HttpResponse('error!')
        else:
            return HttpResponse('指定的id不存在')
    else:
        return HttpResponse('error!')

#返回所有Todo任务
@csrf_exempt
def returnAll(request):
    try:
        if request.method == 'GET':
            content = Content.objects.values()
            return HttpResponse(content)
    except Exception as e:
        print(e)
        return HttpResponse('error!')

    else:
        return HttpResponse('error!')
