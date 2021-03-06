try:
    try:
        import xmlrpclib
    except ImportError:
        import xmlrpc.client as xmlrpclib
except ImportError:
    import _pydev_xmlrpclib as xmlrpclib
try:
    try:
        from SimpleXMLRPCServer import SimpleXMLRPCServer
    except ImportError:
        from xmlrpc.server import SimpleXMLRPCServer
except ImportError:
    from _pydev_SimpleXMLRPCServer import SimpleXMLRPCServer
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
try:
    execfile=execfile #Not in Py3k
except NameError:
    from _pydev_execfile import execfile
try:
    import Queue
except:
    import queue as Queue #@UnresolvedImport
try:
    from pydevd_exec import Exec
except:
    from pydevd_exec2 import Exec
try:
    from urllib import quote
except:
    from urllib.parse import quote #@UnresolvedImport


import os
try:
    relpath = os.path.relpath
except:
    # Only there from 2.6 onwards... let's provide a replacement.
    def _split_path(path):
        parts = []
        loc = path

        while loc != os.curdir and loc != os.pardir:
            prev = loc
            loc, child = os.path.split(prev)
            if loc == prev:
                break

            parts.append(child)

        parts.append(loc)
        parts.reverse()
        return parts

    def relpath(path, start=None):
        if start is None:
            start = os.curdir
        origin = os.path.abspath(path)
        start = os.path.abspath(start)

        orig_list = _split_path(os.path.normcase(origin))
        dest_list = _split_path(start)

        if orig_list[0] != os.path.normcase(dest_list[0]):
            return start

        i = 0
        for start_seg, dest_seg in zip(orig_list, dest_list):
            if start_seg != os.path.normcase(dest_seg):
                break
            i += 1

        segments = [os.pardir] * (len(orig_list) - i)
        segments += dest_list[i:]
        if len(segments) == 0:
            return os.curdir
        else:
            return os.path.join(*segments)
