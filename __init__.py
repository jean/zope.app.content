##############################################################################
#
# Copyright (c) 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Content Type convenience lookup functions 

$Id$
"""
__docformat__ = 'restructuredtext'
from zope.interface import classProvides
from zope.app.interface import queryType
from zope.app.schema.interfaces import IVocabularyFactory
from zope.app.content.interfaces import IContentType
from zope.app.component.vocabulary import UtilityVocabulary

def queryContentType(object):
    """Returns the interface implemented by object which implements
    `IContentType`."""
    return queryType(object, IContentType)

class ContentTypesVocabulary(UtilityVocabulary):
    classProvides(IVocabularyFactory)
    interface = IContentType
