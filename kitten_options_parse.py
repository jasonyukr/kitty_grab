# generated by gen-config.py DO NOT edit
# vim:fileencoding=utf-8

import typing
from kitten_options_utils import parse_map
from kitty.conf.utils import merge_dicts, to_color


class Parser:

    def selection_background(self, val: str, ans: typing.Dict[str, typing.Any]) -> None:
        ans['selection_background'] = to_color(val)

    def selection_foreground(self, val: str, ans: typing.Dict[str, typing.Any]) -> None:
        ans['selection_foreground'] = to_color(val)

    def map(self, val: str, ans: typing.Dict[str, typing.Any]) -> None:
        for k in parse_map(val):
            ans['map'].append(k)


def create_result_dict() -> typing.Dict[str, typing.Any]:
    return {
        'map': [],
    }


actions = frozenset(('map',))


def merge_result_dicts(defaults: typing.Dict[str, typing.Any], vals: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
    ans = {}
    for k, v in defaults.items():
        if isinstance(v, dict):
            ans[k] = merge_dicts(v, vals.get(k, {}))
        elif k in actions:
            ans[k] = v + vals.get(k, [])
        else:
            ans[k] = vals.get(k, v)
    return ans


parser = Parser()


def parse_conf_item(key: str, val: str, ans: typing.Dict[str, typing.Any]) -> bool:
    func = getattr(parser, key, None)
    if func is not None:
        func(val, ans)
        return True
    return False
