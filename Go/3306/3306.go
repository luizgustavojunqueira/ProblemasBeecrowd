package main

import (
	"fmt"
)

func MDC(a, b int) int {
	if b == 0 {
		return a
	}
	return MDC(b, a%b)
}

func MDCSlice(s []int) int {
	if len(s) == 1 {
		return s[0]
	}
	return MDC(s[0], MDCSlice(s[1:]))
}

func main() {

	var n, q int

	_, err := fmt.Scan(&n, &q)

	for err == nil {

		nums := make([]int, n)

		for i := 0; i < n; i++ {
			fmt.Scan(&nums[i])
		}

		for i := 0; i < q; i++ {
			var query int
			fmt.Scan(&query)

			switch query {
			case 1:
				var a, b, v int

				fmt.Scanf("%d %d %d", &a, &b, &v)

				for j := a - 1; j < b; j++ {
					nums[j] = nums[j] + v
				}
			case 2:
				var a, b int

				fmt.Scanf("%d %d", &a, &b)

				mdc := MDCSlice(nums[a-1 : b])

				fmt.Println(mdc)

			default:

			}
		}

		_, err = fmt.Scan(&n, &q)

	}
}
