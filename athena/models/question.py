#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jack River'

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Tag(models.Model):
    """ Tag model
    """

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    creator = models.ForeignKey(User, verbose_name=_('Creator'))
    create_time = models.DateTimeField(verbose_name=_('Create Time'),
                                       auto_now_add=True)

    class Meta(object):
        app_label = 'athena'
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Question(models.Model):
    """ Question model
    """

    title = models.CharField(max_length=255, verbose_name=_('Title'))
    content = models.TextField(verbose_name=_('Content'))
    questioner = models.ForeignKey(User, verbose_name=_('Questioner'))
    vote_up = models.IntegerField(verbose_name=_('Vote Up'), default=0)
    vote_down = models.IntegerField(verbose_name=_('Vote Down'), default=0)
    create_time = models.DateTimeField(verbose_name=_('Create Time'),
                                       auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'))

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return self.__unicode__()

    class Meta(object):
        app_label = 'athena'
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class QuestionComment(models.Model):
    """ Question comment model
    """

    question = models.ForeignKey(Question, verbose_name=_('Question'))
    commenter = models.ForeignKey(User, verbose_name=_('Commenter'))
    content = models.TextField(verbose_name=_('Content'))
    create_time = models.DateTimeField(verbose_name=_('create_time'),
                                       auto_now_add=True)

    def __unicode__(self):
        return self.content

    def __repr__(self):
        return self.content

    class Meta(object):
        app_label = 'athena'
        verbose_name = _('Question Comment')
        verbose_name_plural = _('Question Comments')


__all__ = (
    'Question',
    'QuestionComment',
)