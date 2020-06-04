#include <iostream>
#include <conio.h>
#include <time.h>
using namespace std;

int main()
{
	int *arr; // �������� ��� �������� ���'�� �� �����
	int size; // ����� ������

	// �������� ������� �������� ������
	cout << "Array size = ";
	cin >> size;

	if (size <= 0) { // �������� �� ����� ������ � �������
		cerr << "Invalid size" << endl;
		return 1;
	}

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
	cout << endl;
	int temp; // ����� ��� ����� ���������� ������ 

	// ���������� ����������
	for (int i = 0; i < size - 1; i++) {
		for (int j = 0; j < size - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				// ���� ���� ������
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}

	// ��������� ������������� ������
	cout << "Array after sorting:";
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
	_getch();
	delete[] arr; // ��������� ���'��

	return 0;
}