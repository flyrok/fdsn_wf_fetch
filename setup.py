""" Pull waveforsm from fdsn server and saves as
SAC or mseed

See:
https://github.com/flyrok/fdsn_wf_fetch
"""

from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).resolve().parent


# Get the long description from the README file
readme=here / 'README.md'
with open(readme, encoding='utf-8') as f:
    long_description = f.read()

PROJECT_NAME="fdsn_wf_fetch"
exec(open(here / "src/version.py").read())
VERSION=__version__
DESCRIPTION="Pull station waveform data from FDSN server"
URL="https://github.com/flyrok/fdsn_wf_fetch"
AUTHOR="A Ferris"
EMAIL="aferris@flyrok.org"
CLASSIFIERS=['Development Status :: 3 - Alpha',
    'Intended Audience :: Seismic Researcher',
    'Topic :: Obspy/FDSN :: Helper Script',
    'License :: OSI Approved :: GPL-3 License',
    'Programming Language :: Python :: 3']
KEYWORDS="seismology obspy earthquakes fdsn seismograms"     

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
    python_requires='>=3.6',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'fdsn_wf_fetch.py=src.fdsn_wf_fetch:main',
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

