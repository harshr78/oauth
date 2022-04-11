from functools import wraps
from django.http import HttpResponseRedirect

def authors_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        profile = request.user.get_profile()
        if profile.usertype == 'Author':
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap
