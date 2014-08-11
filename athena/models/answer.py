#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jack River'

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from athena.models.question import Question


class Answer(models.Model):
    """ Answer model
    """

    question = models.ForeignKey(Question, verbose_name=_('Question'))
    content = models.TextField(verbose_name=_('Content'))
    answerer = models.ForeignKey(User, verbose_name=_('Answerer'))
    vote_up = models.IntegerField(verbose_name=_('Vote Up'), default=0)
    vote_down = models.IntegerField(verbose_name=_('Vote Down'), default=0)
    create_time = models.DateTimeField(verbose_name=_('Create Time'),
                                       auto_now_add=True)

    class Meta(object):
        app_label = 'athena'
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')


class AnswerComment(models.Model):
    """ Answer comment model
    """

    content = models.TextField(verbose_name=_('Content'))
    commenter = models.ForeignKey(User, verbose_name=_('Commenter'))
    create_time = models.DateTimeField(verbose_name=_('Create Time'),
                                       auto_now_add=True)

    class Meta(object):
        app_label = 'athena'
        verbose_name = _('Answer Comment')
        verbose_name_plural = _('Answer Comments')


__all__ = (
    'Answer',
    'AnswerComment',
)