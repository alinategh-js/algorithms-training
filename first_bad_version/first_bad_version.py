def isBadVersion(version: int):
    return version >= 2


class Solution:
    def firstBadVersion(self, n: int) -> int:
        pointers_list = [1, int(n/2), n]
        while True:
            for index, version in enumerate(pointers_list):
                isBad = isBadVersion(version)
                if isBad:
                    if index != 0:
                        return self.linearFirstBadVersion(pointers_list[index - 1], version)
                    else:
                        return 1

            # new_pointers_list = []
            # for index, version in enumerate(pointers_list):
            #     if index != len(pointers_list) - 1:
            #         new_pointers_list.append(version)
            #         new_pointers_list.append(
            #             int((pointers_list[index+1] + version)/2))

            # pointers_list = new_pointers_list.copy()

    def linearFirstBadVersion(self, start_version, end_version):
        left_pointer = start_version
        right_pointer = end_version
        current_pointer = (left_pointer + right_pointer) // 2
        bad_version = -1
        while left_pointer <= right_pointer:
            current_pointer = (left_pointer + right_pointer) // 2
            isBad = isBadVersion(current_pointer)
            if isBad:
                right_pointer = current_pointer - 1
                bad_version = current_pointer
            else:
                left_pointer = current_pointer + 1

        return bad_version

s = Solution()
print(s.firstBadVersion(3))
