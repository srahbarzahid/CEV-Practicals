sum=0
i="y"

while [ "$i"=="y" ]; do
  echo "Enter the first number:"
  read a
  echo "Enter the second number:"
  read b
  echo "1. Addition"
  echo "2. Subtraction"
  echo "3. Division"
  echo "4. Multiplication"
  echo "Choose your option:"
  read opt

  case $opt in
    1) sum=$((a + b))
       echo "Sum: $sum" ;;
    2) sum=$((a - b))
       echo "Difference: $sum" ;;
    3) sum=$(echo "scale=2; $a / $b" | bc) 
         echo "Division: $sum";;
    4) sum=$((a * b))
       echo "Product: $sum" ;;
    *) echo "Invalid option." ;;
  esac

  echo "Do you want to continue? [y/n]"
  read i
  if [ "$i" != "y" ]; then
    exit 0
  fi
done

