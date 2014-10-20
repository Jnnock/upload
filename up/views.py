from django.http import HttpResponse
from django.shortcuts import render
from up.models import Database
from django.utils import timezone
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
import os

def index(request):
	try:
		user=request.POST['user']
		intro=request.POST['intro']
		if 'files' in request.FILES:
			filename=request.FILES['files'].name
			dirs ='templates/files/'+filename
			content = request.FILES['files'].read()
			if os.path.isfile(dirs):
				os.remove(dirs) 
			fp=open(dirs, 'wb')
			fp.write(content)
			fp.flush()
			fp.close()
		else:
			f=None
		result=Database(user=user,introduction=intro,files=filename,time=timezone.now())
		result.save()
		if result:
			return render(request,'up/index.html',{'result':'Success !'})
		else:
			return render(request,'up/index.html',{'result':'Failed !'})
	except:
		return render(request,'up/index.html')

def list(request):
	limit = 18 
	data=Database.objects.all().order_by('-time')
	paginator = Paginator(data, limit) 
	page = request.GET.get('page')
	try:
	    topics = paginator.page(page)
	except PageNotAnInteger: 
	    topics = paginator.page(1) 
	except EmptyPage: 
		topics = paginator.page(paginator.num_pages)
	return render(request,'up/list.html',{'content':topics})

def search(request):
	try:
		key=request.POST['search']
		limit = 3 
		result=Database.objects.filter(files__contains=key)
		paginator = Paginator(result, limit) 
		page = request.GET.get('page')
		try:
		    topics = paginator.page(page)
		except PageNotAnInteger: 
		    topics = paginator.page(1) 
		except EmptyPage: 
			topics = paginator.page(paginator.num_pages)
		#result=Database.objects.filter(user__contains=user)
		return render(request,'up/search.html',{'result':topics})
	except:
		return render(request,'up/search.html')
