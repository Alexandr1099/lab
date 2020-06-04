#include <cstdlib>
#include <iostream>
#include <time.h>
#include <conio.h>

using namespace std;

int main() {
	
	int *arr; // �������� ��� �������� ���'�� �� �����
	int size; // ����� ������

	// �������� ������� �������� ������
	cout << "Array size = ";
	cin >> size;
	arr = new int[size]; // �������� ���'�� �� �����

	srand(time(NULL));
	// ���������� ������ ���������� �������
	for (int i = 0; i < size; i++) {
		arr[i] = 1 + rand() % 1000;
	}
	// ��������� �� ������������� ������
	cout << "Array before sorting:";
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
	// ����������� ����� ����������
	int step = size / 2;
	// ���� ���� �� ����� 0
	while (step > 0) {
		for (int i = 0; i < (size - step); i++) {
			int j = i;
			while (j >= 0 && arr[j] > arr[j + step]) {
				// ���� �� ������� �� ������� ������
				// � ���� ������������ ������� �����
				// �� ������� ���� ����������� �� ������ �����
				// ������ �������� ������
				int exch = arr[j];
				arr[j] = arr[j + step];
				arr[j + step] = exch;
				j--;
			}
		}
		// �������� ���� � ���
		step = step / 2;
	}
	// ��������� ������������� ������
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