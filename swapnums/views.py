from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# tuple unpacking
def num(request):
    return HttpResponse("
                                    a=10,b=20
                                c=a
                                a=b
                                b=c
                                print(a,b)


                                a=20
                                b=30
                                a,b=b,a
                                print(a,b)


                                a=10
                                b=20
                                a=a+b
                                b=a-b
                                a=a-b
                                print(a,b)

                                n1=3
                                n2=5
                                n1=n1*n2
                                n2=n1//n2
                                n1=n1//n2

                                print(n1,n2)
    ")