# -*- coding: utf-8 -*-
from logging import getLogger
from zope.i18nmessageid import MessageFactory


logger = getLogger('pd.contentrules.sms')
messageFactory = MessageFactory('pd.contentrules.sms')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
