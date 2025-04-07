read -p "enter the base of triangle:" b
read -p "enter the height of triangle:" h
area=$(echo "scale=2; 0.5 * $b * $h" | bc)
echo "area of triangle is:"$area

