class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        length = len(colors)
        count = 0

        # Extend colors to simulate circular behavior
        extended_colors = colors + colors[:k-1]

        # Initial check for the first k-window
        is_alternating = True
        for i in range(k - 1):
            if extended_colors[i] == extended_colors[i + 1]:
                is_alternating = False
                break
        if is_alternating:
            count += 1

        # Sliding window: Check only the entering and exiting element
        for i in range(1, length):
            if extended_colors[i - 1] == extended_colors[i]:  # Exit invalidated
                is_alternating = False
            
            if extended_colors[i + k - 2] == extended_colors[i + k - 1]:  # Enter invalidated
                is_alternating = False

            # Restore if alternating
            if is_alternating:
                count += 1
            else:
                # Recompute if necessary
                is_alternating = True
                for j in range(i, i + k - 1):
                    if extended_colors[j] == extended_colors[j + 1]:
                        is_alternating = False
                        break
                if is_alternating:
                    count += 1

        return count