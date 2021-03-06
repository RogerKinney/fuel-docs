# -*- coding: utf-8 -*-
#
# "Fuel" documentation build configuration file, created by
# sphinx-quickstart on Tue Sep 25 14:02:29 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# -- Default Settings -----------------------------------------------------
execfile('../common_conf.py')

exclude_patterns = ['_*', "pages", 'relnotes', 'contents', 'index', '*-guide', '*.rst']

pdf_documents = [ 
    ('pdf/pdf_user', u'Mirantis-OpenStack-4.0-UserGuide',  u'User Guide',
    u'2013, Mirantis Inc.'),
    ('pdf/pdf_install', u'Mirantis-OpenStack-4.0-InstallGuide', u'Installation Guide', u'2013, Mirantis Inc.'),
    ('pdf/pdf_reference', u'Mirantis-OpenStack-4.0-ReferenceArchitecture', u'Reference Architecture', u'2013, Mirantis Inc.'),
    ('pdf/pdf_preinstall', u'Mirantis-OpenStack-4.0-Pre-InstallationGuide', u'Pre-Installation Guide', u'2013, Mirantis Inc.')
#    (master_doc, project, project, copyright),
]
