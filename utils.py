import os
from subprocess import Popen, PIPE, STDOUT

import jinja2

from consts import RES_FILENAME


def template_render(tpl_path, context, dir_legacy=True):
    """
    Возвращает заполненный контекстом шаблон в виде строки
    :param tpl_path: str путь до файла с шаблоном
    :param context: dict контекст
    :param dir_legacy: bool флаг, показывающий что путь берется относительно дирректории с шаблонами
    :return:
    """
    if dir_legacy:
        path, filename = os.path.split(os.path.join(get_template_dir(), tpl_path))
    else:
        path, filename = os.path.split(tpl_path)

    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def get_base_dir():
    return os.path.dirname(os.path.abspath(__file__))


def get_template_dir():
    return os.path.join(get_base_dir(), 'templates')


def get_logs_dir():
    logs_dir = os.path.join(get_base_dir(), 'logs')

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    return logs_dir


def get_audio_file():
    return os.path.join(get_base_dir(), RES_FILENAME)


def create_audio_message(message):
    with Popen(['wine', '/home/forty/Загрузки/balcon/balcon.exe', '-i', '-n', 'Maxim',
                '-w', RES_FILENAME, '-enc', 'utf8'], stdout=PIPE, stdin=PIPE, stderr=STDOUT) as p:
        p.communicate(input=message.encode('utf-8'))
