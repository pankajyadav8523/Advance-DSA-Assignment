"""
This script is about to displaying maximal point from a set of points given by user.
Here I will use two algorithms first(left to right sweep) and  second(right to left sweep).

Author : Pankaj Yadav
Date : 28th January, 2024
"""


class MaximalPoint:
    """This class deals with the maximal point."""

    def __init__(self, length):
        """It initializes the length attribute."""
        self._length = length
        self._list = []

    def userInput(self, input_coordinates):
        """This method is converting user input coordinates into a list of tuples."""
        self._list.append(input_coordinates)

    def sort_x_coordinate(self):
        """It sorts the x-coordinate of points using the merge sort algorithm."""
        self._merge_sort(self._list)

    def _merge_sort(self, arr):
        """It is a helper method used for sorting the x-coordinate of points."""
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self._merge_sort(left_half)
            self._merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][0] > right_half[j][0]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def _reverse_points_ascending(self):
        """Converting the points into ascending order."""
        mid = self._length // 2
        for i in range(mid):
            self._list[i], self._list[self._length-1-i] = self._list[self._length-1-i], self._list[i]

    def left_to_right_sweep(self):
        """Left-to-right sweep algorithm for finding the maximal point."""
        self._reverse_points_ascending()
        print("Display the maximal points using left to right algorithm:")
        comparison_ltr = 0
        candidate_list = []
        for i in range(self._length):
            comparison_ltr += 1
            while candidate_list and self._list[i][1] > candidate_list[-1][1]:
                comparison_ltr += 1
                candidate_list.pop()
            candidate_list.append(self._list[i])

        for i in range(len(candidate_list)):
            print(candidate_list[i])
        print("no. of comaparison in left to right : ",comparison_ltr)

    def right_to_left_sweep(self):
        """Right-to-left sweep algorithm for finding the maximal point."""
        previous = self._list[0]
        print("Display the maximal points using right to left algorithm:")
        print(previous)
        comparison_rtl = 0
        for i in range(1, self._length):
            current = i
            comparison_rtl += 1
            if previous[1] <= self._list[current][1]:
                print(self._list[current])
                previous = self._list[current]
        print("no. of comaparison in right to left : ",comparison_rtl)

if __name__ == "__main__":
    try:
        inp = int(input("Enter the no. of points you want to enter: "))
        m = MaximalPoint(inp)
        for _ in range(inp):
            inp_str = input("Enter the co-ordinates of points separated by space: ")
            coordinates = tuple(map(float, inp_str.split()))
            m.userInput(coordinates)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    # Perform sorting by x-coordinate
    m.sort_x_coordinate()

    # Perform right-to-left sweep
    m.right_to_left_sweep()

    # Perform left-to-right sweep
    m.left_to_right_sweep()