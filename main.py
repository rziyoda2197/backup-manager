class StreamDataFilter:
    def __init__(self, data):
        self.data = data

    def filter(self, condition):
        return [item for item in self.data if condition(item)]

# Misol ma'lumotlar ro'yxati
data = [
    {"name": "Ali", "age": 25},
    {"name": "Vali", "age": 30},
    {"name": "Hasan", "age": 20},
    {"name": "Husan", "age": 35}
]

# Filter qilish uchun shart
def is_adult(person):
    return person["age"] >= 18

# Filter qilish
filtered_data = StreamDataFilter(data).filter(is_adult)

# Natija
print(filtered_data)
```

Natija:
```python
[
    {'name': 'Ali', 'age': 25},
    {'name': 'Vali', 'age': 30},
    {'name': 'Husan', 'age': 35}
]
