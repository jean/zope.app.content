##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id: test_file.py,v 1.1 2003/04/14 12:19:28 mgedmin Exp $
"""

import unittest

from zope.testing.functional import BrowserTestCase


class TestFile(BrowserTestCase):

    def testAddFile(self):
        # Step 1: add the file
        response = self.publish('/+/action.html',
                                basic='mgr:mgrpw',
                                form={'type_name': u'File', 'id': u'foo'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/@@contents.html')
        # Step 2: check that it it visible in the folder listing
        response = self.publish('/')
        self.assertEqual(response.getStatus(), 200)
        self.assert_(response.getBody().find('foo') != -1)
        # Step 3: check that its contents are available
        response = self.publish('/foo')
        self.assertEqual(response.getStatus(), 200)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFile))
    return suite

if __name__=='__main__':
    unittest.main(defaultTest='test_suite')
