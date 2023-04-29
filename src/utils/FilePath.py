import os
import sys


def resource_path(relative_path):
    """获取打包后的资源路径"""
    if getattr(sys, "frozen",False):
        # 打包后的路径
        base_path=sys._MEIPASS
    else:
        base_path=os.path.abspath(".")\
                  # +"/src/"

    print("文件位置-", base_path)
    return os.path.join(base_path, relative_path)
