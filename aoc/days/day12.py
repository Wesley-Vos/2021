from aoc.util.Day import Day

class Graph:
    def __init__(self, data):
        self.graph = {}
        for row in data:
            src, des = row.split("-")
            self._add_edge(src, des)
            self._add_edge(des, src)
        self._SMALL = [v for v in self.graph.keys() if v.islower()]
    
    def __str__(self):
        out = ""
        for src, dess in self.graph.items():
            out += f"Source {src} is connected to {dess}\n"
        return out
        
    def _add_edge(self, src, des):
        if src != "end" and des != "start":
            if src in self.graph:
                self.graph.get(src).append(des)
            else:
                self.graph[src] = [des]
        
    def _find_path(self, src, des, path, double):
        cnt = 0
        for adj in self.graph.get(src):
            if adj == des:
                path.append(adj)
                cnt += 1
            else:
                if adj in self._SMALL and adj in path:
                    if double:
                        continue
                    else:
                        cnt += self._find_path(adj, des, path.copy() + [adj], True)
                else:
                    cnt += self._find_path(adj, des, path.copy() + [adj], double)
        return cnt   
        
    def cnt_all_paths(self, src, des, double):
        return self._find_path(src, des, [src], double)
        

class Day12(Day):
    def __init__(self, filename):
        super().__init__(filename)
        self.graph = Graph(self.data)
        
    def solve_part1(self):
        return self.graph.cnt_all_paths("start", "end", True)

    def solve_part2(self):
        # return 0
        return self.graph.cnt_all_paths("start", "end", False)


def main():
    day = Day12("day12.in")
    day.run()


if __name__ == "__main__":
    main()
