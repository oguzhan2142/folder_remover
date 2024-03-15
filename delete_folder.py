import errno
import os
import shutil
import stat
import time


def handle_remove_readonly(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
        func(path)
    elif func in (os.rmdir, os.remove) and excvalue.errno == errno.ENOTEMPTY:
        for _ in range(5):  # retry 5 times
            time.sleep(0.5)  # wait for 0.5 seconds
            try:
                func(path)
                break
            except OSError:
                pass
        else:  # if all retries failed, re-raise the last exception
            raise
    else:
        raise

def delete(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path, onerror=handle_remove_readonly)