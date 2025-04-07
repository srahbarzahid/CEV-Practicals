read -p "enter the number: " n
i=1
sum=0
while [ $i -le $n ];
do
  sum=`expr $sum + $i` 
  i=`expr $i + 1`
done
echo "sum=$sum"  
