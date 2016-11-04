from django.shortcuts import render, render_to_response

# Create your views here.
def index(request): 
        uid = request.session.get('user') 
        if uid is None: 
            #main landing page 
            #ipdb.set_trace() 
            return render_to_response('url_test/index.html')
