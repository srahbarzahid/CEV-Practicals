read -p "enter the number for reversing:" n
res=0
while [ $n -gt 0 ]
   do 
     rev=$(( $n % 10 ))
     res=$(( ($res * 10) + $rev ))
     n=$(( n / 10))
   done
 echo "reveres is ="$res     
