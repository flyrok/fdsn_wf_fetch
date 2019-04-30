""" Pull waveforsm from fdsn server


See:
https://github.com/flyrok/fdsn_wffetch
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

PROJECT_NAME="fdsn_wf_fetch"
exec(open(here+"/fdsn_wf/version.py").read())
VERSION=__version__
DESCRIPTION="Pull station waveform data from FDSN server"
URL="https://github.com/flyrok/fdsn_station_info"
AUTHOR="A Ferris"
EMAIL="aferris@gmail.com"
CLASSIFIERS=['Development Status :: 3 - Alpha',
    'Intended Audience :: Seismic Researchers',
    'Topic :: Obspy/FDSN :: Helper Scripts',
    'License :: OSI Approved :: GPL-3 License',
     'Programming Language :: Python :: 3']
KEYWORDS="seismology obspy earthquakes fdsn"     

setup(
    name=PROJECT_NAME,  # Required
    version=VERSION,  # Required
    description=DESCRIPTION,  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url=URL,  # Optional
    author=AUTHOR,  # Optional
    author_email=EMAIL,  # Optional
    classifiers=CLASSIFIERS ,
    keywords=KEYWORDS,  # Optional
    python_requires='>=3.5',
    include_package_data=True,
    packages=find_packages(exclude=['examples','doc']),
    install_requires=[],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'fdsn_wf_fetch.py=fdsn_wf_fetch.fdsn_wf_fetch:main',
        ],
    },
    extras_require={  # Optional
    },
    package_data={  
    },
    project_urls={  # Optional
        'Source': URL,
    },
)

