# Тесты для проверки BOM файлов

Этот набор тестов проверяет корректность работы модуля `bom.py`.

## Структура

```
test_bom/
├── test_bom.py           # Основной файл с тестами
├── test_data/            # Тестовые BOM файлы
│   ├── Bill of Materials-valid.csv              # Корректный BOM
│   ├── Bill of Materials-empty_part.csv         # С пустыми Part
│   ├── Bill of Materials-empty_description.csv  # С пустыми Description
│   ├── Bill of Materials-empty_designator.csv   # С пустыми Designator
│   ├── Bill of Materials-empty_footprint.csv    # С пустыми Footprint
│   ├── Bill of Materials-m3_component.csv       # С компонентами M3/M4
│   ├── Bill of Materials-wrong_headers.csv      # С неверными заголовками
│   ├── Bill of Materials-extra_empty_line.csv   # С дополнительными пустыми строками
│   └── Bill of Materials-multiple_errors.csv    # С несколькими ошибками
└── README.md             # Этот файл
```

**Примечание**: Тест автоматически создает временные директории для каждого файла, так как функция `bom_check()` работает с директориями, а не с отдельными файлами.

## Тестовые сценарии

### 1. Валидный BOM файл
- **Файл**: `Bill of Materials-valid.csv`
- **Ожидаемый результат**: ✅ Проверка проходит успешно
- **Описание**: Корректный BOM файл со всеми заполненными полями

### 2. Пустые поля Part
- **Файл**: `Bill of Materials-empty_part.csv`
- **Ожидаемый результат**: ❌ Ошибка с указанием элементов
- **Описание**: BOM с незаполненными полями Part в некоторых компонентах

### 3. Пустые поля Description
- **Файл**: `Bill of Materials-empty_description.csv`
- **Ожидаемый результат**: ❌ Ошибка с указанием элементов
- **Описание**: BOM с незаполненными полями Description

### 4. Пустые поля Designator
- **Файл**: `Bill of Materials-empty_designator.csv`
- **Ожидаемый результат**: ❌ Ошибка с указанием номера строки
- **Описание**: BOM с незаполненными полями Designator

### 5. Пустые поля Footprint
- **Файл**: `Bill of Materials-empty_footprint.csv`
- **Ожидаемый результат**: ❌ Ошибка с указанием элементов
- **Описание**: BOM с незаполненными полями Footprint

### 6. Компоненты M3/M4/M5/M6
- **Файл**: `Bill of Materials-m3_component.csv`
- **Ожидаемый результат**: ❌ Ошибка о неисключенных компонентах
- **Описание**: BOM содержит компоненты M3/M4, которые должны быть исключены

### 7. Неправильные заголовки
- **Файл**: `Bill of Materials-wrong_headers.csv`
- **Ожидаемый результат**: ❌ Ошибка о неверных заголовках
- **Описание**: BOM с неправильными названиями столбцов

### 8. Дополнительные пустые строки
- **Файл**: `Bill of Materials-extra_empty_line.csv`
- **Ожидаемый результат**: ❌ Ошибка о пустой строке
- **Описание**: BOM содержит пустую строку не на второй позиции (первая пустая строка игнорируется)

### 9. Множественные ошибки
- **Файл**: `Bill of Materials-multiple_errors.csv`
- **Ожидаемый результат**: ✅ Проверка проходит (валидный файл для будущих тестов)
- **Описание**: Файл для тестирования множественных ошибок

## Запуск тестов

Для запуска тестов необходим pytest. Установите зависимости:

```bash
pip install -r requirements.txt
```

Или установите pytest напрямую:
```bash
pip install pytest
```

### Из директории test_bom:
```bash
pytest test_bom.py -v
```

### Из корневой директории pcb_checker:
```bash
pytest test_bom/test_bom.py -v
```

### Запуск конкретного теста:
```bash
pytest test_bom.py::test_valid_bom -v
```

### Запуск с детальным выводом:
```bash
pytest test_bom.py -vv
```

### Запуск с остановкой на первой ошибке:
```bash
pytest test_bom.py -x
```

## Интерпретация результатов

Pytest выводит результаты в стандартном формате:
- `.` - тест пройден
- `F` - тест провален
- `E` - ошибка выполнения теста

В конце выводится итоговая статистика с количеством пройденных и проваленных тестов.

Пример вывода:
```
test_bom.py::test_valid_bom PASSED                                  [ 11%]
test_bom.py::test_bom_errors[Bill of Materials-empty_part.csv-...] PASSED [ 22%]
...
========================== 9 passed in 0.15s ===========================
```

## Добавление новых тестов

### Для тестов с ошибками:

Добавьте параметры в декоратор `@pytest.mark.parametrize` функции `test_bom_errors`:

```python
@pytest.mark.parametrize("test_file,expected_error", [
    # ... существующие тесты ...
    ("Bill of Materials-<новый_тест>.csv", "текст ожидаемой ошибки"),
])
```

### Для специфичных тестов:

Создайте отдельную функцию теста:

```python
def test_custom_check(temp_bom_dir):
    """Описание теста"""
    test_file = os.path.join(TEST_DATA_DIR, "Bill of Materials-custom.csv")
    success, output = run_bom_check(test_file, temp_bom_dir)
    
    assert not success, "Ожидалась ошибка"
    assert "текст ошибки" in output, "Ожидаемая ошибка не найдена"
```

## Примечания

- Первая пустая строка после заголовка (строка 2) игнорируется, так как это стандартная строка Altium
- Все остальные пустые строки должны вызывать ошибку
- Модуль проверяет все ошибки в BOM и выводит их все разом
- Тесты используют перехват stdout для анализа вывода
