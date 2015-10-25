import re
from .exceptions import DefineBlockError
from .constants import ALWAYS_ALLOWED, LINE_END


class BlockBlock:

    RE_BLOCK = re.compile('^\s*#block\s+([a-zA-Z0-9_]+)\s*:\s*$', re.UNICODE)

    def __init__(self, lines):
        from .block import Block
        self._name = self._compile(lines)
        self._block = Block(lines, allowed=ALWAYS_ALLOWED | LINE_END)

    def render(self, namespace):
        namespace.add_block(self._name, self._block)
        return None

    def _compile(self, lines):
        m = self.RE_BLOCK.match(lines.current)
        if m is None:
            raise DefineBlockError('Incorrect block definition at line {}, {}\nShould be something like: #block my_block:'.format(lines.pos, lines.current))
        return m.group(1)
