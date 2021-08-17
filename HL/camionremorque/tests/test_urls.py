from django.test import SimpleTestCase
from django.urls import reverse,resolve
from camionremorque.views import index,modifierCamion,loadMore


class TestUrls(SimpleTestCase):
    def test_camionremorque_url_is_resolved(self):
        url = reverse('camionremorque')
        self.assertEqual(resolve(url).func,index)
    
    def test_modifierCamion_url_is_resolved(self):
        url = reverse('modifierCamion')
        self.assertEqual(resolve(url).func,modifierCamion)
    
    def test_loadMore_url_is_resolved(self):
        url = reverse('loadMore',args=['matricule'])
        self.assertEqual(resolve(url).func,loadMore)