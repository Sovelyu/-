'''Задача 2. Поиск самой длинной растущей серии

Условие
Дан список целых чисел. Найдите **непрерывную** подпоследовательность, в которой каждое следующее число строго больше предыдущего. Верните длину самой длинной такой серии и её содержимое.
Напишите функцию `longest_increasing_streak(nums: list[int]) -> dict`:
```python
{
"length": 3,
"streak": [2, 5, 9]
}
```
Если серия не найдена (список пуст, длина 1 или все числа убывают/равны), верните `"length": 0, "streak": []`.

### Требования
- Решить за **один проход** по списку (без вложенных циклов)
- Обработать: пустой список, список из 1 элемента, все числа одинаковые, убывающая последовательность
- Если несколько серий одинаковой максимальной длины → вернуть первую встретившуюся


### Пример
```python
nums = [1, 3, 2, 5, 8, 4, 7]
# Выход: {"length": 3, "streak": [2, 5, 8]}
# (серии: [1,3] → 2, [2,5,8] → 3, [4,7] → 2. Макс = 3)
```'''

def longest_increasing_streak(nums: list[int]) -> dict:
    if not nums:
        return {"length": 0, "streak": []}

    current_lenght = 1
    total_lenght = 0
    final_index = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_lenght += 1
        else:
            if current_lenght > total_lenght:
                total_lenght = current_lenght
                final_index = i - total_lenght
            current_lenght = 1

    if current_lenght > total_lenght:
        total_lenght = current_lenght
        final_index = len(nums) - total_lenght


    if total_lenght <= 1:
        return {"length": 0, "streak": []}

    return {
        "length" : total_lenght, # Исправлена опечатка в ключе
        "streak": nums[final_index:final_index+total_lenght],
    }

#Пример
nums = [1, 3, 2, 5, 8, 4, 7, 8]
print(longest_increasing_streak(nums))