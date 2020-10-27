#include <stdio.h>

int f(long long n, long long x)
{
	long long pow10;
	if (x <= n) return n == x;
	for (pow10 = 10; pow10 <= x && x % pow10 < n; pow10 *= 10)
		if (f(n - x % pow10, x / pow10)) return 1;
	return 0;
}

// N = m^2
long long T(long long m)
{
	long long sum = 0, n0, n;
	for (n0 = 9; n0 <= 10; n0++)
		for (n = n0; n <= m; n += 9)
			if (f(n, n * n)) sum += n * n;
	return sum;
}

int main(void)
{
	long long m = 1000000;
	printf("T(%lld) = %lld\n", m * m, T(m));
}