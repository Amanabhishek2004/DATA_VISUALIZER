from django.db import models

# Create your models here.
class CompanyData(models.Model):
    end_year = models.CharField(max_length=255,null = True)
    intensity = models.CharField(max_length =22 , blank = True,null = True)
    sector = models.CharField(max_length=255,null = True)
    topic = models.CharField(max_length=255,null = True)
    url = models.URLField(null = True)
    region = models.CharField(max_length=255,null = True)
    start_year = models.CharField(max_length = 225,null = True)
    impact = models.CharField(max_length=255,null = True)
    added = models.CharField(max_length = 225,null = True)
    published = models.CharField(max_length = 225,null = True)
    country = models.CharField(max_length=255,null = True)
    relevance = models.CharField(max_length = 22 , null =True)
    pestle = models.CharField(max_length=255,null = True)
    source = models.CharField(max_length=255,null = True)
    title = models.TextField(max_length = 300 , null = True)
    likelihood = models.CharField(max_length = 22 , null = True)
    insight = models.CharField(max_length = 120 , null = True )

    
    def __str__(self):
        return self.title