from rest_framework import serializers
from .models import CompanyData


class data_serializer(serializers.ModelSerializer):
   update_data = serializers.SerializerMethodField(read_only = True)
  
   class Meta:
      model = CompanyData
      fields = [
            'end_year',
            'intensity',
            "update_data",
            'sector',
            'topic',
            'url',
            'region',
            'start_year',
            'impact',
            'added',
            'published',
            'country',
            'relevance',
            'pestle',
            'source',
            'title',
            'likelihood',
            'insight',
      ]

      
   def get_update_data(self , obj):
         return f"http://127.0.0.1:8000/api/{obj.id}"