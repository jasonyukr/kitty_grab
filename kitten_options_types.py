# generated by gen-config.py DO NOT edit
# vim:fileencoding=utf-8

import typing
from kitty.conf.utils import KeyAction, KittensKeyMap
import kitty.conf.utils
from kitty.rgb import Color
import kitty.rgb
from kitty.types import ParsedShortcut
import kitty.types


option_names = (  # {{{
 'map',
 'select_by_word_characters',
 'selection_background',
 'selection_foreground')  # }}}


class Options:
    select_by_word_characters: str = ''
    selection_background: Color = Color(red=82, green=148, blue=226)
    selection_foreground: Color = Color(red=255, green=255, blue=255)
    map: typing.List[typing.Tuple[kitty.types.ParsedShortcut, kitty.conf.utils.KeyAction]] = []
    key_definitions: KittensKeyMap = {}
    config_paths: typing.Tuple[str, ...] = ()
    config_overrides: typing.Tuple[str, ...] = ()

    def __init__(self, options_dict: typing.Optional[typing.Dict[str, typing.Any]] = None) -> None:
        if options_dict is not None:
            for key in option_names:
                setattr(self, key, options_dict[key])

    @property
    def _fields(self) -> typing.Tuple[str, ...]:
        return option_names

    def __iter__(self) -> typing.Iterator[str]:
        return iter(self._fields)

    def __len__(self) -> int:
        return len(self._fields)

    def _copy_of_val(self, name: str) -> typing.Any:
        ans = getattr(self, name)
        if isinstance(ans, dict):
            ans = ans.copy()
        elif isinstance(ans, list):
            ans = ans[:]
        return ans

    def _asdict(self) -> typing.Dict[str, typing.Any]:
        return {k: self._copy_of_val(k) for k in self}

    def _replace(self, **kw: typing.Any) -> "Options":
        ans = Options()
        for name in self:
            setattr(ans, name, self._copy_of_val(name))
        for name, val in kw.items():
            setattr(ans, name, val)
        return ans

    def __getitem__(self, key: typing.Union[int, str]) -> typing.Any:
        k = option_names[key] if isinstance(key, int) else key
        try:
            return getattr(self, k)
        except AttributeError:
            pass
        raise KeyError(f"No option named: {k}")


defaults = Options()
defaults.map = [
    # quit
    (ParsedShortcut(mods=0, key_name='q'), KeyAction('quit')),
    # quit
    (ParsedShortcut(mods=0, key_name='ESCAPE'), KeyAction('quit')),
    # confirm
    (ParsedShortcut(mods=0, key_name='ENTER'), KeyAction('confirm')),
    # move
    (ParsedShortcut(mods=0, key_name='LEFT'), KeyAction('move', ('left',))),
    # move
    (ParsedShortcut(mods=0, key_name='RIGHT'), KeyAction('move', ('right',))),
    # move
    (ParsedShortcut(mods=0, key_name='UP'), KeyAction('move', ('up',))),
    # move
    (ParsedShortcut(mods=0, key_name='DOWN'), KeyAction('move', ('down',))),
    # move
    (ParsedShortcut(mods=0, key_name='PAGE_UP'), KeyAction('move', ('page_up',))),
    # move
    (ParsedShortcut(mods=0, key_name='PAGE_DOWN'), KeyAction('move', ('page_down',))),
    # move
    (ParsedShortcut(mods=0, key_name='HOME'), KeyAction('move', ('first',))),
    # move
    (ParsedShortcut(mods=0, key_name='a'), KeyAction('move', ('first_nonwhite',))),
    # move
    (ParsedShortcut(mods=0, key_name='END'), KeyAction('move', ('last_nonwhite',))),
    # move
    (ParsedShortcut(mods=0, key_name='e'), KeyAction('move', ('last',))),
    # move
    (ParsedShortcut(mods=4, key_name='HOME'), KeyAction('move', ('top',))),
    # move
    (ParsedShortcut(mods=4, key_name='END'), KeyAction('move', ('bottom',))),
    # move
    (ParsedShortcut(mods=4, key_name='LEFT'), KeyAction('move', ('word_left',))),
    # move
    (ParsedShortcut(mods=4, key_name='RIGHT'), KeyAction('move', ('word_right',))),
    # scroll
    (ParsedShortcut(mods=4, key_name='UP'), KeyAction('scroll', ('up',))),
    # scroll
    (ParsedShortcut(mods=4, key_name='DOWN'), KeyAction('scroll', ('down',))),
    # select_stream
    (ParsedShortcut(mods=1, key_name='LEFT'), KeyAction('select', ('stream', 'left'))),
    # select_stream
    (ParsedShortcut(mods=1, key_name='RIGHT'), KeyAction('select', ('stream', 'right'))),
    # select_stream
    (ParsedShortcut(mods=1, key_name='UP'), KeyAction('select', ('stream', 'up'))),
    # select_stream
    (ParsedShortcut(mods=1, key_name='DOWN'), KeyAction('select', ('stream', 'down'))),
    # select_stream
    (ParsedShortcut(mods=1, key_name='PAGE_UP'), KeyAction('select', ('stream', 'page_up'))),
    # select_stream
    (ParsedShortcut(mods=1, key_name='PAGE_DOWN'), KeyAction('select', ('stream', 'page_down'))),
    # select_stream
    (ParsedShortcut(mods=1, key_name='HOME'), KeyAction('select', ('stream', 'first'))),
    # select_stream
    (ParsedShortcut(mods=0, key_name='A'), KeyAction('select', ('stream', 'first_nonwhite'))),
    # select_stream
    (ParsedShortcut(mods=1, key_name='END'), KeyAction('select', ('stream', 'last_nonwhite'))),
    # select_stream
    (ParsedShortcut(mods=0, key_name='E'), KeyAction('select', ('stream', 'last'))),
    # select_stream
    (ParsedShortcut(mods=5, key_name='HOME'), KeyAction('select', ('stream', 'top'))),
    # select_stream
    (ParsedShortcut(mods=5, key_name='END'), KeyAction('select', ('stream', 'bottom'))),
    # select_stream
    (ParsedShortcut(mods=5, key_name='LEFT'), KeyAction('select', ('stream', 'word_left'))),
    # select_stream
    (ParsedShortcut(mods=5, key_name='RIGHT'), KeyAction('select', ('stream', 'word_right'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='LEFT'), KeyAction('select', ('columnar', 'left'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='RIGHT'), KeyAction('select', ('columnar', 'right'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='UP'), KeyAction('select', ('columnar', 'up'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='DOWN'), KeyAction('select', ('columnar', 'down'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='PAGE_UP'), KeyAction('select', ('columnar', 'page_up'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='PAGE_DOWN'), KeyAction('select', ('columnar', 'page_down'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='HOME'), KeyAction('select', ('columnar', 'first'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='A'), KeyAction('select', ('columnar', 'first_nonwhite'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='END'), KeyAction('select', ('columnar', 'last_nonwhite'))),
    # select_columnar
    (ParsedShortcut(mods=2, key_name='E'), KeyAction('select', ('columnar', 'last'))),
    # select_columnar
    (ParsedShortcut(mods=6, key_name='HOME'), KeyAction('select', ('columnar', 'top'))),
    # select_columnar
    (ParsedShortcut(mods=6, key_name='END'), KeyAction('select', ('columnar', 'bottom'))),
    # select_columnar
    (ParsedShortcut(mods=6, key_name='LEFT'), KeyAction('select', ('columnar', 'word_left'))),
    # select_columnar
    (ParsedShortcut(mods=6, key_name='RIGHT'), KeyAction('select', ('columnar', 'word_right'))),
]
