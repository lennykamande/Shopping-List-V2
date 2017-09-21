# tests.py

import unittest

from flask_testing import TestCase
from flask import url_for, abort

from app import create_app, db 
from app.models import User, Product

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='postgresql://postgres:2014@localhost/shopping_cart'
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test user
        user = User(username="admin", password="admin2016", email="admin@andela.com")

        # save users to database
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestModels(TestBase):

    def test_user_model(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(User.query.count(), 1)

    def test_product_model(self):
        """
        Test number of records in Department table
        """

        # create test department
        product = Product(name="Potatoes", description="A vegetable that is brown in color made for fries")

        # save department to database
        db.session.add(product)
        db.session.commit()

        self.assertEqual(Product.query.count(), 1)


class TestViews(TestBase):

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.register'))
        self.assertEqual(response.status_code, 200)


    def test_admin_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('dashboard.homepage')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)


if __name__ == '__main__':
    unittest.main()