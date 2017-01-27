from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
	if request.method == 'POST':
		 User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		 return render(request, 'accounts/signup.html')
	else:

			return render(request, 'accounts/signup.html')