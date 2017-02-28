from setuptools import setup

setup(name="SoftwareEng_A3",
      version="1.0",
      description="LED Testing for Assignment3 in COMP30670 2017",
      url="",
      author="Selene Waide",
      author_email="selene.waide@ucdconnect.ie",
      licence="",
      packages=['led_solver'],
      entry_points = {
          'console_scripts': ['comp30670_SoftwareEng_A3 = led_solver.main:main_led']
          },
      install_requires=[
          'numpy'
      ],
      )

