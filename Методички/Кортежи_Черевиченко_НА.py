correct_answers = (
    (1, 1), 
    (2, 2), 
    (3, 3), 
    (4, 2), 
    (5, 1), 
    (6, 2), 
    (7, 1),
    (8, 3),
    (9, 1),
    (10, 2),
    (11, 1),
    (12, 2),
    (13, 3),
    (14, 3),
    (15, 2),
    (16, 1),
    (17, 2),
    (18, 1),
    (19, 2),
    (20, 1))

nums = list(range(1, 21))
answers = list(map(int, input().split()))

if tuple(zip(nums, answers)) == correct_answers:
    print('Экзамен сдан')
else:
    print('Экзамен провален')







                   