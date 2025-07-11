read -p "enter starting number: " n1
read -p "enter ending range: " n2
echo "Prime numbers between $n1 and $n2 are:"
for ((i=$n1;i<=$n2; i++));do
    if [ $i -lt 2 ]; then
        continue
    fi
    prime=1
    for ((j=2; j<i; j++))
    do
        if [ $((i % j)) -eq 0 ]; then
            prime=0
            break
        fi
    done
    if [ $prime -eq 1 ]; then
        echo $i
    fi
done

