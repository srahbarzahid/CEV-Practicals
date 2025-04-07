read -p "enter the first number:" n1
read -p "enter the second number:" n2
echo "before swapping"
echo "first number:"$n1
echo "second number:"$n2
temp=$n1
n1=$n2
n2=$temp
echo "after swapping"
echo "first number:"$n1
echo "second number:"$n2
