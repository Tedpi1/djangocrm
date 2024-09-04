from django.test import TestCase
from django.shortcuts import reverse
class LandingPageView(TestCase):
    def test_get(self):
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')
        #test if the right template is returned
        
        print(response.status_code)
# Create your tests here.
