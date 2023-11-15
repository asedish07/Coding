#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int n, num = 0, sum = 0;
	int li1[1000], li2[1000];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf(" %d", &li1[i]);
		sum += li1[i];
	}
	for (int i = 0; i < n; i++) {
		scanf(" %d", &li2[i]);
	}
	for (int i = 0; i < n; i++) {
		if (li2[i] == 0) {
			num += li1[i];
		}
	}
	printf("%d\n%d", sum, num);

	return 0;
}