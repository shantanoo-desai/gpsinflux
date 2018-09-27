from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

with open('requirements.txt', 'r') as f:
    requires = [x.strip() for x in f if x.strip()]

setup(name='gpsinflux',
      version='1.0',
      description='Python Module to write GPS information to InfluxDB',
      long_description=readme(),
      url='https://github.com/shantanoo-desai/gpsinflux',
      author='Shantanoo Desai',
      author_email='shantanoo.desai@gmail.com',
      license='MIT',
      packages=['gpsinflux'],
      install_requires=requires,
      zip_safe=False)
