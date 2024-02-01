from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect('')
        # else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

# def is_judge(user):
#     return user.is_authenticated and user.is_judge

# def judge_required(view_func):
#     decorated_view_func = user_passes_test(is_judge, login_url='judge_login')
#     return decorated_view_func(view_func)

def judge_required(view_func):
    return view_func

def is_participant(user):
    return user.is_authenticated and user.is_participant

def participant_required(view_func):
    decorated_view_func = user_passes_test(is_participant, login_url='participant_login')
    return decorated_view_func(view_func)
