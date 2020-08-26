from rest_framework import viewsets
from .serializers import OrderSerializer
from onlineorder.models import Order
from rest_framework import viewsets,permissions

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    #queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.orders.all()

    def perform_create(self,serializer):
        serializer.save(contractor=self.request.user)

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            data={
                "status":201,
                "message":"Order successfully created",
                "data":serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )