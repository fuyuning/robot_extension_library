import os
from setuptools import setup, find_packages
from setuptools.command.install import install

# 1.2.0.dev1  # Development release
# 1.2.0a1     # Alpha Release
# 1.2.0b1     # Beta Release
# 1.2.0rc1    # Release Candidate
# 1.2.0       # Final Release
# 1.2.0.post1 # Post Release
# 15.10       # Date based release
# 23          # Serial release
VERSION = '0.0.1a1'
PATH = os.path.dirname(os.path.abspath(__file__))

# When the project is installed by pip, this is the specification that is used to install its dependencies.
install_requires = ['xlwt>=1.3.0']


def read(f_name):
    return open(os.path.join(PATH, f_name)).read()


class PostInstallCommand(install):
    def run(self):
        pass


setup(
    # This is the name of your project, determining how your project is listed on PyPI.
    name='RobotFrameworkExtensions',
    version=VERSION,
    # Give a short and long description for your project. These values will be displayed on PyPI if you publish your project.
    description='The extensions with robot-framework for my self.',
    long_description=read('README.md'),
    # Give a homepage URL for your project.
    url='',
    # Provide details about the author.
    author='',
    author_email='',
    license='MIT',
    # List keywords that describe your project.
    keywords='',
    # List additional relevant URLs about your project.
    project_urls=[],
    packages=find_packages(exclude=['docs', 'tests*', 'example']),
    install_requires=install_requires,
    # If your project only runs on certain Python versions, setting the `python_requires` argument.
    python_requires='>=3',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        # You can then let the toolchain handle the work of turning these interfaces into actual scripts.
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    cmd_class={
        'install': PostInstallCommand,
    }
)
