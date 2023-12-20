#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
	int list[1000];
	int n, tmp;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &list[i]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 1; j < n; j++) {
			if (list[j - 1] > list[j]) {
				tmp = list[j];
				list[j] = list[j - 1];
				list[j - 1] = tmp;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d\n", list[i]);
	}

	return 0;
}