class BricksAndWaterPython:

    def how_much_water(bricks_array: list) -> int:
        water = 0
        length = len(bricks_array)

        for i in range(1, length - 1):
            # print(f"i: {i}")
            left_height = bricks_array[:i]          # von element aus die höhe von den linken säulen
            # print(f"left_height: {left_height}")
            right_height = bricks_array[i + 1:]     # von element aus die höhe von den rechten säulen aus
            # print(f"right_height: {right_height}")
            lower_height = min(max(left_height), max(right_height)) - bricks_array[i]
            water += max(lower_height, 0)

        return water

print("Water: ", BricksAndWaterPython.how_much_water([2, 0, 3, 0, 4] ))
