#include <cstdlib>
#include <iostream>
#include <time.h>
#include <conio.h>

using namespace std;

int main() {
	
	int *arr; // Вказівник для виділення пам'яті під масив
	int size; // Розмір масиву

	// Введення кількості елементів масиву
	cout << "Array size = ";
	cin >> size;
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
	// Ініціалізація кроку сортування
	int step = size / 2;
	// Поки крок не рівний 0
	while (step > 0) {
		for (int i = 0; i < (size - step); i++) {
			int j = i;
			while (j >= 0 && arr[j] > arr[j + step]) {
				// Поки не прийшли до початку масиву
				// і поки розглядається елемент більше
				// ніж елемент який знаходиться на відстані кроку
				// міняємо елементи місцями
				int exch = arr[j];
				arr[j] = arr[j + step];
				arr[j + step] = exch;
				j--;
			}
		}
		// зменшуємо крок в двоє
		step = step / 2;
	}
	// Виведення відсортованого масиву
	cout << endl;
	cout << "Array after sorting:";
	for (int i = 0; i < size; i++)
	{
		cout << arr[i] << ' ';
	}

	delete[] arr;
	_getch();
	
	return 0;
}