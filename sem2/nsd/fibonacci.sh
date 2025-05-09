read -p "enter the limit: " n
a=0
b=1
echo $a
echo $b
i=2
while [ $i -lt $n ]
   do
     c=$(( $a + $b ))
     echo $c
     a=$b
     b=$c
     i=$(( $i + 1 ))
   done 
    
