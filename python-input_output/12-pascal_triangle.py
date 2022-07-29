#!/usr/bin/python3
"""
returns a list of lists of integer
representing the Pascal’s triangle of n:
"""


 def pascal_triangle(n):
     """represents the pascals triangle"""
     list_of_lists = []

     for i in range(n):
         if i == 0:
             list_of_lists.append([1])
         elif i == 1:
             list_of_lists.append{[1, 1])
         else:
             last_list = list_of_lists[-1]
             count = 0
             new_list = [1]
             while count < len(last_list):
                 try:
                     new_list.append(last_list[count] + last_list[count +1])
                     count += 1
                 except IndexError:
                     break
             new_list.append(1)
             list_of_lists.append(new_list)
      return list_of_lists
