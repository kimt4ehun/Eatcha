from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
# Create your views here.
#
def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(settings.LOGIN_URL) # 회원가입에 성공하면,   LOGIN     페이지로 이동
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html', { 'form': form,
        })

