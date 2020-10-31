from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product

class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #    context = super(ProductListView, self).get_context_data(**kwargs)
    #    print(context)
    #    return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    ctx = {
        'object_list': queryset
    }
    return render(request, "products/list.html", ctx)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        #print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instace = Product.objects.get_by_id(pk)
        if instace is None:
            raise Http404("Product doesn't exist ")        

    # def get_queryset(self, *args, **kwargs):
    #    request = self.request
    #    pk = self.kwargs.get('pk')
    #    return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk)
    #instance = get_object_or_404(Product, pk=pk)
    #try:
    #    instance = Product.objects.get(id=pk)
    #except Product.DoesNotExist:
    #    print('no product here')
    #    raise Http404("Product doesn't exist ")
    #except:
    #    print("??")

    instace = Product.objects.get_by_id(pk)
    #print(instace)
    if instace is None:
        raise Http404("Product doesn't exist ")
    #qs = Product.objects.filter(id=pk)

    #if qs.exists() and qs.count == 1:
    #    instance = qs.first()
    #else:
    #    raise Http404("Product doesn't exist ")

    ctx = {
        'object': instance
    }
    return render(request, "products/detail.html", ctx)