

from django.http import response
from django.test.testcases import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from camionremorque.models import Camion, Remorque



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.camionremorque = reverse('camionremorque')
        self.modifierCamion = reverse('modifierCamion')
        self.loadMore = reverse('loadMore', args=['matriculation'])
        self.remorque = Remorque.objects.create(matriculation='00002-891-22')
        self.matriculation = Camion.objects.create(id=1,
                                                   matriculation='00014-508-22',
                                                   remorque=self.remorque,
                                                   designation='test')

    def test_index_GET(self):

        response = self.client.get(self.camionremorque)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'camionremorque/index.html')

    def test_modifierCamion_GET(self):

        response = self.client.get(self.modifierCamion)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'camionremorque/modifier_camion.html')

    def test_loadMore_GET(self):
        response = self.client.get(self.loadMore)
        self.assertEqual(response.status_code, 200)

    def test_modifierCamion_POST_Existiong_remorque(self):
        response = self.client.post(self.modifierCamion, {
            "validation-select2": "1",
            "remorque": "00002-891-22"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.matriculation.remorque.matriculation, "00002-891-22")

    def test_modifierCamion_POST_none_Existiong_remorque(self):
        response = self.client.post(self.modifierCamion, {
            "validation-select2": "1",
            "remorque": "2202433"
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Camion.objects.get(id=1).remorque.matriculation, "2202433")

    def test_modifierCamion_POST_no_data(self):
        response = self.client.post(self.modifierCamion)

        self.assertEqual(response.status_code, 404)
        self.assertNotEquals(
            Camion.objects.get(id=1).remorque.matriculation, "2202433")
