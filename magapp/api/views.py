from rest_framework.viewsets import ModelViewSet
from magapp.models import Product
from .serializers import ProductReadSerializer, ProductCreateSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer
    serializer_classes = {
        'list': ProductReadSerializer,
        'retrieve': ProductReadSerializer,
        'default': ProductCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,self.serializer_classes.get('default'))