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
	int n, num2;
	char num1[10];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", num1);
		if (strcmp(num1, "push") == 0) {
			scanf(" %d", &num2);
			push(num2);
		}
		else if (strcmp(num1, "pop") == 0) {
			if (is_empty()) {
				printf("-1\n");
			}
			else {
				printf("%d\n", pop());
			}
		}
		else if (strcmp(num1, "size") == 0) {
			printf("%d\n", s.top + 1);
		}
		else if (strcmp(num1, "empty") == 0) {
			if (is_empty()) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
		}
		else if (strcmp(num1, "top") == 0) {
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