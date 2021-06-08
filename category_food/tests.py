from django.test import TestCase

from category_food.models import Company, Dish


class TestCompany(TestCase):

    def test_create_success(self):
        company_info = {
            'name': 'KFC',
            'image': 'media/company_image/IMG-20210209-WA0013.jpg',
            'description': '',
        }
        company = Company.objects.create(**company_info)
        self.assertEqual(company.name, company_info['name'])
        self.assertEqual(company.image, company_info['image'])
        self.assertEqual(company.description, company_info['description'])

    def test_create_fail(self):
        company_info = {
            'name': 'KFC',
            'image': 'media/company_image/IMG-20210209-WA0013.jpg',
            'description': 24,
        }
        with self.assertRaises(ValueError):
            company = Company.objects.create(**company_info)

    def test_update(self):
        company_info = {
            'name': 'KFC',
            'image': 'media/company_image/IMG-20210209-WA0013.jpg',
            'description': 24,
        }
        name = 'KFC'
        company = Company.objects.create(**company_info)
        company.name = name
        company.save()
        company.refresh_from_db()

    def test_delete(self):
        company_info = {
            'name': 'KFC',
            'image': 'media/company_image/IMG-20210209-WA0013.jpg',
            'description': 24,
        }
        company = Company.objects.create(**company_info)
        pk = company.pk
        company.delete()
        with self.assertRaises(Company.DoesNotExist):
            Company.objects.get(pk=pk)


class TestDishModel(TestCase):

    def test_create_success(self):
        dish_info = {
            'name': 'KFC',
            'image': 'media/dish_image/IMG-20210209-WA0014.jpg.jpg',
            'description': '',
            'category': '',
            'component': '',
        }
        dish = Dish.objects.create(**dish_info)
        self.assertEqual(dish.name, dish_info['name'])
        self.assertEqual(dish.image, dish_info['image'])
        self.assertEqual(dish.description, dish_info['description'])
        self.assertEqual(dish.category, dish_info['category'])
        self.assertEqual(dish.component, dish_info['component'])

    def test_create_fail(self):
        dish_info = {
            'name': 'KFC',
            'image': 'SEKA',
            'description': '',
            'category': '',
            'component': '',
        }
        with self.assertRaises(ValueError):
            dish = Dish.objects.create(**dish_info)

    def test_update(self):
        dish_info = {
            'name': 'KFC',
            'image': 'media/dish_image/media/dish_image/IMG-20210209-WA0014.jpg.jpg',
            'description': '',
            'category': '',
            'component': '',
        }
        name = 'KFC'
        dish = Dish.objects.create(**dish_info)
        dish.name = name
        dish.save()
        dish.refresh_from_db()

    def test_delete(self):
        dish_info = {
            'name': 'KFC',
            'image': 'media/dish_image/IMG-20210209-WA0014.jpg.jpg',
            'description': '',
            'category': '',
            'component': '',
        }
        company = Dish.objects.create(**dish_info)
        pk = company.pk
        company.delete()
        with self.assertRaises(Dish.DoesNotExist):
            Company.objects.get(pk=pk)