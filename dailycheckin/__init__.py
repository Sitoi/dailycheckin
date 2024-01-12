import pkgutil as _pkgutil


class CheckIn:
    name = "Base"


__path__ = _pkgutil.extend_path(__path__, __name__)
for _, _modname, _ in _pkgutil.walk_packages(path=__path__, prefix=__name__ + "."):
    if _modname not in ["dailycheckin.main", "dailycheckin.configs"]:
        __import__(_modname)
