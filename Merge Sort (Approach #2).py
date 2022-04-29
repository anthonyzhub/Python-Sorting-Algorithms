def merge(self, strList, leftPtr, midPtr, rightPtr):

      # OBJECTIVE: Create 2 temporary lists representing each half of the original list,
      #               then slowly update element's value at index inside of original list

      # Create 2 new list
      sizeA = midPtr - leftPtr + 1
      sizeB = rightPtr - midPtr

      # Copy elements from original list to 2 new lists
      leftHalf = [""] * sizeA
      for i in range(sizeA):
          leftHalf[i] = strList[leftPtr + i]

      rightHalf = [""] * sizeB
      for i in range(sizeB):
          rightHalf[i] = strList[midPtr + 1 + i]

      # Create 3 pointers
      i = 0
      j = 0
      originalPtr = 0

      # Traverse strList
      while i < sizeA and j < sizeB:

          # If leftHalf's element is bigger than rightHalf's, add rightHalf's element first
          if leftHalf[i] >= rightHalf[j]:
              strList[originalPtr] = rightHalf[j]
              j += 1

          else:
              strList[originalPtr] = leftHalf[i]
              i += 1

          originalPtr += 1

      # Add remaining elements from leftHalf
      while i < sizeA:
          strList[originalPtr] = leftHalf[i]
          i += 1
          originalPtr += 1

      # Add remaining elements from rightHalf
      while j < sizeB:
          strList[originalPtr] = rightHalf[j]
          j += 1
          originalPtr += 1

  def mergeSort(self, strList, leftPtr, rightPtr):

      # OBJECTIVE: Split list by half until one element is left

      # Check that both pointers don't overlap
      if leftPtr < rightPtr:

          # Calculate middle index
          midPtr = (leftPtr + rightPtr) // 2

          # Continue to split list
          self.mergeSort(strList, leftPtr, midPtr)
          self.mergeSort(strList, midPtr + 1, rightPtr)

          # Merge list
          self.merge(strList, leftPtr, midPtr, rightPtr)

  def solOne(self, str1, str2):

      # OBJECTIVE: Check if both strings are permutations of one another

      # If both strings aren't equal in length, then return false
      if len(str1) != len(str2):
          return False

      # Turn both strings into lists
      str1 = list(str1)
      str2 = list(str2)

      # Sort both strings
      self.mergeSort(str1, 0, len(str1) - 1)
      self.mergeSort(str2, 0, len(str2) - 1)

      # Compare both lists
      return str1 == str2
