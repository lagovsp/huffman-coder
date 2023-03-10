import sys
from typing import Any


class HuffmanCoder:
    class Vertex:
        def __init__(self,
                     is_terminal: bool = False,
                     elem: str = None,
                     lower_pred: 'HuffmanCoder.Vertex' = None,
                     greater_pred: 'HuffmanCoder.Vertex' = None):
            self.is_terminal = is_terminal
            self.elem = elem
            self.lower = lower_pred
            self.greater = greater_pred

        def __repr__(self) -> str:
            if self.is_terminal:
                return f'({self.elem})'
            return f'({self.lower} & {self.greater})'

    def __init__(self):
        self.syms_entries = dict[Any, int]()
        self.codes = dict[str, str]()

    def reset_dict(self) -> None:
        self.syms_entries.clear()

    def _create_dict(self, data: str):
        for s in data:
            inserted = False
            for key, val in self.syms_entries.copy().items():
                if not key.is_terminal or not key.elem == s:
                    continue
                self.syms_entries[key] += 1
                inserted = True
                break
            if not inserted:
                self.syms_entries.update({HuffmanCoder.Vertex(is_terminal=True,
                                                              elem=s): 1})

    @staticmethod
    def _extract_min_vertex(src: dict[Any, int]) -> Any:
        lower = min(src.items(), key=lambda x: x[1])
        del src[lower[0]]
        return lower

    def _create_tree(self) -> 'HuffmanCoder.Vertex':
        s_entries = self.syms_entries.copy()

        if not s_entries:
            return HuffmanCoder.Vertex(is_terminal=True)
        if len(s_entries) == 1:
            sym, entries = s_entries.popitem()[0]
            self.codes.update({sym: entries})
            return HuffmanCoder.Vertex(is_terminal=True)

        while not len(s_entries) == 1:
            lower = HuffmanCoder._extract_min_vertex(s_entries)
            greater = HuffmanCoder._extract_min_vertex(s_entries)

            ver = HuffmanCoder.Vertex(lower_pred=lower[0],
                                      greater_pred=greater[0])
            s_entries.update({ver: lower[1] + greater[1]})

        return s_entries.popitem()[0]

    def _set_codes_from_tree(self, ver: Any, prefix=str()) -> None:
        if not ver.is_terminal:
            self._set_codes_from_tree(ver.greater, prefix=prefix[:] + '1')
            self._set_codes_from_tree(ver.lower, prefix=prefix[:] + '0')
            return
        self.codes.update({ver.elem: prefix})

    def encode(self, data: str) -> (list[str], dict[str, str]):
        self._create_dict(data)
        top_ver = self._create_tree()
        self._set_codes_from_tree(top_ver)
        return [self.codes[s] for s in data], self.codes


def main():
    coder = HuffmanCoder()
    coded_data, codes = coder.encode(sys.argv[1])
    print('USED FOLLOWING CODES', codes)
    print('CODED DATA', ' '.join(coded_data))


if __name__ == '__main__':
    main()
