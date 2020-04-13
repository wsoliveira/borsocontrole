from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import bc_sector


class TestSector(TestCase):
    def setUp(self):
        # Set up data for the whole TestCase
        bc_sector.objects.create(name="sector1", description='desc. sector1').save()
        bc_sector.objects.create(name="sector2", description='desc. sector2').save()
        self.username = 'dummy@dummy.com'
        self.password = 'Dummy@123'
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()
        self.c = Client()
        user_login = self.c.login(username=self.username, password=self.password)
        self.assertTrue(user_login)

    def testFormGet(self):
        response = self.c.get(reverse('sector_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name='base.html')
        self.assertTemplateUsed(response=response, template_name='navbar.html')

    def testFormPost(self):
        post_data = {
            'name': 'sector3',
            'description': 'desc. sector3',
        }
        response = self.c.post('/companies/sector/new/', post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/companies/sector/list/')
        ret = bc_sector.objects.get(name='sector3')
        self.assertTrue(ret)

    def testFormUpdate(self):
        post_data = {
            'name': 'sector4',
            'description': 'desc. sector3',
        }
        ret = bc_sector.objects.get(name='sector1')
        response = self.c.post(f'/companies/sector/update/{ret.id}/', post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/companies/sector/list/')
        ret = bc_sector.objects.get(name='sector4')
        self.assertTrue(ret)

    def testFormDelete(self):
        ret = bc_sector.objects.get(name='sector2')
        response = self.c.post(f'/companies/sector/delete/{ret.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/companies/sector/list/')
        ret = bc_sector.objects.get(name='sector2', is_active=False)
        self.assertTrue(ret)



