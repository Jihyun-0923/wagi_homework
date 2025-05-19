from django.shortcuts import render, redirect
from .forms import RegisterForm  # user/forms.py에 RegisterForm 정의되어 있어야 함!

# 회원가입 뷰
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # 사용자 생성
            return redirect('user:login')  # 회원가입 후 로그인 페이지로 이동
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})