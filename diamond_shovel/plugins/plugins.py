from contextlib import contextmanager


class PluginInitContext:
    @property
    def config(self):
        ...

    @property
    def data_folder(self):
        ...

    @contextmanager
    def open_resource(self, name):
        ...
