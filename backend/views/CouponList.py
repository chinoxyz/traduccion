from django.shortcuts import render
from rest_framework.views import APIView



class CouponListView(APIView):
    
    def get(self,request):
        """
        input:
        code
        
        output:
        Success:
            OK
        Else:
            Error
        """
        
        context = {"couponlist":[]}
        
        return render(request, 'couponlist.html', context)
