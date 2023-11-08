#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_SIZE 1000001

struct stack {
	int list[MAX_SIZE];
	int top;
} s;

void init() {
	s.top = -1;
	return;
}

int is_empty() {
	if (s.top == -1) return 1;
	return 0;
}

int is_full() {
	if (s.top == MAX_SIZE - 1) return 1;
	return 0;
}

void push(int value) {
	if (is_full()) {
		/* printf("ERROR: NO MORE SPACE\n"); */
		return;
	}
	s.list[++(s.top)] = value;
	return;
}

int peek() {
	if (is_empty()) {
		/* printf("ERROR: NO VALUE FOUND\n"); */
		return 0;
	}
	return s.list[(s.top)];
}

int pop() {
	if (is_empty()) {
		/* printf("ERROR: NO VALUE FOUND\n"); */
		return 0;
	}
	return s.list[(s.top)--];
}

int main(void) {
	init();
	int n, num1, num2;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &num1);
		if (num1 == 1) {
			scanf(" %d", &num2);
			push(num2);
		}
		else if (num1 == 2) {
			if (is_empty()) {
				printf("-1\n");
			}
			else {
				printf("%d\n", pop());
			}
		}
		else if (num1 == 3) {
			printf("%d\n", s.top + 1);
		}
		else if (num1 == 4) {
			if (is_empty()) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
		}
		else {
			if (is_empty()) {
				printf("-1\n");
			}
			else {
				printf("%d\n", peek());
			}
		}
	}

	return 0;
}