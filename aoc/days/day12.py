from aoc.util.Day import Day
from collections import defaultdict


class PathFinder:
    def __init__(self, graph, src, des):
        self.graph = graph
        self.src, self.des = src, des
        graph.filter_edges(src, des)

    def _find_path(self, edge, path, double_small):
        cnt = 0
        if edge == self.des:
            return 1

        for adj in self.graph.get(edge):
            if adj.islower() and adj in path:
                cnt += self._find_path(adj, path.copy() + [adj], True) if not double_small else 0
            else:
                cnt += self._find_path(adj, path.copy() + [adj], double_small)
        return cnt

    def cnt_all_paths(self, double_small):
        return self._find_path(self.src, [self.src], double_small)


class Graph:
    def __init__(self, data):
        self.graph = defaultdict(list)
        for src, des in map(lambda r: r.split("-"), data):
            self._add_edge(src, des)

    def __str__(self):
        return "\n".join(f"Source {src} is connected to {dess}" for src, dess in self.graph.items())

    def _add_edge(self, src, des, bi=True):
        self.get(src).append(des)
        if bi: 
            self.get(des).append(src)

    def filter_edges(self, src, des):
        self.graph.pop(des)
        for edge, ads in self.graph.items():
            self.graph[edge] = [ad for ad in ads if ad != src]

    def get(self, key):
        return self.graph[key]


class Day12(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.graph = Graph(self.data)
        self.path_finder = PathFinder(self.graph, "start", "end")

    def solve_part1(self):
        return self.path_finder.cnt_all_paths(True)

    def solve_part2(self):
        return self.path_finder.cnt_all_paths(False)


def main():
    day = Day12("day12.in")
    day.run()


if __name__ == "__main__":
    main()
