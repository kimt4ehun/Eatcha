from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
# Create your views here.
#
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(settings.LOGIN_URL) # 회원가입에 성공하면,   LOGIN     페이지로 이동
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', { 'form': form,
        })

