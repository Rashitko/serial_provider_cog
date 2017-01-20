import os

import yaml
from setuptools import setup
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        upm_install_path = os.environ.get('UPM_INSTALL_PATH', os.getcwd())
        path = os.path.join(upm_install_path, 'external_modules.yml')
        with open(path) as external_mods_file:
            external_mods = yaml.load(external_mods_file)
            if external_mods is None:
                external_mods = {}
        with open(path, 'w+') as external_mods_file:
            external_mods['serial_provider_cog'] = {
                'modules': [
                    {'prefix': 'serial_provider.modules.serial_module', 'class_name': 'SerialProvider'}
                ],
                'recorders': []
            }
            external_mods['serial_provider_cog']['modules'] = ['serial_provider.modules.serial_module.SerialModule']
            yaml.dump(external_mods, external_mods_file)
        install.run(self)


setup(
    name='serial_provider_cog',
    version='0.1',
    packages=['serial_provider', 'serial_provider.modules'],
    url='',
    license='',
    author='Michal Raska',
    author_email='michal.raska@gmail.com',
    description='',
    install_requires=['up', 'pyyaml', 'twisted', 'pyserial'],
    cmdclass={
        'install': PostInstallCommand,
    }
)
