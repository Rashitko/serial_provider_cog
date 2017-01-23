from up.registrar import UpRegistrar


class Registrar(UpRegistrar):
    def __init__(self):
        super().__init__('serial_cog')

    def register(self):
        external_modules = self._load_external_modules()
        if external_modules is not None:
            self._register_module('SerialProvider', 'serial_cog.modules.serial_module')
            self._write_external_modules()
        return True
