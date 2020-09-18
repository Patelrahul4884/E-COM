from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer


def validate_user_session(id,token):
    UserModel=get_user_model()
    
    try:
        user=UserModel.objects.all(pk=id)
        if user.session_token==token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':'please login!','code':'500'})
    
    if request.method=='POST':
        user_id=id
        transaction_id=request.POST['transaction_id']
        amount=request.POST['amount']
        products=request.POST['products']

        total_products=len(products.split(',')[:-1])
        UserModel=get_user_model()

        try:
            user=UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error':'user does not exist'})

        ordr=Order(user=user,
        product_name=products,
        total_products=total_products,
        transaction_id=transaction_id,
        total_amount=amount)
        ordr.save()
        return JsonResponse({'error':False,
                            'success':True,
                            'message':'order placed successfully'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all().order_by('id')
    serializer_class=OrderSerializer