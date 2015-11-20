from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context

from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("Hello World")

# def curr_datetime(request):
# 	now = datetime.datetime.now()
# 	#html = "<html><body>It is now %s.</body></html>" % now
# 	t = get_template('curr_datetime.html')
# 	html = t.render(Context({'curr_date': now}))
# 	return HttpResponse(html)

# use render_to_response
# def curr_datetime(request):
# 	now = datetime.datetime.now()
# 	return render_to_response('curr_datetime.html', {'curr_date': now})

# use locals
def curr_datetime(request):
	curr_date = datetime.datetime.now()
	return render_to_response('curr_datetime.html', locals())

# def hours_ahead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#     return HttpResponse(html)

# use locals and base.html
def hours_ahead(request, hour_offset):
    try:
        hour_offset = int(hour_offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html', locals())
