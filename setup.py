#! -*- coding: utf-8 -*-
import codecs
import os 
import re
from setuptools import setup, find_packages

# avoid a from JapaneseTokenizer import __version__ as version (that compiles JapaneseTokenizer.__init__ and is not compatible with bdist_deb)
version = None
for line in codecs.open(os.path.join('JapaneseTokenizer', '__init__.py'), 'r', encoding='utf-8'):
    matcher = re.match(r"""^__version__\s*=\s*['"](.*)['"]\s*$""", line)
    version = version or matcher and matcher.group(1)

setup(
    author='Kensuke Mitsuzawa',
    name = 'JapaneseTokenizer',
    version=version,
    test_suite='JapaneseTokenizer.test.test_all.suite',
    install_requires = ['mecab-python'],
    packages=find_packages(),
    )

