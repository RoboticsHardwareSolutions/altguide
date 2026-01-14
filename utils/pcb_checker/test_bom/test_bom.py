#!/usr/bin/env python3
"""
Тесты для проверки BOM файлов.
Запуск: python test_bom.py
"""

import sys
import os
import shutil
import tempfile
from io import StringIO

# Добавляем родительскую директорию в путь для импорта модулей
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bom import bom_check


class TestResult:
    """Класс для хранения результатов теста"""
    def __init__(self, name, passed, message=""):
        self.name = name
        self.passed = passed
        self.message = message


def run_test(test_name, test_file_path, should_fail=False, expected_error=None):
    """
    Запускает один тест BOM проверки
    
    Args:
        test_name: Название теста
        test_file_path: Полный путь к тестовому BOM файлу
        should_fail: Ожидается ли ошибка (True) или успех (False)
        expected_error: Текст, который должен присутствовать в сообщении об ошибке
    
    Returns:
        TestResult: Результат теста
    """
    print(f"\n{'='*60}")
    print(f"Тест: {test_name}")
    print(f"{'='*60}")
    
    # Создаем временную директорию и копируем туда файл
    temp_dir = tempfile.mkdtemp()
    try:
        # Копируем тестовый файл как "Bill of Materials.csv"
        temp_file = os.path.join(temp_dir, "Bill of Materials.csv")
        shutil.copy2(test_file_path, temp_file)
        
        # Перехватываем stdout для анализа вывода
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            bom_check(temp_dir + "/")
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            if should_fail:
                print(f"❌ FAILED: Ожидалась ошибка, но проверка прошла успешно")
                return TestResult(test_name, False, "Ожидалась ошибка, но проверка прошла успешно")
            else:
                print(f"✅ PASSED: Проверка прошла успешно")
                if output.strip():
                    print(f"Вывод: {output.strip()}")
                return TestResult(test_name, True)
                
        except SystemExit as e:
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            
            if not should_fail:
                print(f"❌ FAILED: Неожиданная ошибка")
                print(f"Вывод: {output.strip()}")
                return TestResult(test_name, False, f"Неожиданная ошибка: {output.strip()}")
            else:
                # Проверяем, содержит ли вывод ожидаемую ошибку
                if expected_error and expected_error not in output:
                    print(f"❌ FAILED: Получена ошибка, но не та, что ожидалась")
                    print(f"Ожидалось: {expected_error}")
                    print(f"Получено: {output.strip()}")
                    return TestResult(test_name, False, f"Ошибка не соответствует ожидаемой")
                else:
                    print(f"✅ PASSED: Получена ожидаемая ошибка")
                    print(f"Вывод: {output.strip()}")
                    return TestResult(test_name, True)
        
        except Exception as e:
            sys.stdout = old_stdout
            print(f"❌ FAILED: Неожиданное исключение: {str(e)}")
            return TestResult(test_name, False, f"Неожиданное исключение: {str(e)}")
    
    finally:
        # Удаляем временную директорию
        shutil.rmtree(temp_dir, ignore_errors=True)


def main():
    """Запускает все тесты"""
    print("="*60)
    print("ЗАПУСК ТЕСТОВ BOM ПРОВЕРКИ")
    print("="*60)
    
    # Получаем путь к директории с тестовыми данными
    test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")
    
    # Определяем тесты
    tests = [
        {
            "name": "Валидный BOM файл",
            "file": "Bill of Materials-valid.csv",
            "should_fail": False
        },
        {
            "name": "BOM с пустыми полями Part",
            "file": "Bill of Materials-empty_part.csv",
            "should_fail": True,
            "expected_error": "поля Part в элементе"
        },
        {
            "name": "BOM с пустыми полями Description",
            "file": "Bill of Materials-empty_description.csv",
            "should_fail": True,
            "expected_error": "поля Description в элементе"
        },
        {
            "name": "BOM с пустыми полями Designator",
            "file": "Bill of Materials-empty_designator.csv",
            "should_fail": True,
            "expected_error": "поля Designator в строке"
        },
        {
            "name": "BOM с пустыми полями Footprint",
            "file": "Bill of Materials-empty_footprint.csv",
            "should_fail": True,
            "expected_error": "поля Footprint в элементе"
        },
        {
            "name": "BOM с компонентами M3/M4",
            "file": "Bill of Materials-m3_component.csv",
            "should_fail": True,
            "expected_error": "компоненты"
        },
        {
            "name": "BOM с неправильными заголовками",
            "file": "Bill of Materials-wrong_headers.csv",
            "should_fail": True,
            "expected_error": "заголовков"
        },
        {
            "name": "BOM с дополнительной пустой строкой",
            "file": "Bill of Materials-extra_empty_line.csv",
            "should_fail": True,
            "expected_error": "пустая строка"
        },
    ]
    
    # Запускаем тесты
    results = []
    for test in tests:
        test_file_path = os.path.join(test_data_dir, test["file"])
        result = run_test(
            test["name"],
            test_file_path,
            test.get("should_fail", False),
            test.get("expected_error", None)
        )
        results.append(result)
    
    # Выводим итоги
    print("\n" + "="*60)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("="*60)
    
    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)
    total = len(results)
    
    print(f"\nВсего тестов: {total}")
    print(f"✅ Пройдено: {passed}")
    print(f"❌ Провалено: {failed}")
    
    if failed > 0:
        print("\nПроваленные тесты:")
        for result in results:
            if not result.passed:
                print(f"  - {result.name}")
                if result.message:
                    print(f"    {result.message}")
    
    print("\n" + "="*60)
    
    # Возвращаем код выхода
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
