package main

import "fmt"

/*
  C,C++,Javaとパラメタ宣言する方法が違う
*/
func add(x int, y int) int {
	return x + y
}

/*
  同じタイプのパラメタなら、最後にタイプを宣言してもいい。
*/
func add_num2(x, y int) int {
	return x + y

}
func main() {
	fmt.Printf("%d + %d = %d\n", 22, 33, add(22, 33))
	fmt.Printf("%d + %d = %d\n", 22, 33, add_num2(22, 33))
}
