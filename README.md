# 6.2-Lists

### Objective
Practice list manipulation skills by writing functions that modify lists in various ways. Each function includes detailed specifications and example inputs/outputs.

---

### Tasks

1. **Swap First and Last Elements**
   Write a function to swap the first and last elements of a list.
   ```python
   def swap_first_and_last(my_list):
       pass

   # Example function calls:
   print(swap_first_and_last(["cat", "dog", "goldfish"]))  
   # Output: ["goldfish", "dog", "cat"]

   print(swap_first_and_last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  
   # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
   ```

---

2. **Replace Middle Element**
   Replace the middle element of a list with the sum of all its values. If the list has an even number of elements, replace the element just after the middle.
   ```python
   def replace_middle_element(my_list):
       pass

   # Example function calls:
   print(replace_middle_element([1, 2, 3, 4, 5]))  
   # Output: [1, 2, 15, 4, 5]

   print(replace_middle_element([1, 2, 3, 4, 5, 6, 7, 8]))  
   # Output: [1, 2, 3, 4, 36, 6, 7, 8]
   ```

---

3. **Reverse a Subset of the List**
   Reverse the elements between index 2 and index 5 (inclusive).
   ```python
   def reverse_subset(my_list):
       pass

   # Example function calls:
   print(reverse_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  
   # Output: [1, 2, 6, 5, 4, 3, 7, 8, 9, 10]

   print(reverse_subset(["Austin", "Buda", "Georgetown", "Cedar Park", "Manor", "Elgin", "Round Rock", "Leander"]))  
   # Output: ["Austin", "Buda", "Elgin", "Manor", "Cedar Park", "Georgetown", "Round Rock", "Leander"]
   ```

---

4. **Replace Negative Numbers**
   Replace all negative numbers in a list with their absolute values.
   ```python
   def replace_negative_numbers(my_list):
       pass

   # Example function calls:
   print(replace_negative_numbers([-1, 0, 1]))  
   # Output: [1, 0, 1]

   print(replace_negative_numbers([-10, -1, 0, 1, -22]))  
   # Output: [10, 1, 0, 1, 22]
   ```

---

5. **Rotate List Left**
   Rotate the elements of the list `k` positions to the left.
   ```python
     def rotate_list_left(my_list, k):
       pass

      # Example function calls:
      print(rotate_list_left([1, 2, 3, 4, 5], 1))  
      # Output: [2, 3, 4, 5, 1]
   
      print(rotate_list_left(["a", "b", "c", "d", "e", "f"], 3))  
      # Output: ["d", "e", "f", "a", "b", "c"]
   ```

---

6. **Rotate List Right**
   Rotate the elements of the list `k` positions to the right.
   ```python
   def rotate_list_right(my_list, k):
       pass

   # Example function calls:
   print(rotate_list_right([1, 2, 3, 4, 5], 1))  
   # Output: [5, 1, 2, 3, 4]

   print(rotate_list_right(["a", "b", "c", "d", "e", "f"], 3))  
   # Output: ["d", "e", "f", "a", "b", "c"]
   ```
