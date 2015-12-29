from setuptools import setup

if __name__ == '__main__':
    setup(
        name='pytest-repeat',
        description='Repeat plugin for py.test',
        author='Aarni Koskela',
        author_email='akx@iki.fi',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Testing',
            'Topic :: Utilities',
            'Intended Audience :: Developers',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
        ],
        py_modules=['pytest_repeat'],
        entry_points={'pytest11': ['repeat = pytest_repeat']},
    )
