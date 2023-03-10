import sys
from typing import Any


class HuffmanCoder:
    class Vertex:
        def __init__(self,
                     is_terminal: bool = False,
                     elem: str = None,
                     low_pred: 'HuffmanCoder.Vertex' = None,
                     great_pred: 'HuffmanCoder.Vertex' = None):
            self.is_terminal = is_terminal
            self.elem = elem
            self.lower = low_pred
            self.greater = great_pred

        def __repr__(self) -> str:
            if self.is_terminal:
                return f'({self.elem})'
            return f'({self.lower} & {self.greater})'

    def __init__(self):
        self.syms_entries = dict[HuffmanCoder.Vertex, int]()
        self.codes = dict[str, str]()

    def reset_dict(self) -> None:
        self.syms_entries.clear()

    def _create_dict(self, data: str):
        syms_to_times = dict[str, int]()

        for s in data:
            if s in syms_to_times:
                syms_to_times[s] += 1
                continue
            syms_to_times.update({s: 1})

        self.syms_entries = {
            HuffmanCoder.Vertex(is_terminal=True, elem=key): val
            for key, val in syms_to_times.items()
        }

    @staticmethod
    def _extract_min_vertex(vertexes: dict[Any, int]) -> ('HuffmanCoder.Vertex', int):
        lower, times = min(vertexes.items(), key=lambda x: x[1])
        del vertexes[lower]
        return lower, times

    def _create_tree(self) -> 'HuffmanCoder.Vertex':
        s_entries = self.syms_entries.copy()

        if not s_entries:
            raise Exception('NO DATA GIVEN')

        while not len(s_entries) == 1:
            lower, l_times = HuffmanCoder._extract_min_vertex(s_entries)
            greater, g_times = HuffmanCoder._extract_min_vertex(s_entries)

            s_entries.update(
                {HuffmanCoder.Vertex(low_pred=lower, great_pred=greater): l_times + g_times}
            )

        return s_entries.popitem()[0]

    def _set_codes_from_tree(self, ver: Any, prefix=str()) -> None:
        if not ver.is_terminal:
            self._set_codes_from_tree(ver.greater, prefix=prefix[:] + '1')
            self._set_codes_from_tree(ver.lower, prefix=prefix[:] + '0')
            return
        self.codes.update({ver.elem: prefix if prefix else '0'})

    def encode(self, data: str) -> (list[str], dict[str, str]):
        self._create_dict(data)
        self._set_codes_from_tree(self._create_tree())
        return [self.codes[s] for s in data], self.codes


def main():
    if not len(sys.argv) == 2:
        raise Exception(f'BAD ARGUMENTS')

    coder = HuffmanCoder()
    coded_data, codes = coder.encode(sys.argv[1])
    print(f'USED FOLLOWING CODES\n{codes}')
    print(f'CODED DATA\n{" ".join(coded_data)}')


if __name__ == '__main__':
    main()
