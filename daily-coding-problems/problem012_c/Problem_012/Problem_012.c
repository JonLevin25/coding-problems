#include <stdio.h>
#include <assert.h>

int allowedSteps[] = {1, 2};
int uniqueClimbStrategies(int n) {
	if (n == 0) return 1;

	int result = 0;
	int stepTypesCount = sizeof(allowedSteps) / sizeof(int);
	for (int i = 0; i < stepTypesCount; i++) {
		if (allowedSteps[i] <= n) {
			result += uniqueClimbStrategies(n - allowedSteps[i]);
		}
	}

	return result;
}

void tests() {
	// 1: {[1]}
	assert(uniqueClimbStrategies(1) == 1);

	// 2: {[1, 1], [2]}
	assert(uniqueClimbStrategies(2) == 2);

	// 3: {[2, 1], [1, 2], [1, 1, 1]}
	assert(uniqueClimbStrategies(3) == 3);

	// 4: {[2, 2], [2, 1, 1], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]}
	assert(uniqueClimbStrategies(4) == 5);
}

int main() {
	tests();
	printf("All tests completed successfully!\n");
	return 0;
}