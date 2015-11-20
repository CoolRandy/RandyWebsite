from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from polls.models import Poll

# index version1
# def index(request):
# 	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
# 	#output = ','.join([p.question for p in latest_poll_list])
# 	template = loader.get_template('polls/index.html')
# 	context = Context({
# 			'latest_poll_list': latest_poll_list,
# 		})
# 	return HttpResponse(template.render(context))

# index version2
def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	#output = ','.join([p.question for p in latest_poll_list])
	#template = loader.get_template('polls/index.html')
	context = Context({
			'latest_poll_list': latest_poll_list,
		})
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	# try:
	# 	poll = Poll.objects.get(pk=poll_id)
	# except Poll.DoesNotExist:
	# 	raise Http404
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
	return HttpResponse("You are looking at the result of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You are voting on poll %s." % poll_id)

