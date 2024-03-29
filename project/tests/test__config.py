# project/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from project.server import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'] == True)
        self.assertFalse(current_app == None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'mariadb+mariadbconnector://root@localhost:3306/flask_jwt_auth'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'mariadb+mariadbconnector://root@localhost:3306/flask_jwt_auth_test'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] == False)


if __name__ == '__main__':
    unittest.main()
