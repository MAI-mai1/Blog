

import requests


def md_change_to_rst(md_file: str, rst_file: str):
    """
    将 markdown 格式文档转换为 rst 格式文档
    @param md_file:  markdown文件的路径
    @param rst_file:  rst文件的路径
    """
    response = requests.post(
        url='http://c.docverter.com/convert',
        data={'to': 'rst', 'from': 'markdown'},
        files={'input_files[]': open(md_file, 'rb')}
    )

    if response.ok:
        with open(rst_file, "wb") as f:
            f.write(response.content)


if __name__ == '__main__':
    md_change_to_rst("preface.md", "preface.rst")
