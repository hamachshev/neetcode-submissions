class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        in_order = sorted(list(zip(position, speed)),key=lambda x: x[0])
        fleets = 1 if len(position) >= 1 else 0

        while len(in_order) > 1:
            car = in_order.pop()
            cycles = (target - car[0]) / car[1]

            car2 = in_order[-1]

            if car2[0] + car2[1] * cycles < target:
                fleets += 1
            else:
                in_order.pop()
                in_order.append(car)

        return fleets