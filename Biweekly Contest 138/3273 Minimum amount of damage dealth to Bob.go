package main

import (
	"sort"
)

type A struct {
	a int
	h int
}

func c(a, b A, p int) bool {
	return int64(a.a)*int64((b.h+p-1)/p) > int64(b.a)*int64((a.h+p-1)/p)
}

func minDamage(power int, damage, health []int) int64 {
	s := make([]A, len(damage))
	for i := range s {
		s[i] = A{damage[i], health[i]}
	}

	sort.Slice(s, func(i, j int) bool {
		return c(s[i], s[j], power)
	})

	var t int64
	var c int64
	for _, v := range s {
		c += int64(v.a)
	}

	for _, v := range s {
		ttd := (v.h + power - 1) / power
		t += c * int64(ttd)
		c -= int64(v.a)
	}

	return t
}
