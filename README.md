# testovoe_viborka

Добро пожаловать в мой замечательный скрипт для обработки CSV-файлов!

Cкрипт для обработки CSV-файла, поддерживающий операции:  фильтрацию с операторами «больше», «меньше» и «равно» агрегацию с расчетом среднего (avg), минимального (min) и максимального (max) значения.

## **Основные возможности**

- Легкое фильтрование данных
- Быстрое выполнение агрегации
- Удобная сортировка записей

## **Установка**

Перед началом работы с проектом необходимо установить зависимости, перечисленные в файле `requirements.txt`. Следуйте инструкции ниже:

1. **Клонируйте или скачайте репозиторий с проектом.**

2. **Установите зависимости из файла `requirements.txt`:**

pip install -r requirements.txt


Файл CSV должен находиться в одной директории или нужно прописать путь полностью.

Примеры работы скрипта:

**1. Простой просмотр содержимого CSV-файла:**

  Показывает все данные из файла без каких-либо ограничений.
  
***python main.py products.csv***

![2025-06-18_15-46-08](https://github.com/user-attachments/assets/c8b75833-7284-4b48-b79b-af2274dd4867)

**2. Фильтрация данных:**

  Фильтрует товары с ценой выше определенной суммы.
  
***python main.py products.csv --where "price>500"***

![2025-06-18_16-15-29](https://github.com/user-attachments/assets/3d838f6b-793e-4349-8997-59a5a592b80b)

**3. Агрегация данных:**

  Подсчет среднего значения указанного атрибута (например, средняя оценка товара).
  
***python main.py products.csv --aggregate-column rating --agg-type avg***

![2025-06-18_16-25-48](https://github.com/user-attachments/assets/b16c7000-e9c3-4570-90ed-2b171b782d31)

**4. Совмещённые операции (фильтрация и агрегация):**

  Считаем среднее значение оценки среди товаров с высокой стоимостью.
  
***python main.py products.csv --where "price>500" --aggregate-column rating --agg-type avg***

![2025-06-18_16-25-48](https://github.com/user-attachments/assets/0188753d-f55e-4684-9c83-c4c022e5265d)


**5. Сортировка данных:**

  Упорядочивание товаров по цене в порядке возрастания.
  
***python main.py products.csv --order-by "price=asc"***

![2025-06-18_16-38-48](https://github.com/user-attachments/assets/3aad81b1-277b-48d5-94fe-462a1013f0a2)

**6. Все возможности вместе:**

  Сначала фильтруем товары по стоимости, сортируем по оценке и считаем среднее значение.
  
***python main.py products.csv --where "price>500" --order-by "rating=desc" --aggregate-column rating --agg-type avg***

![2025-06-18_16-42-01](https://github.com/user-attachments/assets/f917c2e1-0d52-45ad-a0de-696adae3ac8a)

***Примечания:***

Все вышеуказанные команды используют одинаковые правила для формирования выражений фильтрации и агрегации.
Аргументы типа --where, --aggregate-column, --agg-type и --order-by являются взаимодополняющими и могут использоваться в любых сочетаниях

**Заключение**

Спасибо за интерес к моему проекту! Надеюсь, он окажется полезным.
