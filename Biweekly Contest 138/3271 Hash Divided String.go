package main

func stringHash(s string, k int) string {
	r := ""
	n := len(s)
	i := 0
	for i < n {
		j := i
		v := 0
		for j < i+k && j < n {
			v += int(s[j] - 'a')
			j++
		}
		v = v % 26
		c := rune('a' + v)
		r += string(c)
		i = j
	}
	return r
}
