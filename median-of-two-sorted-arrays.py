def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        i1 = -1
        i2 = -1
        last = 0
        last_last = 0
        if n % 2 == 0:
            for i in range(int(n / 2) + 1):
                if i1 + 1 > len(nums1) - 1:
                    i2 += 1
                    last_last = last
                    last = nums2[i2]
                elif i2 + 1 > len(nums2) - 1:
                    i1 += 1
                    last_last = last
                    last = nums1[i1]
                else:
                    if nums1[i1 + 1] < nums2[i2 + 1]:
                        i1 += 1
                        last_last = last
                        last = nums1[i1]
                    else:
                        i2 += 1
                        last_last = last
                        last = nums2[i2]
            return (last + last_last) / 2
        else:
            for i in range(int(n / 2) + 1):
                if i1 + 1 > len(nums1) - 1:
                    i2 += 1
                    last = nums2[i2]
                elif i2 + 1 > len(nums2) - 1:
                    i1 += 1
                    last = nums1[i1]
                else:
                    if (nums1[i1 + 1] < nums2[i2 + 1]):
                        i1 += 1
                        last = nums1[i1]
                    else:
                        i2 += 1
                        last = nums2[i2]

            return last
        