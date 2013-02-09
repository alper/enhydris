# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.http import require_POST
from django.template import RequestContext, loader
# from django.template.defaultfilters import slugify
# from django.forms import ModelForm
# from django.core.urlresolvers import reverse
# from django.db.models import Q

# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):
    t = loader.get_template('watersnake/index.html')
    
    c = RequestContext(request, {
    })

    return HttpResponse(t.render(c))
