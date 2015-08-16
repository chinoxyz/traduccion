from django.shortcuts import render
from rest_framework.views import APIView


class CreateView(APIView):
    follow = '/'
    def get(self, request):
        context = {}#'form': LoginForm()}
        return render(request, 'user/login.html', context)
    def post(self, request):
        """form = LoginForm(request.data)
        if form.is_valid():
            login_data = form.cleaned_data
            user = authenticate(username=login_data['username'], password=login_data['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(self.follow)
            else:
                form.add_error(None, 'The username or password you entered are invalid.')"""
        context = {}#'form': form}
        return render(request, 'user/login.html', context)