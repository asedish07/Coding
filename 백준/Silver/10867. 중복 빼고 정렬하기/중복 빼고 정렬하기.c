#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_SIZE 2000

int arr[2001] = { 0 }, narr[100000];

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf(" %d", &narr[i]);
	}
	for (int i = 0; i < n; i++) {
		int a = narr[i];
		arr[a + 1000] += 1;
	}
	for (int i = 0; i <= MAX_SIZE; i++) {
		if (arr[i] != 0) {
			printf("%d ", i - 1000);
		}
	}

	return 0;
}