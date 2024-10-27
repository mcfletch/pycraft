"""Load and reload scripts as the user changes them on disk"""

import asyncio, os, glob, traceback, logging

try:
    from imp import new_module
except ImportError:
    import importlib, types

    def new_module(name):
        return types.ModuleType(name)


log = logging.getLogger(__name__)


class ScriptLoader(object):
    def __init__(self, script_dirs):
        self.script_dirs = script_dirs
        self.scripts = {}  # path: module
        self.names = {}  # python name: path
        self.msg_queue = asyncio.Queue()

    async def main(self):
        """Scan the scripts directories, loading each script and watching for changes"""
        log.info("Starting to load scripts from: %s", self.script_dirs)
        import os, glob

        directories = [
            os.path.normpath(os.path.abspath(x))
            for x in self.script_dirs.split(os.pathsep)
        ]

        while True:
            for directory in directories:
                # log.info("Scanning directory: %s", directory)
                for path in sorted(glob.glob(os.path.join(directory, '*.py'))):
                    try:
                        if path not in self.scripts:
                            self.scripts[path] = await self.load_path(path)
                            await self.msg_queue.put("Loaded script: %r" % (path))
                        elif os.stat(path) != self.scripts[path][0]:
                            self.scripts[path] = await self.load_path(path)
                            await self.msg_queue.put("Reloaded script: %r" % (path))
                    except (SyntaxError, OSError) as err:
                        # you deleted the file or it became unavailable...
                        log.warning("Unable to process path: %s", path)
                        pass  # TODO: something useful...
            await asyncio.sleep(2)

    async def load_path(self, path):
        import os, traceback

        try:
            base = os.path.splitext(os.path.basename(path))[0]
            name = 'scripts.%s' % (base,)
            other = self.names.get(name)
            if other is not None and other != path:
                await self.msg_queue.put(
                    "Duplicate module name: %s, please rename your file" % (path,)
                )
                return None, None
            self.names[name] = path
            stat = os.stat(path)
            with open(path, encoding='utf-8') as fh:
                content = fh.read()
            new_module = new_module(name)
            new_module.__file__ = path
            code = compile(content, path, 'exec')
            exec(code, new_module.__dict__, new_module.__dict__)
        except Exception as err:
            await self.msg_queue.put(
                "Can't import %s:\n %s" % (base, traceback.format_exc()),
            )
            return None, None
        else:
            return stat, new_module
