import sys
import yaml
import re


def parse_line(line):
    """Парсинг одной строки."""
    # Убираем комментарии
    line = re.sub(r'/\#.*?\#/', '', line)  # Удаляем многострочные комментарии

    # Обрабатываем массивы [value1; value2; ...]
    if line.startswith('[') and line.endswith(']'):
        values = line[1:-1].split(';')
        return [parse_value(value.strip()) for value in values]

    # Обрабатываем строки
    if line.startswith("'") and line.endswith("'"):
        return line[1:-1]  # Убираем кавычки

    # Обрабатываем числа
    try:
        return int(line)  # Пробуем преобразовать в число
    except ValueError:
        return line.strip()  # Если не число, то просто возвращаем строку


def parse_value(value):
    """Парсинг значений (строки, числа, массивы)."""
    value = value.strip()
    if value.startswith("["):
        return parse_line(value)
    elif value.startswith("'"):
        return parse_line(value)
    else:
        return int(value) if value.isdigit() else value


def parse_config(text):
    """Парсинг текста конфигурации."""
    result = {}
    lines = text.splitlines()

    for line in lines:
        if line.strip() == '':
            continue

        # Проверяем на декларации констант
        if ":=" in line:
            name, value = line.split(":=")
            result[name.strip()] = parse_value(value.strip())

        # Проверяем на вычисления констант
        elif "@(" in line and ")" in line:
            name = line[2:-1].strip()
            if name in result:
                result[name] = result[name]
            else:
                print(f"Ошибка: Константа {name} не определена.")
                sys.exit(1)

    return result


def main():
    """Основная функция для обработки командной строки."""
    if len(sys.argv) < 2:
        print("Ошибка: Необходимо указать файл конфигурации.")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    config_data = parse_config(text)
    yaml.dump(config_data, sys.stdout, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    main()
