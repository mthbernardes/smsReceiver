# -*- coding: utf-8 -*-
from setuptools import setup,find_packages

setup(
    name='smsReceiver',
    version='2.0',
    url='https://github.com/mthbernardes/smsReceiver',
    license='MIT License',
    author='Matheus Bernardes',
    author_email='mthbernardes@gmail.com',
    keywords='sms receive',
    description=u'Module to get online number to receive SMS',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests','lxml'],
)
