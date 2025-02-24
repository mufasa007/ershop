import os
import re

pattern_name_exclude = r'\._|\.DS_Store'

pattern_name = (
    r'( \(Z-Library\).)|'
    r'( & chenjin5_com \[加西亚·马尔克斯 & chenjin5_com\] -- 新经典文库, \d{4} -- chenjin5_com 海量电子书免费下载 -- \d+ -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( -- \d{4} -- chenjin5_com 海量电子书免费下载 -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( -- c.-- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( \[\[英\] 杰拉德·马丁\] & chenjin5_com \[\[英\] 杰拉德·马丁 \[\[英\]\] -- \d{4} -- cj5 -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( & chenjin5_com -- \d{4} -- cj5 -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( -- XJDCN -- \d+ -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( -- chenjin5_com 海量电子书免费下载 -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( & chenjin5_com -- \d+ -- cj5 -- [a-f0-9]+ -- .)|'
    r'( & chenjin5_com \[\[英\] 杰拉德·马丁 \[\[英\]\] -- \d+ -- cj5 -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( & chenjin5_com -- \d+ -- cj5 -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( -- [a-f0-9]+ -- Anna’s Archive.)|'
    r'( -- \d+ -- [a-f0-9]+ -- [^ ]+ (Archive).)|'
    r'( -- [a-f0-9]+.)|'
    r'( -- [a-f0-9]+ -- Anna| -- 笔趣阁.)|'
    r'( -- chenjin5_com 海量电子书免费下载.)|'
    r'(.enjin5_com 海量电子书免费下载.)|'
    r'( -- cj5.)|'
    r'( -- [a-f0-9]+ -- .)|'
    r'( -- chenjin5_com 万千书友聚集地.)'
)

match_suffix = r'\.[a-zA-Z0-9]+$'


def convertFileSize(size):
    # 定义单位列表
    units = 'Bytes', 'KB', 'MB', 'GB', 'TB'
    # 初始化单位为Bytes
    unit = units[0]
    # 循环判断文件大小是否大于1024，如果大于则转换为更大的单位
    for i in range(1, len(units)):
        if size >= 1024:
            size /= 1024
            unit = units[i]
        else:
            break
    # 格式化输出文件大小，保留两位小数
    return '{:.2f}{}'.format(size, unit)


def list_files_and_folders(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                oldname = file_name
                an = re.search(pattern_name_exclude, oldname)  # 匹配是否为垃圾文件（mac、windows）
                if an is None:
                    print(f'{oldname}')
                    name = file_name
                    if (re.search(pattern_name, oldname) is not None):
                        newname = re.sub(pattern_name, '.', oldname)
                        oldPath = os.path.join(root, oldname)
                        newPath = os.path.join(root, newname)
                        name = newname
                        os.rename(oldPath, newPath)

                    filePath = os.path.join(root, name)
                    stats = os.stat(filePath)

                    fileSize = convertFileSize(stats.st_size)
                    print(fileSize)

                    file.write(f" | {name} | {fileSize} | \n")


# 指定要读取的目录路径
directory_path = '/Users/zhoujiankang/Documents/project/virtualGoods/文学/诺贝尔文学奖/1982年诺贝尔文学奖-加西亚·马尔克斯/加西亚·马尔克斯作品全集'
# 指定输出的txt文件路径
output_txt_path = 'output.txt'

list_files_and_folders(directory_path, output_txt_path)


