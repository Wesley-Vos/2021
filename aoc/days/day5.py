from aoc.util.Day import Day


class HTV:
    class Line:
        def __init__(self, start, end):
            self.start = start
            self.end = end 
    
    
    def __init__(self, data):
        self.hor = {}
        self.vert = {}
        self.diag = []
        self.maxx = 0
        self.maxy = 0
        for row in data:
            start, end = row.split(" -> ")
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            self.maxx = max(self.maxx, x2)
            self.maxy = max(self.maxy, y2)
            if x1 == x2:    #vert
                y1, y2 = sorted((y1, y2))
                if x1 in self.vert:
                    self.vert[x1].append((y1, y2))
                else:
                    self.vert[x1] = [(y1, y2)]
            elif y1 == y2:    #horiz
                x1, x2 = sorted((x1, x2))
                if y1 in self.hor:
                    self.hor[y1].append((x1, x2))
                else:
                    self.hor[y1] = [(x1, x2)]
            elif abs(x1 - x2) == abs(y1 - y2):
                # (x1 == y1 and x2 == y2) or (x1 == y2 and x2 == y1):
                #(x1, y1), (x2, y2) = sorted(((x1, y1), (x2, y2)))
                self.diag.append(((x1, y1), (x2, y2)))
            else:
                pass
        
    def cnt(self):
        start = (0, 0)
        maxx = 0
        maxy = 0
           
        end = (self.maxx, self.maxy)
        print(end)
        #return 0
        
        data = [[0 for _ in range(0, end[0] + 2)] for _ in range(0, end[1] + 2)]

        #print("\n".join(map(lambda r: " ".join(map(str, r)), data)))
        
        for idx, row in self.hor.items():
            for x1, x2 in row:
                for i in range(x1, x2 + 1):
                    data[idx][i] += 1
                    
                    
        for idx, row in self.vert.items():
            for y1, y2 in row:
                for i in range(y1, y2 + 1):
                    data[i][idx] += 1
                    
        for row in self.diag:
            #print(row)
            if row[0][0] == 1 + row[0][1]:
                for i in range(row[0][0], row[1][0] + 1):
                    #print(i, i)
                    data[i][i] += 1
            else:
                row = sorted(row)
                #print(row)
                (x1, y1), (x2, y2) = row
                amount = abs(x1 - x2)
                
                if x2 > x1:
                    xran = list(range(x1, x2 + 1))
                else:
                    xran = list(range(x2, x1 + 1))
                    xran.sort(reverse=True)

                #print(y1, y2)
                if y2 > y1:
                    yran = list(range(y1, y2 + 1))
                else:
                    #print(list(range(y2, y1 + 1)))
                    yran = list(range(y2, y1 + 1))
                    yran.sort(reverse = True)
                    
                #print(xran)
                #print(yran)
                    
                for i in range(0, amount + 1):
                    #print(xran[i], yran[i])
                    data[yran[i]][xran[i]] += 1
        
        res = 0
        for row in data:
            res += len(list(filter(lambda c: c >= 2, row)))
        
        
        return res


class Day5(Day):

    def __init__(self, filename):
        super().__init__(filename)
        
    def solve_part1(self):
        htv = HTV(self.data)
        return htv.cnt()

    def solve_part2(self):
        return 0


def main():
    day = Day5("day5.in")
    day.run()


if __name__ == "__main__":
    main()
