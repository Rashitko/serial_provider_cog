from setuptools import setup

setup(
    name='serial_provider_cog',
    version='0.1.4',
    packages=['serial_cog', 'serial_cog.modules'],
    url='https://github.com/Rashitko/serial_provider_cog',
    download_url='https://github.com/Rashitko/serial_provider_cog/master/tarball/',
    license='MIT',
    author='Michal Raska',
    author_email='michal.raska@gmail.com',
    description='',
    install_requires=['up', 'pyyaml', 'pyserial'],
    package_data={
        'serial_cog': ['registered_modules.yml']
    }
)
