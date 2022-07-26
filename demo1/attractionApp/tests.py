from decimal import Decimal
from unicodedata import name
from django.test import TestCase
from attractionApp.models import regionModels,cityModels,attractionModels,categoryModels

# Create your tests here.

class TestModels(TestCase):

    def setUp(self):
        self.region1 = regionModels.objects.create(
            regionName = "E",
            regionLikes = 10
        )
        self.region2 = regionModels.objects.create(
            regionName = "S",
            regionLikes = 10
        )
        
        self.city1 = cityModels.objects.create(
            cityName = "London",
            cityLikes = 30,
            cityRegion = self.region1
        )

        self.city2 = cityModels.objects.create(
            cityName = "Glasgow",
            cityLikes = 100,
            cityRegion = self.region2
        )
        self.category1 = categoryModels.objects.create(
            categoryName = "tourist",
            categoryLikes = 100 
        )

        self.acctrction1 = attractionModels.objects.create(
            attractionName = "London Eye",
            attractionLat = 51.503399,
            attractionLng = -0.119519,
            attractionContent = "here is london eyes",
            attractionPostcode = "SE1 7PB",
            attractionLikes = 10000,
            attractionCategory = self.category1,
            attractionCity = self.city1
        )
        
    def testRegion(self):
        regionE = regionModels.objects.get(regionName="E")
        self.assertEqual(regionE.regionName,'E')
        self.assertEqual(regionE.regionLikes,10)

    def testCity(self):
        london = cityModels.objects.get(cityName = "London")
        glasgow = cityModels.objects.get(cityName = "Glasgow")
        print(london.cityId)
        self.assertEqual(london.cityName,"London")
        self.assertEqual(london.cityRegion,self.region1)
        self.assertEqual(london.cityRegion.regionName,"E")

    def testAttraction(self):
        londonEye = attractionModels.objects.get(attractionName = "London Eye")
        print("london eye: "+ str(Decimal(londonEye.attractionLat).quantize(Decimal('0.000000'))))
        print(londonEye.attractionLng)
        self.assertEqual(londonEye.attractionLat,Decimal('51.503399'))
        self.assertEqual(londonEye.attractionCategory.categoryName,"tourist")

    
    
