from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

def main(request):
	return render(request, 'web/main.html')

def menu_1(request, page):
	return render(request, 'web/menu_1.html', {'page':page})

def menu_2(request, page):
	return render(request, 'web/menu_2.html', {'page':page})

def menu_3(request):
	result_posts_all = Result_post.objects.all().order_by('-id')
	page_number = int(request.GET.get('p', 1))
	pagenator = Paginator(result_posts_all, 11)
	result_posts = pagenator.get_page(page_number)
	return render(request, 'web/menu_3.html', {'result_posts':result_posts})

def menu_4(request):
	return render(request, 'web/menu_4.html')

def menu_5(request):
	return render(request, 'web/menu_5.html')

def menu_6(request, page):
	if page == 'notice':
		notice_posts_all = Notice_post.objects.all().order_by('-id')
		page_number = int(request.GET.get('p', 1))
		pagenator = Paginator(notice_posts_all, 11)
		notice_posts = pagenator.get_page(page_number)
		return render(request, 'web/menu_6.html', {'page':page,'notice_posts':notice_posts})

	elif page == 'information':
		pass

def detail_notice(request, page, notice_post_pk):
	if page == 'notice':
		notice_post = get_object_or_404(Notice_post, pk=notice_post_pk)
		return render(request, 'web/detail_notice.html', {'notice_post':notice_post})

	else:
		pass

def detail_result(request, result_post_pk):
	result_post = get_object_or_404(Result_post, pk=result_post_pk)
	return render(request, 'web/detail_result.html', {'result_post':result_post})
