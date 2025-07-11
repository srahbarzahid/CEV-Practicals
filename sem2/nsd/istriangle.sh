read -p "Enter first side: " a
read -p "Enter second side: " b
read -p "Enter third side: " c
if [ $((a + b)) -gt $c ] && [ $((a + c)) -gt $b ] && [ $((b + c)) -gt $a ]; then
    echo "The numbers can form a triangle."
else
    echo "The numbers cannot form a triangle."
fi

