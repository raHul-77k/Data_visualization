from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Data
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer

def index(request):
    year_filter = request.GET.get('year')  # Get the year filter parameter from the URL
    topic_filter = request.GET.get('topic')
    region_filter = request.GET.get('region')
    datas = Data.objects.all()

    if year_filter:
        datas = datas.filter(start_year=year_filter)  # Apply year filter if provided
    
    if topic_filter:
        datas = datas.filter(topic=topic_filter)  # Apply topic filter if provided

    if region_filter:
        datas = datas.filter(region=region_filter)  # Apply region filter if provided
    
    distinct_years = datas.order_by('start_year').values_list('start_year', flat=True).distinct()
    distinct_topics = datas.order_by('topic').values_list('topic', flat=True).distinct()
    distinct_region = datas.order_by('region').values_list('region', flat=True).distinct()

    paginator = Paginator(datas, 30)  # Show 30 objects per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    chart_data = []
    for item in page_obj:
        chart_data.append({
            'start_year': item.start_year,
            'Intensity': item.intensity,
            'Likelihood': item.likelihood,
            'Relevance': item.relevance,
            'Country': item.country,
            'Topics': item.topic,
            'Region': item.region
        })

    context = {
        'chart_data': chart_data,
        'page_obj': page_obj,
        'selected_year': year_filter,
        'selected_topic': topic_filter,
        'selected_region': region_filter,
        'years': distinct_years,
        'topics': distinct_topics,
        'regions': distinct_region
    }
    return render(request, 'templates/index.html', context)


@api_view(['GET'])
def data_api(request):
    year_filter = request.GET.get('year')
    topic_filter = request.GET.get('topic')
    region_filter = request.GET.get('region')
    datas = Data.objects.all()

    if year_filter:
        datas = datas.filter(start_year=year_filter)

    if topic_filter:
        datas = datas.filter(topic=topic_filter)

    if region_filter:
        datas = datas.filter(region=region_filter)

    serializer = DataSerializer(datas, many=True)
    return Response(serializer.data)