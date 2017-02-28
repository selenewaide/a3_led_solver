from setuptools import setup

setup(name="SoftwareEng_A3",
      version="1.0",
      description="LED Testing for Assignment3 in COMP30670 2017",
      url="",
      author="Selene Waide",
      author_email="selene.waide@ucdconnect.ie",
      licence="",
      packages=['led_solver'],
      scripts = ["scripts/solve_led"],
      install_requires=[
          'numpy'
      ],
      )

