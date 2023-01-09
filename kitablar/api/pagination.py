from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "sehife"



class LargePagination(PageNumberPagination):
    page_size = 20
    page_query_param = "sehife"