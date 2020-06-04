#include <iostream>
#include <conio.h>
#include <time.h>
using namespace std;

int main()
{
	int *arr; // вказівник для виділення пам'яті під масив
	int size; // розмір масиву

	// Введення кількості елементів масиву
	cout << "Array size = ";
	cin >> size;

	if (size <= 0) { // Перевірка чи розмір масиву є додатнім
		cerr << "Invalid size" << endl;
		return 1;
	}

	arr = new int[size]; // Виділення пам'яті під масив

	srand(time(NULL));

	// Заповнення масиву рандомними числами
	for (int i = 0; i < size; i++) {
		arr[i] = 1 + rand() % 1000;

	}

	// Виведення не відсортованого масиву
	cout << "Array before sorting:";
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
	int temp; // Змінна для обміну елементами масиву 

	// Сортування бульбашкою
	for (int i = 0; i < size - 1; i++) {
		for (int j = 0; j < size - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				// Зміна місця змінних
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}

	// Виведення відсортованого масиву
	cout << "Array after sorting:";
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
	_getch();
	delete[] arr; // Звільнення пам'яті

	return 0;
}