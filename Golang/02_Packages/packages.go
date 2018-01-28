/*
１。全てのGoフログラムはPackageで構成されせいる。
２。フログラムはmainPackageから実行を開始する。
*/

package main

/*
importするPackages
*/
import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Happy", math.Pi, "Day")
}
