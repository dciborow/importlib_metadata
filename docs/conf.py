#!/usr/bin/env python3

extensions = ['sphinx.ext.autodoc', 'jaraco.packaging.sphinx', 'rst.linker']

master_doc = "index"

link_files = {
    '../CHANGES.rst': dict(
        using=dict(GH='https://github.com'),
        replace=[
            dict(
                pattern=r'(Issue #|\B#)(?P<issue>\d+)',
                url='{package_url}/issues/{issue}',
            ),
            dict(
                pattern=r'(?m:^((?P<scm_version>v?\d+(\.\d+){1,2}))\n[-=]+\n)',
                with_scm='{text}\n{rev[timestamp]:%d %b %Y}\n',
            ),
            dict(
                pattern=r'PEP[- ](?P<pep_number>\d+)',
                url='https://www.python.org/dev/peps/pep-{pep_number:0>4}/',
            ),
        ],
    )
}

# Be strict about any broken references:
nitpicky = True

# Support intersphinx links
extensions += [
    'sphinx.ext.intersphinx',
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'importlib_resources': (
        'https://importlib-resources.readthedocs.io/en/latest/',
        None,
    ),
}

# Workaround for #316
nitpick_ignore = [
    ('py:class', 'importlib_metadata.EntryPoints'),
    ('py:class', 'importlib_metadata.SelectableGroups'),
    ('py:class', 'importlib_metadata._meta._T'),
]
