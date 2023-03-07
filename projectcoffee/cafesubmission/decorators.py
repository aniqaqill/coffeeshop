from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

def admin_required(view_func):
    decorated_view_func = staff_member_required(view_func)
    
    def wrap(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')
        return decorated_view_func(request, *args, **kwargs)
    
    return wrap
