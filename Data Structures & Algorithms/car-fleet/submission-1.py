class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack=[]
        print(cars)

        for p, s in cars:
            d = (target - p)/s
            
            if not stack or stack[-1] < d:
                stack.append(d)
            print(stack)
        return len(stack)