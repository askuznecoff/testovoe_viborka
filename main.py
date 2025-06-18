import argparse
import csv
import re
from typing import List, Dict, Tuple
from tabulate import tabulate


class Condition:
    def __init__(self, condition_str: str):
        pattern = r'^(\w+)\s*(<=|>=|=|>|<)\s*([\d.]+)$'
        match = re.match(pattern, condition_str)
        if not match:
            raise ValueError(f"Invalid condition format '{condition_str}'. Expected 'column operator value'.")

        self.column = match.group(1)
        self.operator = match.group(2)
        self.value = float(match.group(3))

    def matches(self, row: Dict[str, str]):
        cell_value = float(row[self.column])
        match self.operator:
            case '>':
                return cell_value > self.value
            case '<':
                return cell_value < self.value
            case '=':
                return cell_value == self.value
            case '>=':
                return cell_value >= self.value
            case '<=':
                return cell_value <= self.value
            case _:
                raise ValueError(f"Unknown operator '{self.operator}'")


def load_csv(file_path: str) -> List[Dict]:
    with open(file_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)


def filter_data(data: List[Dict], conditions: List[Condition]) -> List[Dict]:
    filtered_data = []
    for row in data:
        if all(condition.matches(row) for condition in conditions):
            filtered_data.append(row)
    return filtered_data


def calculate_aggregation(data: List[Dict], column: str, aggregation_type: str) -> float:
    values = [float(row[column]) for row in data]

    if aggregation_type == 'avg':
        return sum(values) / len(values)
    elif aggregation_type == 'min':
        return min(values)
    elif aggregation_type == 'max':
        return max(values)
    else:
        raise ValueError(f"Unknown aggregation type '{aggregation_type}'")


def display_result(aggregation_type: str, result: float) -> None:
    """
    Лаконичный вывод результата агрегации с динамическим выравниванием.
    """
    # Определяем общую ширину для централизации и вывода
    title_width = max(len(aggregation_type.upper()), len(str(result))) + 2  # прибавляем запас на красоту
    separator = "-" * title_width
    border = "+" + "-" * title_width + "+"

    # Центрированный заголовок
    centered_title = f"{aggregation_type.upper():^{title_width}}"
    # Центральное размещение результата
    centered_result = f"{result:.2f}".center(title_width)

    print(border)
    print(f"| {centered_title} |")
    print(f"+{separator}+")
    print(f"| {centered_result} |")
    print(border)


def process_csv(file_path: str, where_conditions: List[str], aggregation_column: str = None,
                aggregation_type: str = None, order_by: str = None) -> None:
    data = load_csv(file_path)
    conditions = [Condition(cond) for cond in where_conditions]
    filtered_data = filter_data(data, conditions)

    # Сортируем данные, если задан аргумент '--order-by'
    if order_by:
        col, direction = order_by.split('=')
        reverse = True if direction.lower() == 'desc' else False
        filtered_data.sort(key=lambda row: float(row[col]), reverse=reverse)

    if aggregation_column and aggregation_type:
        result = calculate_aggregation(filtered_data, aggregation_column, aggregation_type)
        display_result(aggregation_type, result)
    else:
        print(tabulate(filtered_data, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CSV Filter & Aggregation Tool')
    parser.add_argument('file', help='Path to the input CSV file.')
    parser.add_argument('--where', nargs='+', help='Filter conditions like "rating>4.7"', default=[])
    parser.add_argument('--aggregate-column', help='Column to perform aggregation on.', default=None)
    parser.add_argument('--agg-type', choices=['avg', 'min', 'max'], help='Type of aggregation.', default=None)
    parser.add_argument('--order-by', help='Order results by column and direction (like "price=asc")', default=None)
    args = parser.parse_args()
    process_csv(args.file, args.where, args.aggregate_column, args.agg_type, args.order_by)