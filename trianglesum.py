triangle=[
    [1],
    [2,3],
    [4,5,6],
    [7,8,9,6]]
sum_num=sum(int(digit)for rows in triangle for digit in rows)
print("sum",sum_num)
