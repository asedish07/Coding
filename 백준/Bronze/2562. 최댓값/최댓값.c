#include <stdio.h>

int main() {
	int list[9], biggest, cnt = 1;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &list[i]);
	}
	biggest = list[0];
	for (int i = 1; i < 9; i++) {
		if (biggest < list[i]) {
			biggest = list[i];
			cnt = i + 1;
		}
	}
	printf("%d\n%d", biggest, cnt);

	return 0;
}