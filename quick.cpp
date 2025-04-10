#include <iostream>
#include <ctime>

void Initialize(int arr[], size_t size);
void Show(const int arr[], size_t size);

template <typename T>
void QuickSort(T arr[], int first, int last);

int main()
{
    srand(static_cast<unsigned>(time(nullptr)));

    const int SIZE = 10;
    int arr[SIZE];

    Initialize(arr, SIZE);
    Show(arr, SIZE);

    // Sorting
    QuickSort(arr, 0, SIZE - 1);

    Show(arr, SIZE);

    return 0;
}

void Initialize(int arr[], size_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        arr[i] = rand() % 100;
    }
}

void Show(const int arr[], size_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

template <typename T>
void QuickSort(T arr[], int first, int last)
{
    T middle = arr[(first + last) / 2];
    int i = first;
    int j = last;

    do
    {
        while (arr[j] > middle) // 2
            j--;
        while (arr[i] < middle) // 3
            i++;

        if (i <= j)             // 4
        { 
            std::swap(arr[i], arr[j]);
            i++;
            j--;
        }

    } while (i <= j); // 5

    if (j > first)
        QuickSort(arr, first, j);
    if (i < last)
        QuickSort(arr, i, last);
}





// 1. Взяти центральний елемент
// 2. В циклі знайти елемент справа від центрального елемента, який менший за нього
// 3. В циклі знайти елемент зліва від центрального елемента, який більший за нього
// 4. Поміняти місцями найдені значення якщо їх індекси не перетнулись
// 5. Виконати дії 2-4 поки індекси не перетнулись 
// 6. Рекурсивно виконати дії 1-5 для лівої частини масиву, якщо правий індекс не дійшов до початку 
// 7. Рекурсивно виконати дії 1-5 для правої частини масиву, якщо лівий індекс не дійшов до кінця 