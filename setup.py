# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='smsReceiver',
    version='1.0',
    url='https://github.com/mthbernardes/smsReceiver',
    license='MIT License',
    author='Matheus Bernardes',
    author_email='mthbernardes@gmail.com',
    keywords='sms receive',
    description=u'Module to get online number to receive SMS',
    packages=['smsReceiver'],
    install_requires=['requests','lxml'],
)
