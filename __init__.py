"""嘉心糖滚出去"""
import random
from pathlib import Path

from botoy import S
from botoy import decorators as deco
from botoy.contrib import plugin_receiver

IMAGES = [str(i.absolute()) for i in (Path(__file__).parent / 'asoul').iterdir()]


@plugin_receiver.group
@deco.re_findall(r"(然然|嘉然|的捏)")
@deco.ignore_botself
def group(ctx):
    S.bind(ctx).image(random.choice(IMAGES), '嘉❤糖滚出去', type=S.TYPE_PATH)
