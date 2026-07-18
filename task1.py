def process_grades(records: list[str]) -> dict:
    valid_count = 0
    average = 0
    passed = set()
    skipped = 0

    for record in records:
        if not record or ":" not in record:
            skipped += 1
            continue


        name, score = record.split(": ", 1)

        if not score.isdigit() or not name:
            skipped += 1
            continue

        score = int(score)

        if score > 100 or score < 0:
            skipped += 1
            continue

        valid_count += 1
        average += score
        if score >= 60:
            passed.add(name)  # Добавляем в множество

    average = round(average / valid_count, 1) if valid_count > 0 else 0.0

    return {
        "valid_count": valid_count,
        "average": average,
        "passed": sorted(list(passed)),
        "skipped": skipped
    }


data = [
"Иванов: 85",
"Петров: 42",
"Сидоров: abc", # битая
"Козлов: 90",
": 55", # битая
"Иванов: 70" # повтор (считаем как отдельную запись)
]
print(process_grades(data))