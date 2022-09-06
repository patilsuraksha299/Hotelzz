from django.shortcuts import render
from django.http import JsonResponse

from home.models import Emenities, Hotels
# Create your views here.
def home(request):
    emenities=Emenities.objects.all()
    context={
        "emenities":emenities
    }

    return render(request,'home.html',context)


def api_hotels(request):
    hotels_objs=Hotels.objects.all()

    price=request.GET.get('price')
    # print(price)

    emenities=request.GET.get('emenities')
    if emenities:
        emenities=emenities.split(',')
        # print(emenities)
        em=[]
        for e in emenities:
            try:    
                em.append(int(e))
            except Exception as e:
                pass

        hotels_objs=hotels_objs.filter(emenities__in=em).distinct()
        # print(em)

    if price:
        hotels_objs=hotels_objs.filter(price__lte=price)



    payload=[]
    for hotel_obj in hotels_objs:
        result={}
        result['hotel_name']=hotel_obj.hotel_name
        result['hotel_description']=hotel_obj.hotel_descripiton
        result['hotel_image']=hotel_obj.hotel_image
        result['hotel_price']=hotel_obj.price
        payload.append(result)
    return JsonResponse(payload,safe=False)