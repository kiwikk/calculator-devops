from setuptools import setup, find_packages


setup(
	name='calc',
	version='0.0.1',
	description='simple calc',
	long_description='simple calc',
	author='edfrolova',
	author_email='lakki00@mail.ru',
	license='Proprietary',
	classifiers=[
		'Intended Audience :: Developers',
		'Licence :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.9'
	],
	package_data={'com': ['py.typed']},
	packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
	install_requires=[line for line in open('requirements.txt', 'r')]
)
