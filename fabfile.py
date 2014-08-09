#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jack River'

import os
import sys
BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, BASE_DIR)

from fabric.api import *
from fabric.context_managers import shell_env


def init_all(environment='Prod'):
    """ initialize project

    :param environment: DJANGO_CONFIGURATION settings, Prod or Dev
    """
    if not environment:
        sys.stderr.write('\nYou have to define the runtime environment: Prod/Dev\n')
    with lcd(BASE_DIR):
        with shell_env(DJANGO_CONFIGURATION=environment):
            # syncdb and migrate
            local('python manage.py syncdb')
            local('python manage.py migrate')
            sys.stdout.write('\nDatabase synced, initializing default site for you now.\n')

            # create default site
            local('python manage.py create_default_site')
            sys.stdout.write('\nSite created, please change domain name to yours.\n')
            sys.stdout.write(
                'If you want to use social account login, please add a Social App for each OAuth based provider.\n'
            )