from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import render

from products.models import Product

class SearchProductListView(ListView):
    template_name = "search/view.html"
    
    def get_context_data(self, *arg, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*arg, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET

        query = method_dict.get('q', None)
        #print(query)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
        
        '''
        __icontains  = field contains this
        __iexact    = field contains exact
        '''
    
