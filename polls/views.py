from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from polls.models import Poll

def index(request) :
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request,{
		'latest_poll_list': latest_poll_list
	})
	return HttpResponse(template.render(context))

def detail(request, poll_id):

	template = loader.get_template('polls/detail.html')
	try:
 		p = Poll.objects.get(id=poll_id)
 	except Poll.DoesNotExist:
 		raise Http404
 	#p = get_object_or_404(Poll, pk=poll_id)
	c = RequestContext(request, {
		'poll':p,
		})
	return HttpResponse(template.render(c))
	
def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)