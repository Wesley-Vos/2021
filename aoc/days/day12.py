from aoc.util.Day import Day
from collections import defaultdict


class PathFinder:
    def __init__(self, graph, src, des):
        self.graph = graph
        self.src, self.des = src, des
        graph.filter_edges(src, des)

    def _find_path(self, edge, path, double):
        cnt = 0
        for adj in self.graph.get(edge):
            if adj == self.des:
                cnt += 1
            else:
                if adj.islower() and adj in path:
                    if not double:
                        cnt += self._find_path(adj, path.copy() + [adj], True)
                else:
                    cnt += self._find_path(adj, path.copy() + [adj], double)
        return cnt

    def cnt_all_paths(self, double):
        return self._find_path(self.src, [self.src], double)


class Graph:
    def __init__(self, data):
        self.graph = defaultdict(list)
        for row in data:
            src, des = row.split("-")
            self._add_edge(src, des)
            self._add_edge(des, src)
    
    def __str__(self):
        return "\n".join(f"Source {src} is connected to {dess}" for src, dess in self.graph.items())
        
    def _add_edge(self, src, des):
        self.get(src).append(des)

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
