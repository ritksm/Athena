#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jack River'


from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site
from django.conf import settings


class Command(BaseCommand):
    help = 'Create default Site for user'

    def handle(self, *args, **options):
        try:
            # clean all existing sites
            Site.objects.all().delete()

            site = Site.objects.create(pk=settings.SITE_ID, name='Default Site', domain='localhost')
            if not site:
                raise CommandError()
        except Exception as e:
            self.stderr.write('Site creation failed, please try again.')
            self.stderr.write('Exception: ', e)