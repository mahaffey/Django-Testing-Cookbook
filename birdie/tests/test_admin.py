import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer
from birdie import admin
from birdie import models
pytestmark = pytest.mark.django_db


class TestPostAdmin():
    def test_excerpt(self):
        site = AdminSite()
        post_admin = admin.PostAdmin(models.Post, site)

        obj = mixer.blend('birdie.Post', body='Hallo world')
        result = post_admin.excerpt(obj)

        assert result == 'Hallo', 'Should return first few characters'
