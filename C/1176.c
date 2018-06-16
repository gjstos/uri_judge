#include <stdio.h>

int main()
{
	int fibonacci[] = {0}, c = 0 , k, f = 1, i, ff;
	
	scanf("%d", &k);
	for(i = 0; i < k; i++){
		scanf("%d", &ff);
		while (c < k){
			fibonacci[c + 1] = f;
			f = f + fibonacci[c];
			c += 1;
		}
		printf("Fib(%d) = %d\n", ff, fibonacci[c - 1]);
	}
	
	return 0;
}
