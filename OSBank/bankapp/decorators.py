from django.shortcuts import redirect

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            print('user is loged-In')
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


